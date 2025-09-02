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
    
    /* Enhanced Chat Message Styling - Modern & Stylish */
    .chat-message {{
        padding: 1.8rem 2.2rem;
        margin: 1.5rem 0;
        border-radius: 24px;
        max-width: 85%;
        word-wrap: break-word;
        font-size: 1.05rem;
        line-height: 1.6;
        box-shadow: 0 12px 32px rgba(0,0,0,0.08);
        position: relative;
        backdrop-filter: blur(20px);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        border: 1px solid rgba(255,255,255,0.1);
    }}
    
    .chat-message:hover {{
        transform: translateY(-2px);
        box-shadow: 0 16px 40px rgba(0,0,0,0.12);
    }}
    
    /* User Messages - Professional Design with Orange Theme */
    .user-message {{
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.95) 0%, 
            rgba(254, 249, 245, 0.95) 100%);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(249, 115, 22, 0.15);
        border-left: 6px solid #f97316;
        color: #0f172a;
        margin-left: auto;
        border-bottom-right-radius: 8px;
        box-shadow: 0 8px 32px rgba(249, 115, 22, 0.1);
        animation: slideInRight 0.6s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }}
    
    .user-message::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 4px;
        height: 100%;
        background: linear-gradient(180deg, #f97316 0%, #ea580c 100%);
        border-radius: 0 2px 2px 0;
    }}
    
    /* Bot Messages - Professional Medical Design */
    .bot-message {{
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.95) 0%, 
            rgba(248, 250, 252, 0.95) 100%);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(34, 197, 94, 0.15);
        border-left: 6px solid #22c55e;
        color: #0f172a;
        margin-right: auto;
        border-bottom-left-radius: 8px;
        box-shadow: 0 8px 32px rgba(34, 197, 94, 0.1);
        animation: slideInLeft 0.6s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }}
    
    .bot-message::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 4px;
        height: 100%;
        background: linear-gradient(180deg, #22c55e 0%, #16a34a 100%);
        border-radius: 0 2px 2px 0;
    }}
    
    /* Enhanced Typing Indicator */
    .typing-indicator {{
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.95) 0%, 
            rgba(248, 250, 252, 0.95) 100%);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(34, 197, 94, 0.15);
        border-left: 6px solid #22c55e;
        padding: 1.8rem 2.2rem;
        border-radius: 24px;
        border-bottom-left-radius: 8px;
        margin: 1.5rem 0;
        max-width: 85%;
        animation: typingPulse 2s infinite ease-in-out;
        box-shadow: 0 8px 32px rgba(34, 197, 94, 0.1);
        position: relative;
    }}
    
    @keyframes slideInRight {{
        from {{
            opacity: 0;
            transform: translateX(60px) scale(0.95);
        }}
        to {{
            opacity: 1;
            transform: translateX(0) scale(1);
        }}
    }}
    
    @keyframes slideInLeft {{
        from {{
            opacity: 0;
            transform: translateX(-60px) scale(0.95);
        }}
        to {{
            opacity: 1;
            transform: translateX(0) scale(1);
        }}
    }}
    
    @keyframes typingPulse {{
        0%, 100% {{
            transform: scale(1);
            box-shadow: 0 8px 32px rgba(34, 197, 94, 0.1);
        }}
        50% {{
            transform: scale(1.02);
            box-shadow: 0 12px 40px rgba(34, 197, 94, 0.15);
        }}
    }}
    
    /* Medical Title Styling */
    .medical-title {{
        font-family: 'Outfit', sans-serif;
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(135deg, #22c55e 0%, #16a34a 50%, #15803d 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: 0 4px 6px rgba(34, 197, 94, 0.1);
        margin-bottom: 0.5rem;
        animation: glow 3s ease-in-out infinite alternate;
    }}
    
    .subtitle {{
        font-family: 'Outfit', 'Inter', sans-serif;
        font-size: 1.3rem;
        font-weight: 700;
        color: #0f172a;
        text-align: center;
        margin: 2rem auto;
        padding: 2rem 3rem;
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.98) 0%, 
            rgba(240, 253, 244, 0.95) 50%,
            rgba(255, 255, 255, 0.98) 100%);
        border: 3px solid transparent;
        background-clip: padding-box;
        border-radius: 24px;
        backdrop-filter: blur(20px);
        box-shadow: 
            0 20px 60px rgba(34, 197, 94, 0.15),
            0 0 0 1px rgba(34, 197, 94, 0.1),
            inset 0 1px 0 rgba(255, 255, 255, 0.8);
        max-width: 850px;
        position: relative;
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
        overflow: hidden;
        animation: subtitlePulse 4s ease-in-out infinite;
    }}
    
    .subtitle::before {{
        content: '';
        position: absolute;
        top: -2px;
        left: -2px;
        right: -2px;
        bottom: -2px;
        background: linear-gradient(
            45deg, 
            #22c55e 0%, 
            #16a34a 25%, 
            #15803d 50%, 
            #16a34a 75%, 
            #22c55e 100%
        );
        background-size: 300% 300%;
        border-radius: 24px;
        z-index: -1;
        animation: gradientFlow 3s ease infinite;
        opacity: 0.8;
    }}
    
    .subtitle::after {{
        content: '"';
        position: absolute;
        top: 0.5rem;
        left: 1.5rem;
        font-size: 3rem;
        color: #22c55e;
        opacity: 0.3;
        font-family: 'Georgia', serif;
        line-height: 1;
        animation: quoteFloat 3s ease-in-out infinite alternate;
    }}
    
    .subtitle .quote-end {{
        position: absolute;
        bottom: 0.5rem;
        right: 1.5rem;
        font-size: 3rem;
        color: #22c55e;
        opacity: 0.3;
        font-family: 'Georgia', serif;
        line-height: 1;
        transform: rotate(180deg);
        animation: quoteFloat 3s ease-in-out infinite alternate-reverse;
    }}
    
    .subtitle:hover {{
        transform: translateY(-5px) scale(1.02);
        box-shadow: 
            0 30px 80px rgba(34, 197, 94, 0.25),
            0 0 0 1px rgba(34, 197, 94, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 1);
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 1) 0%, 
            rgba(240, 253, 244, 1) 50%,
            rgba(255, 255, 255, 1) 100%);
        animation-play-state: paused;
    }}
    
    .subtitle:hover::before {{
        opacity: 1;
        animation-duration: 1.5s;
    }}
    
    .subtitle:hover::after,
    .subtitle:hover .quote-end {{
        opacity: 0.6;
        color: #15803d;
        transform: scale(1.1);
    }}
    
    .subtitle:hover .quote-end {{
        transform: rotate(180deg) scale(1.1);
    }}
    
    @keyframes subtitlePulse {{
        0%, 100% {{
            box-shadow: 
                0 20px 60px rgba(34, 197, 94, 0.15),
                0 0 0 1px rgba(34, 197, 94, 0.1),
                inset 0 1px 0 rgba(255, 255, 255, 0.8);
        }}
        50% {{
            box-shadow: 
                0 25px 70px rgba(34, 197, 94, 0.2),
                0 0 0 1px rgba(34, 197, 94, 0.15),
                inset 0 1px 0 rgba(255, 255, 255, 0.9);
        }}
    }}
    
    @keyframes gradientFlow {{
        0% {{
            background-position: 0% 50%;
        }}
        50% {{
            background-position: 100% 50%;
        }}
        100% {{
            background-position: 0% 50%;
        }}
    }}
    
    @keyframes quoteFloat {{
        0% {{
            transform: translateY(0) scale(1);
            opacity: 0.3;
        }}
        100% {{
            transform: translateY(-8px) scale(1.05);
            opacity: 0.5;
        }}
    }}
    
    @keyframes sparkleAnimation {{
        0%, 100% {{
            opacity: 0;
            transform: scale(0);
        }}
        50% {{
            opacity: 1;
            transform: scale(1.5);
        }}
    }}
    
    /* Enhanced Modern Input Styling */
    .stTextInput > div > div > input {{
        border-radius: 20px;
        border: 2px solid rgba(249, 115, 22, 0.1);
        padding: 16px 24px;
        font-size: 1.05rem;
        font-weight: 400;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
        font-family: 'Inter', sans-serif;
    }}
    
    .stTextInput > div > div > input:focus {{
        border-color: #f97316;
        box-shadow: 0 0 0 4px rgba(249, 115, 22, 0.1), 0 8px 24px rgba(249, 115, 22, 0.15);
        transform: translateY(-1px);
        background: rgba(255, 255, 255, 0.95);
    }}
    
    .stTextInput > div > div > input::placeholder {{
        color: #94a3b8;
        font-weight: 400;
    }}
    
    /* Enhanced Button Styling */
    .stButton > button {{
        background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 16px 32px;
        font-size: 1.05rem;
        font-weight: 600;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 16px rgba(34, 197, 94, 0.25);
        font-family: 'Inter', sans-serif;
        position: relative;
        overflow: hidden;
    }}
    
    .stButton > button::before {{
        content: '💬';
        margin-right: 8px;
        font-size: 1.1rem;
    }}
    
    .stButton > button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(34, 197, 94, 0.35);
        background: linear-gradient(135deg, #16a34a 0%, #15803d 100%);
    }}
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
            text-shadow: 0 0 20px rgba(34, 197, 94, 0.2);
        }}
        to {{
            text-shadow: 0 0 40px rgba(34, 197, 94, 0.4);
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
st.markdown('<h1 class="medical-title">🤖 VITA Chatbot</h1>', unsafe_allow_html=True)
st.markdown('''
<p class="subtitle">
    <span class="sparkle"></span>
    <span class="sparkle"></span>
    <span class="sparkle"></span>
    <span class="sparkle"></span>
    Hiểu bạn từng nhịp – Chăm sóc tận tâm
    <span class="quote-end">"</span>
</p>
''', unsafe_allow_html=True)

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
# st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# Display chat messages with enhanced modern styling
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
        
        # Get current time for timestamp
        timestamp = datetime.now().strftime("%H:%M")
        
        st.markdown(f"""
        <div class="chat-message user-message">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.8rem;">
                <div style="display: flex; align-items: center; gap: 0.8rem;">
                    <div style="width: 40px; height: 40px; border-radius: 50%; 
                                background: linear-gradient(135deg, #f97316 0%, #ea580c 100%); 
                                display: flex; align-items: center; justify-content: center; 
                                font-size: 1rem; color: white; font-weight: 600;
                                box-shadow: 0 4px 12px rgba(249, 115, 22, 0.3);
                                border: 2px solid rgba(255, 255, 255, 0.2);
                                font-family: 'Inter', sans-serif;">
                        {user_initial}
                    </div>
                    <div>
                        <div style="font-weight: 700; color: #f97316; font-size: 1rem; margin-bottom: 2px;">{user_name}</div>
                        <div style="color: #64748b; font-size: 0.8rem; font-weight: 500;">Bệnh nhân</div>
                    </div>
                </div>
                <span style="color: #94a3b8; font-size: 0.85rem; font-weight: 500;">{timestamp}</span>
            </div>
            <div style="color: #1e293b; font-size: 1.05rem; line-height: 1.6; font-weight: 400;">
                {message["content"]}
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Get current time for timestamp
        timestamp = datetime.now().strftime("%H:%M")
        
        st.markdown(f"""
        <div class="chat-message bot-message">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.8rem;">
                <div style="display: flex; align-items: center; gap: 0.8rem;">
                    <div style="width: 40px; height: 40px; border-radius: 50%; 
                                background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%); 
                                display: flex; align-items: center; justify-content: center; 
                                font-size: 1.2rem; color: white; 
                                box-shadow: 0 4px 12px rgba(34, 197, 94, 0.3);
                                border: 2px solid rgba(255, 255, 255, 0.2);">
                        👩🏼‍⚕️
                    </div>
                    <div>
                        <div style="font-weight: 700; color: #22c55e; font-size: 1rem; margin-bottom: 2px;">Dr. HealthBot</div>
                        <div style="color: #64748b; font-size: 0.8rem; font-weight: 500;">AI Health Consultant</div>
                    </div>
                </div>
                <span style="color: #94a3b8; font-size: 0.85rem; font-weight: 500;">{timestamp}</span>
            </div>
            <div style="color: #1e293b; font-size: 1.05rem; line-height: 1.6; font-weight: 400;">
                {message["content"]}
            </div>
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
        
        # Show enhanced typing indicator with modern design
        typing_placeholder = st.empty()
        typing_placeholder.markdown("""
        <div class="typing-indicator">
            <div style="display: flex; align-items: center; gap: 0.8rem; margin-bottom: 0.8rem;">
                <div style="width: 40px; height: 40px; border-radius: 50%; 
                            background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%); 
                            display: flex; align-items: center; justify-content: center; 
                            font-size: 1.2rem; color: white; 
                            box-shadow: 0 4px 12px rgba(34, 197, 94, 0.3);
                            border: 2px solid rgba(255, 255, 255, 0.2);
                            animation: doctorThinking 1.5s infinite;">
                    🩺
                </div>
                <div>
                    <div style="font-weight: 700; color: #22c55e; font-size: 1rem; margin-bottom: 2px;">Dr. HealthBot</div>
                    <div style="color: #64748b; font-size: 0.8rem; font-weight: 500;">AI Health Consultant</div>
                </div>
            </div>
            <div style="display: flex; align-items: center; color: #64748b; font-size: 1rem;">
                <span style="margin-right: 12px;">Đang phân tích và tư vấn</span>
                <div style="display: flex; gap: 4px;">
                    <div style="width: 8px; height: 8px; border-radius: 50%; background: #22c55e; animation: typingDot1 1.4s infinite;"></div>
                    <div style="width: 8px; height: 8px; border-radius: 50%; background: #22c55e; animation: typingDot2 1.4s infinite;"></div>
                    <div style="width: 8px; height: 8px; border-radius: 50%; background: #22c55e; animation: typingDot3 1.4s infinite;"></div>
                </div>
            </div>
        </div>
        <style>
        @keyframes doctorThinking {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
        @keyframes typingDot1 {
            0%, 80%, 100% { transform: scale(0); opacity: 0.5; }
            40% { transform: scale(1); opacity: 1; }
        }
        @keyframes typingDot2 {
            0%, 80%, 100% { transform: scale(0); opacity: 0.5; }
            40% { transform: scale(1); opacity: 1; }
        }
        @keyframes typingDot3 {
            0%, 80%, 100% { transform: scale(0); opacity: 0.5; }
            40% { transform: scale(1); opacity: 1; }
        }
        </style>
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
