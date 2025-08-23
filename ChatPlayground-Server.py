from flask import Flask, request, jsonify, Response
from openai import OpenAI
import json
import os
from flask_cors import CORS
from dotenv import load_dotenv
from together import Together

# Load environment variables from .env file in parent directory
load_dotenv(dotenv_path='/Users/apple/Desktop/AI4DEV/Assignment/Assingment-3-LLMs-playground/pages/.env')

app = Flask(__name__)
CORS(app)

# Configure OpenAI client
openai_client = OpenAI(api_key=os.getenv("API_KEYS"))

# Configure Together AI client
together_client = Together(api_key=os.getenv("TOGETHER_API"))

# Dictionary to store chat histories by session ID
chat_histories = {}

@app.route('/', methods=['POST'])
def chat():
    try:
        data = request.json
        message = data.get('message', {})
        context = data.get('context', [])
        session_id = data.get('sessionId', 'default')
        model = data.get('model', 'gpt-4o-mini')
        temperature = data.get('temperature', 0.7)
        top_p = data.get('top_p', 0.9)
        stream = data.get('stream', False)
        
        # Store or update chat history for this session
        if session_id not in chat_histories:
            chat_histories[session_id] = []
        
        # Add user message to history
        user_message = {"role": "user", "content": message.get('content', '')}
        chat_histories[session_id].append(user_message)
        
        # Prepare messages for OpenAI API
        messages = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]
        
        # Add context from session history
        messages.extend(chat_histories[session_id])
        
        if stream:
            def generate():
                try:
                    # Determine which client to use based on model name
                    if 'gpt' in model.lower():
                        # Use OpenAI for GPT models
                        response = openai_client.chat.completions.create(
                            model=model,
                            messages=messages,
                            temperature=temperature,
                            top_p=top_p,
                            stream=True
                        )
                    else:
                        # Use Together AI for other models
                        response = together_client.chat.completions.create(
                            model=model,
                            messages=messages,
                            temperature=temperature,
                            top_p=top_p,
                            stream=True
                        )
                    
                    assistant_content = ""
                    
                    for chunk in response:
                        # Handle different response formats for both providers
                        content = None
                        
                        if 'gpt' in model.lower():
                            # OpenAI format
                            if hasattr(chunk, 'choices') and chunk.choices[0].delta.content:
                                content = chunk.choices[0].delta.content
                        else:
                            # Together AI format - similar to OpenAI
                            if hasattr(chunk, 'choices') and chunk.choices[0].delta.content:
                                content = chunk.choices[0].delta.content
                        
                        if content:
                            assistant_content += content
                            yield f"data: {json.dumps({'content': content})}\n\n"
                    
                    # Add assistant response to history
                    assistant_message = {"role": "assistant", "content": assistant_content}
                    chat_histories[session_id].append(assistant_message)
                    
                    yield f"data: {json.dumps({'done': True})}\n\n"
                    
                except Exception as e:
                    yield f"data: {json.dumps({'error': str(e)})}\n\n"
            
            return Response(generate(), mimetype='text/event-stream')
        
        else:
            # Non-streaming response
            try:
                if 'gpt' in model.lower():
                    # Use OpenAI for GPT models
                    response = openai_client.chat.completions.create(
                        model=model,
                        messages=messages,
                        temperature=temperature,
                        top_p=top_p
                    )
                    assistant_content = response.choices[0].message.content
                else:
                    # Use Together AI for other models
                    response = together_client.chat.completions.create(
                        model=model,
                        messages=messages,
                        temperature=temperature,
                        top_p=top_p
                    )
                    assistant_content = response.choices[0].message.content
                
                assistant_message = {"role": "assistant", "content": assistant_content}
                chat_histories[session_id].append(assistant_message)
                
                return jsonify({
                    'content': assistant_content,
                    'session_id': session_id,
                    'model_used': 'OpenAI' if 'gpt' in model.lower() else 'Together AI'
                })
            except Exception as e:
                return jsonify({'error': f"Model error: {str(e)}"}), 500
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/status', methods=['GET'])
def get_status():
    """Check API status and available providers"""
    status = {
        'server': 'running',
        'providers': {
            'openai': 'configured' if os.getenv("API_KEYS") else 'not configured',
            'together': 'configured' if os.getenv("TOGETHER_API") else 'not configured'
        },
        'available_models': {
            'openai': ['gpt-4o-mini', 'gpt-4o', 'gpt-4', 'gpt-3.5-turbo'],
            'together': ['meta-llama/Llama-2-7b-chat-hf', 'mistralai/Mixtral-8x7B-Instruct-v0.1', 'custom']
        }
    }
    return jsonify(status)

@app.route('/history/<session_id>', methods=['GET'])
def get_history(session_id):
    """Get chat history for a specific session"""
    history = chat_histories.get(session_id, [])
    return jsonify({'history': history})

@app.route('/clear/<session_id>', methods=['DELETE'])
def clear_history(session_id):
    """Clear chat history for a specific session"""
    if session_id in chat_histories:
        del chat_histories[session_id]
    return jsonify({'message': 'History cleared'})

if __name__ == '__main__':
    print("Starting Flask server...")
    print("Make sure to set your OPENAI_API_KEY in the .env file")
    
    # Get port from environment variable or default to 5001
    port = int(os.getenv("FLASK_PORT", 5001))
    debug = os.getenv("FLASK_DEBUG", "True").lower() == "true"
    
    print(f"Server will be running on http://localhost:{port}")
    app.run(host='0.0.0.0', port=port, debug=debug)