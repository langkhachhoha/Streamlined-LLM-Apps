import streamlit as st
import requests
import json
import base64
import os
from datetime import datetime
import time

st.set_page_config(
    page_title="Doctor Chatbot - AI Health Consultant",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Function to encode image to base64
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

# Get doctor images
doctor_image_path = "/Users/apple/Desktop/LLM-apps/image/Doctor.png"
doctor_base64 = get_base64_image(doctor_image_path)

doctor_1_image_path = "/Users/apple/Desktop/LLM-apps/image/Doctor_1.png"
doctor_1_base64 = get_base64_image(doctor_1_image_path)

# Get VinBig logo for header
vinbig_logo_path = "/Users/apple/Desktop/LLM-apps/image/logo_vinbig.png"
vinbig_logo_base64 = get_base64_image(vinbig_logo_path)

# Enhanced Medical Styling with Vibrant Colors & Animations
if doctor_base64:
    background_style = f"background-image: url('data:image/png;base64,{doctor_base64}');"
else:
    background_style = "background: linear-gradient(135deg, #f0f8ff 0%, #e1f2ff 25%, #d1ecff 50%, #c1e6ff 75%, #b1e0ff 100%);"

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Poppins:wght@300;400;500;600;700;800;900&family=Outfit:wght@300;400;500;600;700;800;900&display=swap');
    

    
    .stApp {{
        {background_style}
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        font-family: 'Outfit', 'Inter', sans-serif;
        min-height: 100vh;
        position: relative;
    }}
    
    .stApp::before {{
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(8px);
        z-index: -1;
    }}
    
    /* Chat Container Styling */
    .chat-container {{
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 20px 60px rgba(0, 102, 204, 0.1);
        border: 1px solid rgba(0, 102, 204, 0.1);
        backdrop-filter: blur(10px);
    }}
    
    /* Chat Message Styling */
    .chat-message {{
        padding: 1rem 1.5rem;
        margin: 0.8rem 0;
        border-radius: 15px;
        max-width: 80%;
        word-wrap: break-word;
        animation: slideInMessage 0.3s ease-out;
    }}
    
    .user-message {{
        background: linear-gradient(135deg, #0066cc 0%, #4da6ff 100%);
        color: white;
        margin-left: auto;
        border-bottom-right-radius: 5px;
        box-shadow: 0 4px 15px rgba(0, 102, 204, 0.3);
    }}
    
    .bot-message {{
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        color: #333;
        margin-right: auto;
        border-bottom-left-radius: 5px;
        border-left: 4px solid #28a745;
        box-shadow: 0 4px 15px rgba(40, 167, 69, 0.15);
    }}
    
    .typing-indicator {{
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-left: 4px solid #28a745;
        padding: 1rem 1.5rem;
        border-radius: 15px;
        border-bottom-left-radius: 5px;
        margin: 0.8rem 0;
        max-width: 80%;
        animation: pulse 1.5s infinite;
    }}
    
    /* Medical Title Styling */
    .medical-title {{
        font-family: 'Outfit', sans-serif;
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(135deg, #0066cc 0%, #4da6ff 50%, #00cc66 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: 0 4px 6px rgba(0, 102, 204, 0.1);
        margin-bottom: 0.5rem;
        animation: glow 3s ease-in-out infinite alternate;
    }}
    
    .subtitle {{
        font-family: 'Inter', sans-serif;
        font-size: 1.2rem;
        font-weight: 500;
        color: #0066cc;
        text-align: center;
        margin-bottom: 2rem;
        opacity: 0.9;
    }}
    
    /* Input Styling */
    .stTextInput > div > div > input {{
        border-radius: 25px;
        border: 2px solid #e3f2fd;
        padding: 12px 20px;
        font-size: 1rem;
        transition: all 0.3s ease;
        background: rgba(255, 255, 255, 0.9);
    }}
    
    .stTextInput > div > div > input:focus {{
        border-color: #0066cc;
        box-shadow: 0 0 20px rgba(0, 102, 204, 0.2);
        background: white;
    }}
    
    /* Button Styling */
    .stButton > button {{
        background: linear-gradient(135deg, #0066cc 0%, #4da6ff 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 12px 30px;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 102, 204, 0.3);
    }}
    
    .stButton > button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 102, 204, 0.4);
    }}
    
    /* Patient Info Styling */
    .patient-info-card {{
        background: linear-gradient(135deg, #e3f2fd 0%, #f3e5f5 100%);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid #0066cc;
        box-shadow: 0 4px 15px rgba(0, 102, 204, 0.1);
    }}
    
    /* Animations */
    @keyframes slideInMessage {{
        from {{
            opacity: 0;
            transform: translateY(20px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    
    @keyframes pulse {{
        0%, 100% {{
            opacity: 1;
        }}
        50% {{
            opacity: 0.7;
        }}
    }}
    
    @keyframes glow {{
        from {{
            text-shadow: 0 0 20px rgba(0, 102, 204, 0.2);
        }}
        to {{
            text-shadow: 0 0 40px rgba(0, 102, 204, 0.4);
        }}
    }}
    
    /* Sidebar Styling */
    .css-1d391kg {{
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
    }}
    
    /* Status indicators */
    .status-indicator {{
        display: inline-flex;
        align-items: center;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 500;
        margin: 0.5rem 0;
    }}
    
    .status-online {{
        background: rgba(40, 167, 69, 0.1);
        color: #28a745;
        border: 1px solid rgba(40, 167, 69, 0.3);
    }}
    
    .status-offline {{
        background: rgba(220, 53, 69, 0.1);
        color: #dc3545;
        border: 1px solid rgba(220, 53, 69, 0.3);
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Load patient data
@st.cache_data
def load_patient_data():
    """Load patient data from JSON file"""
    try:
        json_file_path = "/Users/apple/Desktop/LLM-apps/Doctor_app/patient_data.json"
        if os.path.exists(json_file_path):
            with open(json_file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
    except Exception as e:
        st.error(f"Error loading patient data: {e}")
    return None

def check_server_status():
    """Check if chatbot server is running"""
    try:
        response = requests.get("http://localhost:8502/health", timeout=3)
        return response.status_code == 200
    except:
        return False

def send_chat_message(messages):
    """Send message to chatbot server and get streaming response"""
    try:
        response = requests.post(
            "http://localhost:8502/chat",
            json={
                "messages": messages,
                "stream": True
            },
            stream=True,
            timeout=30
        )
        
        if response.status_code == 200:
            return response
        else:
            st.error(f"Server error: {response.status_code}")
            return None
            
    except requests.exceptions.ConnectionError:
        st.error("🔌 Không thể kết nối đến server chatbot. Vui lòng khởi động server trước.")
        return None
    except Exception as e:
        st.error(f"❌ Lỗi khi gửi tin nhắn: {e}")
        return None

# Page Header
st.markdown('<h1 class="medical-title">🤖 Dr. HealthBot</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Trợ lý AI tư vấn sức khỏe cá nhân hóa | Cuộc trò chuyện thông minh về sức khỏe</p>', unsafe_allow_html=True)

# Check server status
server_online = check_server_status()

if server_online:
    st.markdown('<div class="status-indicator status-online">🟢 Server đang hoạt động</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="status-indicator status-offline">🔴 Server không khả dụng</div>', unsafe_allow_html=True)
    st.warning("⚠️ Vui lòng khởi động chatbot server để sử dụng tính năng này.")
    st.code("python Doctor_chatbot_server.py", language="bash")

# Load patient data
patient_data = load_patient_data()

# Sidebar with patient information
with st.sidebar:
    st.markdown("### 👤 Thông tin bệnh nhân")
    
    if patient_data and 'current_patient' in patient_data:
        current_patient = patient_data['current_patient']
        personal_info = current_patient.get('personal_info', {})
        
        st.success("✅ Đã có dữ liệu bệnh nhân")
        
        # Basic info
        st.markdown(f"""
        <div class="patient-info-card">
            <h4>📋 Thông tin cơ bản</h4>
            <p><strong>Họ tên:</strong> {personal_info.get('full_name', 'N/A')}</p>
            <p><strong>Ngày sinh:</strong> {personal_info.get('birth_date', 'N/A')}</p>
            <p><strong>Giới tính:</strong> {personal_info.get('gender', 'N/A')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Health analysis if available
        diabetes_analysis = current_patient.get('diabetes_analysis', {})
        if diabetes_analysis:
            ai_diagnosis = diabetes_analysis.get('ai_diagnosis', {})
            st.markdown(f"""
            <div class="patient-info-card">
                <h4>🔬 Kết quả phân tích</h4>
                <p><strong>Nguy cơ tiểu đường:</strong> {ai_diagnosis.get('risk_level', 'N/A')}</p>
                <p><strong>Xác suất:</strong> {ai_diagnosis.get('probability', 0)*100:.1f}%</p>
                <p><strong>Độ tin cậy:</strong> {ai_diagnosis.get('confidence', 0):.1f}%</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Chưa có thông tin bệnh nhân")
        st.info("Vui lòng đăng ký thông tin ở trang chính trước khi sử dụng chatbot.")
    
    st.markdown("---")
    
    # Quick actions
    st.markdown("### ⚡ Hành động nhanh")
    if st.button("🔄 Làm mới cuộc trò chuyện"):
        st.session_state.chat_messages = []
        st.rerun()
    
    if st.button("🏠 Về trang chủ"):
        st.switch_page("Homepage.py")

# Initialize chat messages
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []
    
    # Welcome message
    welcome_msg = """👋 Xin chào! Tôi là Dr. HealthBot - trợ lý AI tư vấn sức khỏe của bạn.

🎯 **Tôi có thể giúp bạn:**
- 💬 Trả lời câu hỏi về tình trạng sức khỏe cá nhân
- 📊 Giải thích kết quả phân tích y tế
- 🎯 Đưa ra lời khuyên cá nhân hóa dựa trên thông tin của bạn
- 🏥 Hướng dẫn khi nào cần gặp bác sĩ chuyên khoa
- 🔍 Tư vấn về dinh dưỡng, tập luyện và lối sống

Bạn có câu hỏi gì về sức khỏe mà tôi có thể hỗ trợ không? 😊"""
    
    st.session_state.chat_messages.append({
        "role": "assistant",
        "content": welcome_msg
    })

# Chat container
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# Display chat messages with personalized names
for message in st.session_state.chat_messages:
    if message["role"] == "user":
        # Get user name from patient data
        user_name = "Bạn"  # Default fallback
        user_initial = "👤"  # Default avatar
        if patient_data and 'current_patient' in patient_data:
            personal_info = patient_data['current_patient'].get('personal_info', {})
            full_name = personal_info.get('full_name', '')
            if full_name:
                # Use first name only for a more personal touch
                user_name = full_name.split()[-1] if full_name.split() else "Bạn"
                # Get first letter of the name for avatar
                user_initial = full_name[0].upper() if full_name else "👤"
        
        st.markdown(f"""
        <div class="chat-message user-message" style="position: relative;">
            <div style="position: absolute; right: -50px; top: 10px; width: 40px; height: 40px; 
                        border-radius: 50%; background: linear-gradient(135deg, #64748b 0%, #475569 100%); 
                        display: flex; align-items: center; justify-content: center; font-size: 1rem; 
                        font-weight: 600; color: white; box-shadow: 0 4px 15px rgba(100, 116, 139, 0.2); 
                        border: 3px solid white; font-family: 'Inter', sans-serif;">
                {user_initial}
            </div>
            <strong style="color: #334155;">{user_name}:</strong><br>{message["content"]}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="chat-message bot-message">
            <strong>🤖 Dr. HealthBot:</strong><br>{message["content"]}
        </div>
        """, unsafe_allow_html=True)

# Chat input
if server_online:
    # Use a form to handle input properly
    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_input(
            "Hỏi Dr. HealthBot về sức khỏe...",
            placeholder="Ví dụ: Chỉ số BMI của tôi có bình thường không?",
            key="user_input_form"
        )
        
        col1, col2 = st.columns([3, 1])
        with col2:
            send_button = st.form_submit_button("📤 Gửi", type="primary")
    
    if send_button and user_input.strip():
        # Add user message
        st.session_state.chat_messages.append({
            "role": "user",
            "content": user_input
        })
        
        # Prepare messages for API (exclude welcome message for API)
        api_messages = []
        for msg in st.session_state.chat_messages[1:]:  # Skip welcome message
            api_messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })
        
        # Show typing indicator
        typing_placeholder = st.empty()
        typing_placeholder.markdown("""
        <div class="typing-indicator">
            🤖 Dr. HealthBot đang suy nghĩ...
        </div>
        """, unsafe_allow_html=True)
        
        # Get response from server
        response = send_chat_message(api_messages)
        
        if response:
            # Stream response
            full_response = ""
            response_placeholder = st.empty()
            
            try:
                for line in response.iter_lines():
                    if line:
                        line = line.decode('utf-8')
                        if line.startswith('data: '):
                            data = json.loads(line[6:])
                            if 'content' in data:
                                if data['content'] == '[DONE]':
                                    break
                                full_response += data['content']
                                response_placeholder.markdown(f"""
                                <div class="chat-message bot-message">
                                    <strong>🤖 Dr. HealthBot:</strong><br>{full_response}▊
                                </div>
                                """, unsafe_allow_html=True)
                
                # Remove typing indicator and show final response
                typing_placeholder.empty()
                response_placeholder.markdown(f"""
                <div class="chat-message bot-message">
                    <strong>🤖 Dr. HealthBot:</strong><br>{full_response}
                </div>
                """, unsafe_allow_html=True)
                
                # Add to chat history
                st.session_state.chat_messages.append({
                    "role": "assistant",
                    "content": full_response
                })
                
            except Exception as e:
                typing_placeholder.empty()
                st.error(f"❌ Lỗi khi nhận phản hồi: {e}")
        else:
            typing_placeholder.empty()
        
        # Rerun to refresh the chat
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    ⚠️ <strong>Lưu ý quan trọng:</strong> Dr. HealthBot chỉ mang tính tham khảo và giáo dục. 
    Với các vấn đề sức khỏe nghiêm trọng hoặc cấp tính, vui lòng tham khảo ý kiến bác sĩ chuyên khoa.
    <br><br>
    🏥 <strong>VinBig Doctor App</strong> - Công nghệ AI phục vụ sức khỏe cộng đồng
</div>
""", unsafe_allow_html=True)
