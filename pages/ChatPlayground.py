import streamlit as st
import requests
import uuid
import json
import os
st.set_page_config(layout="wide") 


# Set up the Streamlit interface with enhanced styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        font-family: 'Poppins', sans-serif;
    }
    
    .main-container {
        background: rgba(20, 20, 40, 0.85);
        backdrop-filter: blur(15px);
        border-radius: 25px;
        padding: 2.5rem;
        margin: 1rem;
        box-shadow: 0 25px 50px rgba(0,0,0,0.3);
        border: 1px solid rgba(100,100,150,0.2);
        animation: goldenGlow 3s infinite; /* Thêm hiệu ứng động */
    }

    /* Keyframes cho hiệu ứng phát sáng */
    @keyframes goldenGlow {
        0% {
            border-color: rgba(255, 215, 0, 0.3); /* Viền vàng nhạt */
            box-shadow: 0 0 10px rgba(255, 215, 0, 0.3); /* Ánh sáng nhẹ */
        }
        50% {
            border-color: rgba(255, 215, 0, 0.8); /* Viền vàng đậm */
            box-shadow: 0 0 20px rgba(255, 215, 0, 0.8); /* Ánh sáng mạnh */
        }
        100% {
            border-color: rgba(255, 215, 0, 0.3); /* Quay lại vàng nhạt */
            box-shadow: 0 0 10px rgba(255, 215, 0, 0.3); /* Ánh sáng nhẹ */
        }
    }
    
    .main-title {
        font-size: 3.5em;
        font-weight: 700;
        background: linear-gradient(45deg, #ffd700, #ff6b35, #f7931e, #ffd700);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.2em;
        text-align: center;
        animation: gradientShift 3s ease-in-out infinite;
        text-shadow: 0 0 30px rgba(255,215,0,0.3);
    }
    
    @keyframes gradientShift {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .subtitle {
        font-size: 1.3em;
        color: #b8b8d1;
        text-align: center;
        margin-bottom: 1em;
        font-weight: 300;
        opacity: 0;
        animation: fadeInUp 1s ease-out 0.5s forwards;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .info-box {
        background: linear-gradient(135deg, rgba(255,215,0,0.1), rgba(255,107,53,0.1));
        border-radius: 25px;
        padding: 2.5em;
        margin-bottom: 2em;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
        border: 1px solid rgba(255,215,0,0.3);
        position: relative;
        overflow: hidden;
        opacity: 0;
        animation: slideInLeft 1s ease-out 1s forwards;
        color: #e8e8f0;
    }
    
    .info-box::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255,215,0,0.1), transparent);
        transform: rotate(45deg);
        animation: shimmer 4s infinite;
    }
    
    @keyframes shimmer {
        0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
        100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    .info-box ul {
        margin: 1em 0;
        padding-left: 1.5em;
    }
    
    .info-box li {
        margin-bottom: 0.5em;
        position: relative;
    }
    
    .info-box li::before {
        content: '✨';
        position: absolute;
        left: -1.5em;
        animation: sparkle 2s infinite;
    }
    
    @keyframes sparkle {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.7; transform: scale(1.2); }
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%) !important;
        border-radius: 0 25px 25px 0;
    }
    
    /* Chat input styling */
    .stChatInputContainer {
        border-radius: 25px !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.3) !important;
        border: 2px solid rgba(255,215,0,0.4) !important;
        background: rgba(20,20,40,0.9) !important;
    }
    
    /* Chat messages - Base styling */
    .stChatMessage {
        background: rgba(30,30,50,0.9) !important;
        border-radius: 20px !important;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2) !important;
        margin-bottom: 1rem !important;
        backdrop-filter: blur(15px) !important;
        position: relative !important;
        overflow: hidden !important;
        border: 2px solid transparent !important;
    }

    /* Apply user styling to all messages by default, then override for assistant */
    .stChatMessage {
        border: 2px solid rgba(255, 215, 0, 0.7) !important;
        animation: goldenUserGlow 2s infinite !important;
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.3), 0 5px 15px rgba(0,0,0,0.2) !important;
    }

    /* Animation for user messages - Bright gold */
    @keyframes goldenUserGlow {
        0% {
            border-color: rgba(255, 215, 0, 0.7);
            box-shadow: 0 0 20px rgba(255, 215, 0, 0.3), 0 5px 15px rgba(0,0,0,0.2);
        }
        50% {
            border-color: rgba(255, 193, 7, 1);
            box-shadow: 0 0 35px rgba(255, 215, 0, 0.8), 0 5px 15px rgba(0,0,0,0.2);
        }
        100% {
            border-color: rgba(255, 215, 0, 0.7);
            box-shadow: 0 0 20px rgba(255, 215, 0, 0.3), 0 5px 15px rgba(0,0,0,0.2);
        }
    }

    /* Animation for assistant messages - Deep orange-gold */
    @keyframes deepGoldenGlow {
        0% {
            border-color: rgba(255, 140, 0, 0.8);
            box-shadow: 0 0 25px rgba(255, 140, 0, 0.4), 0 5px 15px rgba(0,0,0,0.2);
        }
        50% {
            border-color: rgba(255, 69, 0, 1);
            box-shadow: 0 0 40px rgba(255, 140, 0, 0.9), 0 5px 15px rgba(0,0,0,0.2);
        }
        100% {
            border-color: rgba(255, 140, 0, 0.8);
            box-shadow: 0 0 25px rgba(255, 140, 0, 0.4), 0 5px 15px rgba(0,0,0,0.2);
        }
    }

    /* Override for assistant messages - Apply to every second message */
    .stChatMessage:nth-child(even) {
        border: 2px solid rgba(255, 140, 0, 0.8) !important;
        animation: deepGoldenGlow 3s infinite !important;
        box-shadow: 0 0 25px rgba(255, 140, 0, 0.4), 0 5px 15px rgba(0,0,0,0.2) !important;
    }

    /* Additional targeting for better compatibility */
    [data-testid*="assistant"] {
        border: 2px solid rgba(255, 140, 0, 0.8) !important;
        animation: deepGoldenGlow 3s infinite !important;
        box-shadow: 0 0 25px rgba(255, 140, 0, 0.4), 0 5px 15px rgba(0,0,0,0.2) !important;
    }

    /* Force assistant styling on chat message containers that contain assistant content */
    div:has([data-testid*="assistant"]) .stChatMessage,
    .stChatMessage:has([data-testid*="assistant"]) {
        border: 2px solid rgba(255, 140, 0, 0.8) !important;
        animation: deepGoldenGlow 3s infinite !important;
        box-shadow: 0 0 25px rgba(255, 140, 0, 0.4), 0 5px 15px rgba(0,0,0,0.2) !important;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(45deg, #ffd700, #ff6b35) !important;
        color: #1a1a2e !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 0.6rem 2.5rem !important;
        font-weight: 700 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 8px 20px rgba(255,215,0,0.3) !important;
        text-shadow: none !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 12px 30px rgba(255,215,0,0.5) !important;
        background: linear-gradient(45deg, #ff6b35, #ffd700) !important;
    }
    
    /* Hide the default trash button styling - using custom solar system now */
    div[data-testid="stButton"] button[aria-label*="Xóa"] {
        opacity: 0 !important;
        height: 0 !important;
        width: 0 !important;
        padding: 0 !important;
        margin: 0 !important;
        border: none !important;
        position: absolute !important;
        z-index: -1 !important;
    }
    
    /* Selectbox and sliders */
    .stSelectbox > div > div {
        border-radius: 15px !important;
        border: 2px solid rgba(255,215,0,0.4) !important;
        background: rgba(30,30,50,0.9) !important;
        color: #e8e8f0 !important;
        animation: glowEffect 2s infinite; /* Thêm hiệu ứng động */
    }

    @keyframes glowEffect {
        0% {
            box-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
        }
        50% {
            box-shadow: 0 0 20px rgba(255, 215, 0, 0.8);
        }
        100% {
            box-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
        }
    }
    
    .stSlider > div > div {
        background: linear-gradient(90deg, #1a1a2e, #2d2d3a) !important;
    }
    
    .stSlider .stSlider-thumb {
        background: linear-gradient(45deg, #ffd700, #ff6b35) !important;
        border: 2px solid #ffd700 !important;
        box-shadow: 0 0 15px rgba(255,215,0,0.5) !important;
    }
    
    .stSlider .stSlider-track {
        background: linear-gradient(90deg, #ffd700, #ff6b35) !important;
        box-shadow: 0 0 10px rgba(255,215,0,0.3) !important;
    }
    
    /* Metrics */
    .metric-container {
        background: linear-gradient(135deg, rgba(255,215,0,0.15), rgba(255,107,53,0.15));
        border-radius: 20px;
        padding: 1.5rem;
        margin: 0.8rem 0;
        border: 1px solid rgba(255,215,0,0.3);
        text-align: center;
        transition: transform 0.3s ease;
        backdrop-filter: blur(10px);
    }
    
    .metric-container:hover {
        transform: scale(1.08);
        box-shadow: 0 10px 25px rgba(255,215,0,0.2);
    }
    
    /* Logo animation */
    .logo-container {
        text-align: center;
        margin-top: 2rem;
        position: relative;
        perspective: 1000px;
    }
    
    .logo-container::before {
        content: '';
        position: absolute;
        top: -20px;
        left: 50%;
        transform: translateX(-50%);
        width: 140px;
        height: 140px;
        background: linear-gradient(45deg, #ffd700, #ff6b35, #ffd700);
        border-radius: 50%;
        opacity: 0.2;
        animation: logoGlow 3s ease-in-out infinite;
        z-index: -1;
        blur: 15px;
    }
    
    @keyframes logoGlow {
        0%, 100% { 
            transform: translateX(-50%) scale(0.8);
            opacity: 0.2;
        }
        50% { 
            transform: translateX(-50%) scale(1.2);
            opacity: 0.4;
        }
    }
    
    .logo-container img {
        border-radius: 25px;
        box-shadow: 
            0 10px 30px rgba(0,0,0,0.4),
            0 0 20px rgba(255,215,0,0.3),
            inset 0 1px 0 rgba(255,255,255,0.1);
        transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        filter: brightness(1.1) contrast(1.1) saturate(1.2);
        position: relative;
        z-index: 2;
        animation: logoFloat 4s ease-in-out infinite;
    }
    
    @keyframes logoFloat {
        0%, 100% { 
            transform: translateY(0px) rotateY(0deg);
        }
        25% { 
            transform: translateY(-8px) rotateY(-5deg);
        }
        50% { 
            transform: translateY(-12px) rotateY(0deg);
        }
        75% { 
            transform: translateY(-8px) rotateY(5deg);
        }
    }
    
    .logo-container img:hover {
        transform: scale(1.2) rotateY(15deg) rotateX(5deg);
        box-shadow: 
            0 20px 50px rgba(0,0,0,0.5),
            0 0 40px rgba(255,215,0,0.6),
            0 0 80px rgba(255,107,53,0.3),
            inset 0 1px 0 rgba(255,255,255,0.2);
        filter: brightness(1.3) contrast(1.2) saturate(1.4);
        animation-play-state: paused;
    }
    
    .logo-wrapper {
        position: relative;
        display: inline-block;
        padding: 20px;
    }
    
    .logo-wrapper::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, transparent, rgba(255,215,0,0.1), transparent);
        border-radius: 30px;
        animation: logoShimmer 2s linear infinite;
        pointer-events: none;
    }
    
    @keyframes logoShimmer {
        0% { transform: translateX(-100%) skewX(-15deg); }
        100% { transform: translateX(100%) skewX(-15deg); }
    }
    
    /* Loading animation */
    .loading-dots {
        display: inline-block;
        position: relative;
        width: 80px;
        height: 80px;
    }
    
    .loading-dots div {
        position: absolute;
        top: 33px;
        width: 15px;
        height: 15px;
        border-radius: 50%;
        background: linear-gradient(45deg, #ffd700, #ff6b35);
        animation-timing-function: cubic-bezier(0, 1, 1, 0);
        box-shadow: 0 0 10px rgba(255,215,0,0.5);
    }
    
    .loading-dots div:nth-child(1) {
        left: 8px;
        animation: dots1 0.6s infinite;
    }
    
    .loading-dots div:nth-child(2) {
        left: 8px;
        animation: dots2 0.6s infinite;
    }
    
    .loading-dots div:nth-child(3) {
        left: 32px;
        animation: dots2 0.6s infinite;
    }
    
    .loading-dots div:nth-child(4) {
        left: 56px;
        animation: dots3 0.6s infinite;
    }
    
    @keyframes dots1 {
        0% { transform: scale(0); }
        100% { transform: scale(1); }
    }
    
    @keyframes dots3 {
        0% { transform: scale(1); }
        100% { transform: scale(0); }
    }
    
    @keyframes dots2 {
        0% { transform: translate(0, 0); }
        100% { transform: translate(24px, 0); }
    }
    
    /* Floating particles */
    .particles {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: -1;
    }
    
    .particle {
        position: absolute;
        width: 6px;
        height: 6px;
        background: rgba(255,215,0,0.4);
        border-radius: 50%;
        animation: float 8s infinite ease-in-out;
        box-shadow: 0 0 10px rgba(255,215,0,0.3);
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0) rotate(0deg); opacity: 1; }
        50% { transform: translateY(-120px) rotate(180deg); opacity: 0.3; }
    }

    .highlight-box {
        background: rgba(255,215,0,0.1);
        border-radius: 20px;
        padding: 1.5rem;
        margin: 1rem 0;
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255,215,0,0.3);
        transition: all 0.3s ease; /* Thêm hiệu ứng chuyển động */
    }

    .highlight-box:hover {
        background: rgba(255,215,0,0.3); /* Nền vàng nổi bật hơn */
        border: 1px solid #ffd700; /* Viền vàng đậm */
        box-shadow: 0 0 15px rgba(255,215,0,0.5); /* Hiệu ứng ánh sáng */
        transform: scale(1.05); /* Phóng to nhẹ khi hover */
    }

    .highlight-box div {
        color: #e8e8f0;
        font-weight: 600;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }
    </style>
    
    <div class="particles">
        <div class="particle" style="left: 10%; animation-delay: 0s;"></div>
        <div class="particle" style="left: 20%; animation-delay: 1s;"></div>
        <div class="particle" style="left: 30%; animation-delay: 2s;"></div>
        <div class="particle" style="left: 40%; animation-delay: 3s;"></div>
        <div class="particle" style="left: 50%; animation-delay: 4s;"></div>
        <div class="particle" style="left: 60%; animation-delay: 5s;"></div>
        <div class="particle" style="left: 70%; animation-delay: 0.5s;"></div>
        <div class="particle" style="left: 80%; animation-delay: 1.5s;"></div>
        <div class="particle" style="left: 90%; animation-delay: 2.5s;"></div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="main-container">
        <div class="main-title">🤖 Chatbot Playground</div>
        <div class="subtitle">✨ Trải nghiệm trò chuyện với AI một cách đơn giản và thú vị ✨</div>
        <div class="info-box">
            <b>🎉 Chào mừng bạn đến với Chatbot Playground!</b><br><br>
            Đây là nơi bạn có thể thử nghiệm và trò chuyện cùng các mô hình AI để khám phá cách chúng phản hồi trong nhiều tình huống khác nhau.<br><br>
            <ul>
                <li>🎯 Chọn mô hình ở thanh bên trái</li>
                <li>🚀 Bắt đầu cuộc trò chuyện với AI</li>
                <li>💡 Khám phá những phản hồi sáng tạo và bất ngờ</li>
            </ul>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)



st.session_state.flask_api_url = "http://localhost:5001"  # Set your Flask API URL here

# Generate a random session ID
session_id = str(uuid.uuid4())

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Function to get avatar path based on selected model
def get_avatar_path():
    if hasattr(st.session_state, 'selected_model'):
        # For GPT models, use openai.png
        if st.session_state.selected_model in ["gpt-4o-mini", "gpt-4o", "gpt-4", "gpt-3.5-turbo"]:
            return os.path.join(os.path.dirname(__file__), "..", "logo", "openai.png")
        else:
            # For Together AI models, get logo from model_info.json
            try:
                model_info_path = os.path.join(os.path.dirname(__file__), "model_info.json")
                with open(model_info_path, "r", encoding="utf-8") as f:
                    model_info = json.load(f)
                
                for model in model_info:
                    if model["id"] == st.session_state.selected_model:
                        logo_filename = model["logo_url"]
                        return os.path.join(os.path.dirname(__file__), "..", "logo", logo_filename)
                        
                # Fallback to meta.png if model not found
                return os.path.join(os.path.dirname(__file__), "..", "logo", "meta.png")
            except:
                # Fallback to meta.png if any error occurs
                return os.path.join(os.path.dirname(__file__), "..", "logo", "meta.png")
    
    # Default fallback
    return os.path.join(os.path.dirname(__file__), "..", "logo", "meta.png")


# Sidebar settings for model, temperature, and top_p
with st.sidebar:
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 2rem;">
            <h2 style="color: #ffd700; text-shadow: 2px 2px 4px rgba(0,0,0,0.5); font-weight: 600;">🎛️ Cấu hình Model</h2>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # Model selection with tabs for different providers
    model_provider = st.radio(
        "Chọn nhà cung cấp:",
        ["OpenAI (GPT)", "Together AI (Custom)"],
        help="OpenAI cho GPT models, Together AI cho các model khác"
    )
    
    if model_provider == "OpenAI (GPT)":
        # TODO 1: Create a selectbox with options "gpt-4o" and "gpt-4"
        st.session_state.selected_model = st.selectbox(
            "Chọn mô hình GPT:",
            ["gpt-4o-mini", "gpt-4o", "gpt-4", "gpt-3.5-turbo"],
            index=0
        )
    else:
        # Together AI model selection with enhanced UI
        st.markdown("**🚀 Chọn mô hình Together AI:**")
        
        # Đọc thông tin model từ file model_info.json
        model_info_path = os.path.join(os.path.dirname(__file__), "model_info.json")
        with open(model_info_path, "r", encoding="utf-8") as f:
            model_info = json.load(f)
        # Tạo model_options từ model_info
        model_options = {item["name"]: item["id"] for item in model_info}
        model_prices = {item["id"]: item["price"] for item in model_info}
        model_descriptions = {item["id"]: item["description"] for item in model_info}
        
        selected_display_name = st.selectbox(
            "Mô hình:",
            options=list(model_options.keys()),
            index=0,
            help="Các mô hình được sắp xếp theo giá từ rẻ đến thấp"
        )
        
        st.session_state.selected_model = model_options[selected_display_name]

    # Display selected model with provider info
    provider_emoji = "🤖" if model_provider == "OpenAI (GPT)" else "🚀"
    try:
        price = model_prices[st.session_state.selected_model]
    except:
        price = ""
    provider_name = "OpenAI" if model_provider == "OpenAI (GPT)" else "Together AI"

    if provider_name == "OpenAI":
        st.markdown(
            f"""
            <div class="highlight-box">
                <div>
                    <div>✨ <b>Đã chọn:</b> {provider_emoji} {st.session_state.selected_model}</div>
                    <div style="margin-top: 0.5rem;">🏢 <b>Nhà cung cấp:</b> {provider_name}</div>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )
    else:
        st.markdown(
            f"""
            <div class="highlight-box">
                <div>
                    <div>✨ <b>Đã chọn:</b> {provider_emoji} {selected_display_name}</div>
                    <div style="margin-top: 0.5rem;">💰 <b>Giá:</b> {price}</div>
                    <div style="margin-top: 0.5rem;">🏢 <b>Nhà cung cấp:</b> {provider_name}</div>
                </div>
            </div>
        """, 
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="text-align: center; margin: 2rem 0;">
            <h3 style="color: #ffd700; text-shadow: 2px 2px 4px rgba(0,0,0,0.5); font-weight: 600;">⚙️ Tham số Model</h3>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # TODO 2: Create a slider ranging from 0.0 to 1.0 with a step of 0.1
    st.session_state.temperature = st.slider(
        "🌡️ Temperature:",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1,
        help="Điều khiển tính sáng tạo: thấp = tập trung, cao = sáng tạo"
    )
    st.caption(f"🌡️ Temperature hiện tại: **{st.session_state.temperature}** {'🔥' if st.session_state.temperature > 0.7 else '❄️' if st.session_state.temperature < 0.3 else '🌤️'}")

    # TODO 3: Create a slider ranging from 0.0 to 1.0 with a step of 0.1
    st.session_state.top_p = st.slider(
        "🎯 Top P:",
        min_value=0.0,
        max_value=1.0,
        value=0.9,
        step=0.1,
        help="Điều khiển đa dạng từ vựng: thấp = ít từ, cao = nhiều từ"
    )
    st.caption(f"🎯 Top P hiện tại: **{st.session_state.top_p}** {'🎊' if st.session_state.top_p > 0.8 else '🎯' if st.session_state.top_p < 0.5 else '⚖️'}")
    
    # Simple clear button in sidebar that clears immediately
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🗑️ Xóa lịch sử chat", key="clear_chat", type="secondary", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

    st.markdown("---")
    
    # User Avatar Upload Section
    st.markdown(
        """
        <div style="text-align: center; margin: 1rem 0;">
            <h3 style="color: #ffd700; text-shadow: 2px 2px 4px rgba(0,0,0,0.5); font-weight: 600;">👤 Avatar Cá Nhân</h3>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # Avatar upload
    uploaded_avatar = st.file_uploader(
        "📸 Tải lên avatar của bạn:",
        type=['png', 'jpg', 'jpeg', 'gif'],
        help="Chọn ảnh để làm avatar cá nhân (PNG, JPG, JPEG, GIF)",
        key="user_avatar_upload"
    )
    
    # Store uploaded avatar in session state
    if uploaded_avatar is not None:
        # Save the uploaded file to session state
        st.session_state.user_avatar = uploaded_avatar
        
        # Display preview
        st.markdown("**🔍 Xem trước avatar:**")
        st.image(uploaded_avatar, width=80)
        
        st.success("✅ Avatar đã được tải lên thành công!")
    else:
        # Reset avatar if no file uploaded
        if "user_avatar" in st.session_state:
            del st.session_state.user_avatar
    
    # Option to reset avatar
    if "user_avatar" in st.session_state:
        if st.button("🔄 Đặt lại avatar mặc định", key="reset_avatar", type="secondary", use_container_width=True):
            del st.session_state.user_avatar
            st.rerun()

    st.markdown("---")
    
    # Solar System Animation at the bottom - optimized spacing
    st.markdown(
        """
        <div style="display: flex; justify-content: center; margin: 1rem 0 0.5rem 0;">
            <div class="solar-system">
                <div class="sun">🌟</div>
                <div class="orbit">
                    <div class="planet robot1">🤖</div>
                </div>
                <div class="orbit orbit2">
                    <div class="planet robot2">🚀</div>
                </div>
                <div class="orbit orbit3">
                    <div class="planet robot3">⭐</div>
                </div>
                <div class="orbit orbit4">
                    <div class="planet robot4">🛸</div>
                </div>
            </div>
        </div>
        
        <style>
        .solar-system {
            position: relative;
            width: 260px;
            height: 260px;
            margin: 0 auto;
            overflow: hidden;
        }
        
        .sun {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 75px;
            height: 75px;
            background: linear-gradient(45deg, #ffd700, #ffed4e, #ff6b35);
            border-radius: 50%;
            font-size: 2.2rem;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 2px solid rgba(255, 215, 0, 0.8);
            box-shadow: 0 0 35px rgba(255, 215, 0, 0.6);
            animation: sunGlow 2s infinite ease-in-out;
            transition: all 0.3s ease;
            z-index: 10;
        }
        
        .sun:hover {
            transform: translate(-50%, -50%) scale(1.15) rotate(15deg);
            box-shadow: 0 0 45px rgba(255, 215, 0, 0.8);
        }
        
        .orbit {
            position: absolute;
            top: 50%;
            left: 50%;
            border: 1px solid rgba(255, 215, 0, 0.15);
            border-radius: 50%;
            transform: translate(-50%, -50%);
        }
        
        .orbit {
            width: 130px;
            height: 130px;
            animation: rotate 4s linear infinite;
        }
        
        .orbit2 {
            width: 160px;
            height: 160px;
            animation: rotate 6s linear infinite reverse;
        }
        
        .orbit3 {
            width: 190px;
            height: 190px;
            animation: rotate 8s linear infinite;
        }
        
        .orbit4 {
            width: 220px;
            height: 220px;
            animation: rotate 10s linear infinite reverse;
        }
        
        .planet {
            position: absolute;
            width: 26px;
            height: 26px;
            border-radius: 50%;
            font-size: 1.2rem;
            display: flex;
            align-items: center;
            justify-content: center;
            top: -13px;
            left: 50%;
            transform: translateX(-50%);
            animation: counterRotate 4s linear infinite;
        }
        
        .robot2 {
            animation: counterRotate 6s linear infinite reverse;
        }
        
        .robot3 {
            animation: counterRotate 8s linear infinite;
        }
        
        .robot4 {
            animation: counterRotate 10s linear infinite reverse;
        }
        
        @keyframes rotate {
            from { transform: translate(-50%, -50%) rotate(0deg); }
            to { transform: translate(-50%, -50%) rotate(360deg); }
        }
        
        @keyframes counterRotate {
            from { transform: translateX(-50%) rotate(0deg); }
            to { transform: translateX(-50%) rotate(-360deg); }
        }
        
        @keyframes sunGlow {
            0% { box-shadow: 0 0 35px rgba(255, 215, 0, 0.6); }
            50% { box-shadow: 0 0 45px rgba(255, 215, 0, 0.8), 0 0 60px rgba(255, 215, 0, 0.3); }
            100% { box-shadow: 0 0 35px rgba(255, 215, 0, 0.6); }
        }
        
        /* Optimized twinkling stars */
        .solar-system::before {
            content: '✨';
            position: absolute;
            top: 15px;
            left: 15px;
            font-size: 0.9rem;
            animation: twinkle 1.5s infinite;
        }
        
        .solar-system::after {
            content: '💫';
            position: absolute;
            bottom: 20px;
            right: 20px;
            font-size: 1rem;
            animation: twinkle 2s infinite 0.5s;
        }
        
        /* Compact background stars */
        .solar-system {
            background-image: 
                radial-gradient(1.5px 1.5px at 45px 70px, #ffd700, transparent),
                radial-gradient(1.5px 1.5px at 180px 50px, #ffed4e, transparent),
                radial-gradient(1px 1px at 70px 180px, #ffd700, transparent),
                radial-gradient(1px 1px at 200px 160px, #ffed4e, transparent),
                radial-gradient(1.5px 1.5px at 140px 25px, #ffd700, transparent),
                radial-gradient(1px 1px at 35px 130px, #ffed4e, transparent);
            animation: starTwinkle 3s infinite ease-in-out;
        }
        
        @keyframes twinkle {
            0%, 100% { opacity: 0.4; transform: scale(0.9); }
            50% { opacity: 1; transform: scale(1.2); }
        }
        
        @keyframes starTwinkle {
            0%, 100% { opacity: 0.8; }
            50% { opacity: 1; }
        }
        </style>
        """,
        unsafe_allow_html=True
    )


# Display model description if Together AI model is selected
if hasattr(st.session_state, 'selected_model') and st.session_state.selected_model not in ["gpt-4o-mini", "gpt-4o", "gpt-4", "gpt-3.5-turbo"]:
    model_info_path = os.path.join(os.path.dirname(__file__), "model_info.json")
    with open(model_info_path, "r", encoding="utf-8") as f:
        model_info = json.load(f)
    
    model_descriptions = {item["id"]: item["description"] for item in model_info}
    
    if st.session_state.selected_model in model_descriptions:
        description_text = model_descriptions[st.session_state.selected_model]
        
        st.markdown(
            f"""
            <div class="model-description-box">
                <div class="shimmer-overlay"></div>
                <div class="glow-border"></div>
                <div class="description-content">
                    <div class="description-icon">🚀</div>
                    <div class="description-text">
                        <strong>Model Description:</strong><br>
                        {description_text}
                    </div>
                </div>
            </div>
            
            <style>
            .model-description-box {{
                position: relative;
                background: linear-gradient(135deg, 
                    rgba(255,215,0,0.15) 0%, 
                    rgba(255,107,53,0.15) 35%, 
                    rgba(138,43,226,0.1) 70%,
                    rgba(0,191,255,0.1) 100%);
                border-radius: 25px;
                padding: 2rem;
                margin: 1.5rem 0;
                overflow: hidden;
                backdrop-filter: blur(20px);
                border: 2px solid transparent;
                animation: borderGlow 3s ease-in-out infinite;
                transition: all 0.3s ease;
                box-shadow: 
                    0 15px 35px rgba(0,0,0,0.3),
                    0 5px 15px rgba(255,215,0,0.2),
                    inset 0 1px 0 rgba(255,255,255,0.1);
            }}
            
            .model-description-box:hover {{
                transform: translateY(-5px) scale(1.02);
                box-shadow: 
                    0 25px 50px rgba(0,0,0,0.4),
                    0 10px 30px rgba(255,215,0,0.4),
                    0 0 40px rgba(255,107,53,0.3);
            }}
            
            @keyframes borderGlow {{
                0% {{
                    border-color: rgba(255, 215, 0, 0.6);
                    box-shadow: 
                        0 15px 35px rgba(0,0,0,0.3),
                        0 5px 15px rgba(255,215,0,0.2),
                        0 0 20px rgba(255,215,0,0.3);
                }}
                33% {{
                    border-color: rgba(255, 107, 53, 0.8);
                    box-shadow: 
                        0 20px 40px rgba(0,0,0,0.4),
                        0 8px 25px rgba(255,107,53,0.4),
                        0 0 30px rgba(255,107,53,0.5);
                }}
                66% {{
                    border-color: rgba(138, 43, 226, 0.7);
                    box-shadow: 
                        0 18px 38px rgba(0,0,0,0.35),
                        0 6px 20px rgba(138,43,226,0.3),
                        0 0 25px rgba(138,43,226,0.4);
                }}
                100% {{
                    border-color: rgba(255, 215, 0, 0.6);
                    box-shadow: 
                        0 15px 35px rgba(0,0,0,0.3),
                        0 5px 15px rgba(255,215,0,0.2),
                        0 0 20px rgba(255,215,0,0.3);
                }}
            }}
            
            .shimmer-overlay {{
                position: absolute;
                top: -50%;
                left: -50%;
                width: 200%;
                height: 200%;
                background: linear-gradient(
                    45deg, 
                    transparent, 
                    rgba(255,255,255,0.1), 
                    transparent
                );
                transform: rotate(45deg);
                animation: shimmerMove 4s ease-in-out infinite;
                pointer-events: none;
            }}
            
            @keyframes shimmerMove {{
                0% {{
                    transform: translateX(-100%) translateY(-100%) rotate(45deg);
                    opacity: 0;
                }}
                50% {{
                    opacity: 1;
                }}
                100% {{
                    transform: translateX(100%) translateY(100%) rotate(45deg);
                    opacity: 0;
                }}
            }}
            
            .glow-border {{
                position: absolute;
                top: -2px;
                left: -2px;
                right: -2px;
                bottom: -2px;
                background: linear-gradient(
                    45deg,
                    #ffd700,
                    #ff6b35,
                    #8a2be2,
                    #00bfff,
                    #ffd700
                );
                border-radius: 25px;
                z-index: -1;
                animation: rotateBorder 6s linear infinite;
                opacity: 0.7;
            }}
            
            @keyframes rotateBorder {{
                0% {{
                    transform: rotate(0deg);
                }}
                100% {{
                    transform: rotate(360deg);
                }}
            }}
            
            .description-content {{
                position: relative;
                z-index: 2;
                display: flex;
                align-items: flex-start;
                gap: 1rem;
            }}
            
            .description-icon {{
                font-size: 2.5rem;
                animation: iconFloat 3s ease-in-out infinite;
                filter: drop-shadow(0 0 10px rgba(255,215,0,0.5));
            }}
            
            @keyframes iconFloat {{
                0%, 100% {{
                    transform: translateY(0px) rotate(0deg);
                }}
                25% {{
                    transform: translateY(-8px) rotate(-5deg);
                }}
                50% {{
                    transform: translateY(-12px) rotate(0deg);
                }}
                75% {{
                    transform: translateY(-8px) rotate(5deg);
                }}
            }}
            
            .description-text {{
                flex: 1;
                color: #e8e8f0;
                font-size: 1.1rem;
                line-height: 1.7;
                text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
                animation: textGlow 4s ease-in-out infinite;
            }}
            
            .description-text strong {{
                color: #ffd700;
                font-weight: 700;
                font-size: 1.2rem;
                display: inline-block;
                margin-bottom: 0.5rem;
                text-shadow: 0 0 10px rgba(255,215,0,0.3);
            }}
            
            @keyframes textGlow {{
                0%, 100% {{
                    text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
                }}
                50% {{
                    text-shadow: 
                        1px 1px 2px rgba(0,0,0,0.5),
                        0 0 15px rgba(255,215,0,0.2);
                }}
            }}
            
            /* Floating particles effect */
            .model-description-box::before {{
                content: '✨';
                position: absolute;
                top: 20px;
                right: 25px;
                font-size: 1.2rem;
                animation: sparkle 2s ease-in-out infinite;
                z-index: 3;
            }}
            
            .model-description-box::after {{
                content: '💫';
                position: absolute;
                bottom: 20px;
                left: 25px;
                font-size: 1rem;
                animation: sparkle 2.5s ease-in-out infinite 1s;
                z-index: 3;
            }}
            
            @keyframes sparkle {{
                0%, 100% {{
                    opacity: 0.6;
                    transform: scale(0.8) rotate(0deg);
                }}
                50% {{
                    opacity: 1;
                    transform: scale(1.2) rotate(180deg);
                }}
            }}
            </style>
            """,
            unsafe_allow_html=True
        )


else:
    st.markdown(
            f"""
            <div class="gpt-description-box">
                <div class="gpt-shimmer-overlay"></div>
                <div class="gpt-glow-border"></div>
                <div class="gpt-description-content">
                    <div class="gpt-description-icon">🤖</div>
                    <div class="gpt-description-text">
                        <strong>OpenAI GPT Description:</strong><br>
                        We are governed by a nonprofit and our unique capped-profit model drives our commitment to safety. This means that as AI becomes more powerful, we can redistribute profits from our work to maximize the social and economic benefits of AI technology.
                    </div>
                </div>
            </div>
            
            <style>
            .gpt-description-box {{
                position: relative;
                background: linear-gradient(135deg, 
                    rgba(0,191,255,0.15) 0%, 
                    rgba(30,144,255,0.15) 35%, 
                    rgba(138,43,226,0.1) 70%,
                    rgba(0,255,127,0.1) 100%);
                border-radius: 25px;
                padding: 2rem;
                margin: 1.5rem 0;
                overflow: hidden;
                backdrop-filter: blur(20px);
                border: 2px solid transparent;
                animation: gptBorderGlow 3s ease-in-out infinite;
                transition: all 0.3s ease;
                box-shadow: 
                    0 15px 35px rgba(0,0,0,0.3),
                    0 5px 15px rgba(0,191,255,0.2),
                    inset 0 1px 0 rgba(255,255,255,0.1);
            }}
            
            .gpt-description-box:hover {{
                transform: translateY(-5px) scale(1.02);
                box-shadow: 
                    0 25px 50px rgba(0,0,0,0.4),
                    0 10px 30px rgba(0,191,255,0.4),
                    0 0 40px rgba(30,144,255,0.3);
            }}
            
            @keyframes gptBorderGlow {{
                0% {{
                    border-color: rgba(0, 191, 255, 0.6);
                    box-shadow: 
                        0 15px 35px rgba(0,0,0,0.3),
                        0 5px 15px rgba(0,191,255,0.2),
                        0 0 20px rgba(0,191,255,0.3);
                }}
                33% {{
                    border-color: rgba(30, 144, 255, 0.8);
                    box-shadow: 
                        0 20px 40px rgba(0,0,0,0.4),
                        0 8px 25px rgba(30,144,255,0.4),
                        0 0 30px rgba(30,144,255,0.5);
                }}
                66% {{
                    border-color: rgba(138, 43, 226, 0.7);
                    box-shadow: 
                        0 18px 38px rgba(0,0,0,0.35),
                        0 6px 20px rgba(138,43,226,0.3),
                        0 0 25px rgba(138,43,226,0.4);
                }}
                100% {{
                    border-color: rgba(0, 191, 255, 0.6);
                    box-shadow: 
                        0 15px 35px rgba(0,0,0,0.3),
                        0 5px 15px rgba(0,191,255,0.2),
                        0 0 20px rgba(0,191,255,0.3);
                }}
            }}
            
            .gpt-shimmer-overlay {{
                position: absolute;
                top: -50%;
                left: -50%;
                width: 200%;
                height: 200%;
                background: linear-gradient(
                    45deg, 
                    transparent, 
                    rgba(0,191,255,0.1), 
                    transparent
                );
                transform: rotate(45deg);
                animation: gptShimmerMove 4s ease-in-out infinite;
                pointer-events: none;
            }}
            
            @keyframes gptShimmerMove {{
                0% {{
                    transform: translateX(-100%) translateY(-100%) rotate(45deg);
                    opacity: 0;
                }}
                50% {{
                    opacity: 1;
                }}
                100% {{
                    transform: translateX(100%) translateY(100%) rotate(45deg);
                    opacity: 0;
                }}
            }}
            
            .gpt-glow-border {{
                position: absolute;
                top: -2px;
                left: -2px;
                right: -2px;
                bottom: -2px;
                background: linear-gradient(
                    45deg,
                    #00bfff,
                    #1e90ff,
                    #8a2be2,
                    #00ff7f,
                    #00bfff
                );
                border-radius: 25px;
                z-index: -1;
                animation: gptRotateBorder 6s linear infinite;
                opacity: 0.7;
            }}
            
            @keyframes gptRotateBorder {{
                0% {{
                    transform: rotate(0deg);
                }}
                100% {{
                    transform: rotate(360deg);
                }}
            }}
            
            .gpt-description-content {{
                position: relative;
                z-index: 2;
                display: flex;
                align-items: flex-start;
                gap: 1rem;
            }}
            
            .gpt-description-icon {{
                font-size: 2.5rem;
                animation: gptIconFloat 3s ease-in-out infinite;
                filter: drop-shadow(0 0 10px rgba(0,191,255,0.5));
            }}
            
            @keyframes gptIconFloat {{
                0%, 100% {{
                    transform: translateY(0px) rotate(0deg);
                }}
                25% {{
                    transform: translateY(-8px) rotate(-5deg);
                }}
                50% {{
                    transform: translateY(-12px) rotate(0deg);
                }}
                75% {{
                    transform: translateY(-8px) rotate(5deg);
                }}
            }}
            
            .gpt-description-text {{
                flex: 1;
                color: #e8e8f0;
                font-size: 1.1rem;
                line-height: 1.7;
                text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
                animation: gptTextGlow 4s ease-in-out infinite;
            }}
            
            .gpt-description-text strong {{
                color: #00bfff;
                font-weight: 700;
                font-size: 1.2rem;
                display: inline-block;
                margin-bottom: 0.5rem;
                text-shadow: 0 0 10px rgba(0,191,255,0.3);
            }}
            
            @keyframes gptTextGlow {{
                0%, 100% {{
                    text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
                }}
                50% {{
                    text-shadow: 
                        1px 1px 2px rgba(0,0,0,0.5),
                        0 0 15px rgba(0,191,255,0.2);
                }}
            }}
            
            /* Floating particles effect */
            .gpt-description-box::before {{
                content: '⚡';
                position: absolute;
                top: 20px;
                right: 25px;
                font-size: 1.2rem;
                animation: gptSparkle 2s ease-in-out infinite;
                z-index: 3;
            }}
            
            .gpt-description-box::after {{
                content: '💎';
                position: absolute;
                bottom: 20px;
                left: 25px;
                font-size: 1rem;
                animation: gptSparkle 2.5s ease-in-out infinite 1s;
                z-index: 3;
            }}
            
            @keyframes gptSparkle {{
                0%, 100% {{
                    opacity: 0.6;
                    transform: scale(0.8) rotate(0deg);
                }}
                50% {{
                    opacity: 1;
                    transform: scale(1.2) rotate(180deg);
                }}
            }}
            </style>
            """,
            unsafe_allow_html=True
        )





# Display the chat history using chat UI
for message in st.session_state.chat_history:
    if message["role"] == "assistant":
        # Use appropriate avatar based on selected model
        avatar_path = get_avatar_path()
        with st.chat_message(message["role"], avatar=avatar_path):
            st.markdown(message["content"])
    else:
        # User messages with custom avatar if uploaded
        if "user_avatar" in st.session_state:
            with st.chat_message(message["role"], avatar=st.session_state.user_avatar):
                st.markdown(message["content"])
        else:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input(key="chat", placeholder="💬 Nhập tin nhắn của bạn... ✨"):
    # Add user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    # Display user message in chat message container with custom avatar if available
    if "user_avatar" in st.session_state:
        with st.chat_message("user", avatar=st.session_state.user_avatar):
            st.markdown(prompt)
    else:
        with st.chat_message("user"):
            st.markdown(prompt)

    # Prepare the payload for the request
    payload = {
        "message": {"content": prompt},
        "context": st.session_state.chat_history,
        "sessionId": session_id,
        "model": st.session_state.selected_model,
        "temperature": st.session_state.temperature,
        "top_p": st.session_state.top_p,
        "stream": True  # Enable streaming
    }

    # Stream the response from the Flask API
    avatar_path = get_avatar_path()
    with st.chat_message("assistant", avatar=avatar_path):
        streamed_content = ""  # Initialize an empty string to concatenate chunks
        response = requests.post(st.session_state.flask_api_url, json=payload, stream=True)

        # Create a placeholder to update the markdown
        response_placeholder = st.empty()
        
        # Add loading animation
        with response_placeholder.container():
            st.markdown(
                """
                <div style="text-align: center; padding: 2rem;">
                    <div class="loading-dots">
                        <div></div>
                        <div></div>
                        <div></div>
                        <div></div>
                    </div>
                    <p style="color: #ffd700; margin-top: 1rem; font-weight: 500;">🤖 AI đang suy nghĩ...</p>
                </div>
                """, 
                unsafe_allow_html=True
            )

        # Check if the request was successful
        if response.status_code == 200:
            
            # TODO 4
            # Loop through each chunk and add the content to the variable streamed_content
            # Don't forget to use markdown to print the result
            for line in response.iter_lines():
                if line:
                    line = line.decode('utf-8')
                    if line.startswith('data: '):
                        try:
                            data = line[6:]  # Remove 'data: ' prefix
                            json_data = json.loads(data)  # Parse JSON safely
                            
                            if 'content' in json_data:
                                content = json_data['content']
                                streamed_content += content
                                # Update the placeholder with the current streamed content
                                response_placeholder.markdown(streamed_content)
                            elif 'done' in json_data and json_data['done']:
                                break
                            elif 'error' in json_data:
                                st.error(f"Error: {json_data['error']}")
                                break
                        except json.JSONDecodeError:
                            continue

            # Once complete, add the full response to the chat history
            st.session_state.chat_history.append({"role": "assistant", "content": streamed_content})
        else:
            st.error(f"Error: {response.status_code}")

