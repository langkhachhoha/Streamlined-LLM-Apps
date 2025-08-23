import streamlit as st

st.set_page_config(
    page_title="🚀 LLMs Playground - AI4DEV",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Hide mainpage from sidebar navigation
st.markdown("""
    <style>
    .stSidebar [data-testid="stSidebarNav"] li:first-child {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

# Navigation sidebar
with st.sidebar:
    # Header
    st.markdown("""
        <div style="text-align: center; padding: 1.5rem 0;">
            <h1 style="color: #ffd700; text-shadow: 0 0 15px rgba(255, 215, 0, 0.7); font-size: 2.2rem; margin-bottom: 0.5rem;">
                🚀 AI4DEV
            </h1>
            <p style="color: #E8E8E8; font-size: 1rem; margin: 0; opacity: 0.9;">LLMs Playground</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Navigation menu
    st.markdown("""
        <div style="margin-bottom: 1rem;">
            <h3 style="color: #ffd700; font-size: 1.3rem; margin-bottom: 1rem; text-align: center;">
                📱 Navigation
            </h3>
        </div>
    """, unsafe_allow_html=True)
    
    # Available apps
    available_apps = {
        "🏠 Trang chủ": None,  # None means stay on current page
        "🎮 Chat Playground": "pages/ChatPlayground.py",
        
    }
    
    # Create navigation selectbox
    selected_app = st.selectbox(
        "Chọn ứng dụng:",
        options=list(available_apps.keys()),
        index=0,
        help="Chọn ứng dụng bạn muốn sử dụng"
    )
    
    # Navigation action
    if selected_app and available_apps[selected_app] is not None:
        # if st.button("🚀 Mở ứng dụng", use_container_width=True):
            st.switch_page(available_apps[selected_app])
    
    st.markdown("---")
    
    # App info section
    st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(20, 20, 40, 0.8), rgba(255, 215, 0, 0.1)); 
                    padding: 1.5rem; border-radius: 15px; border: 1px solid rgba(255, 215, 0, 0.3);">
            <h4 style="color: #ffd700; margin-bottom: 1rem; text-align: center;">💡 Thông tin</h4>
            <p style="color: #E8E8E8; margin: 0.5rem 0; font-size: 0.9rem;">
                <strong>Phiên bản:</strong> 1.0.0<br>
                <strong>Khóa học:</strong> AI4DEV<br>
                <strong>Assignment:</strong> 3 - LLMs Playground
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Help section
    st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(20, 20, 40, 0.8), rgba(255, 215, 0, 0.1)); 
                    padding: 1.5rem; border-radius: 15px; border: 1px solid rgba(255, 215, 0, 0.3);">
            <h4 style="color: #ffd700; margin-bottom: 1rem; text-align: center;">🎯 Hỗ trợ</h4>
            <div style="color: #E8E8E8; font-size: 0.9rem;">
                • <a href="https://docs.streamlit.io" style="color: #4ECDC4;">📚 Tài liệu</a><br>
                • <a href="mailto:support@ai4dev.com" style="color: #4ECDC4;">💬 Hỗ trợ</a><br>
                • <a href="https://github.com/ai4dev/issues" style="color: #4ECDC4;">🐛 Báo lỗi</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Custom CSS for beautiful homepage with black and gold theme
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        font-family: 'Poppins', sans-serif;
    }
    
    .hero-container {
        background: rgba(20, 20, 40, 0.95);
        backdrop-filter: blur(20px);
        border-radius: 30px;
        padding: 4rem 2rem;
        margin: 2rem 0;
        border: 2px solid #ffd700;
        text-align: center;
        animation: heroGlow 3s ease-in-out infinite, fadeInUp 2s ease-out;
        box-shadow: 0 0 50px rgba(255, 215, 0, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .hero-container::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255, 215, 0, 0.1), transparent);
        transform: rotate(45deg);
        animation: shimmerEffect 4s infinite linear;
    }
    
    @keyframes heroGlow {
        0%, 100% { 
            border-color: rgba(255, 215, 0, 0.6);
            box-shadow: 0 0 30px rgba(255, 215, 0, 0.3);
        }
        50% { 
            border-color: rgba(255, 215, 0, 1);
            box-shadow: 0 0 60px rgba(255, 215, 0, 0.6);
        }
    }
    
    @keyframes shimmerEffect {
        0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
        100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
    }
    
    .hero-title {
        font-size: 4.5rem;
        font-weight: 700;
        background: linear-gradient(45deg, #ffd700, #ff6b35, #f7931e, #ffd700);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradientFlow 3s ease-in-out infinite, textPulse 2s ease-in-out infinite;
        margin-bottom: 1rem;
        text-shadow: 0 0 30px rgba(255, 215, 0, 0.5);
        position: relative;
        z-index: 1;
    }
    
    @keyframes textPulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    .hero-subtitle {
        font-size: 1.6rem;
        color: #E8E8E8;
        margin-bottom: 2rem;
        font-weight: 300;
        opacity: 0;
        animation: slideInFromBottom 2s ease-out 0.5s forwards;
        position: relative;
        z-index: 1;
    }
    
    @keyframes slideInFromBottom {
        from {
            opacity: 0;
            transform: translateY(50px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .feature-card {
        background: linear-gradient(135deg, rgba(20, 20, 40, 0.9), rgba(255, 215, 0, 0.1));
        border-radius: 25px;
        padding: 2.5rem;
        margin: 1rem 0;
        border: 2px solid rgba(255, 215, 0, 0.3);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        color: #E8E8E8;
        position: relative;
        overflow: hidden;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        animation: cardFloat 6s ease-in-out infinite;
    }
    
    @keyframes cardFloat {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .feature-card:hover {
        transform: translateY(-15px) scale(1.02);
        box-shadow: 0 25px 50px rgba(255, 215, 0, 0.4);
        border-color: rgba(255, 215, 0, 0.8);
    }
    
    .feature-icon {
        font-size: 3.5rem;
        margin-bottom: 1.5rem;
        display: block;
        animation: iconBounce 2s ease-in-out infinite;
        filter: drop-shadow(0 0 10px rgba(255, 215, 0, 0.6));
    }
    
    @keyframes iconBounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-10px); }
        60% { transform: translateY(-5px); }
    }
    
    .feature-title {
        font-size: 1.6rem;
        font-weight: 600;
        margin-bottom: 1rem;
        color: #ffd700;
        text-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
    }
    
    .app-card {
        background: linear-gradient(135deg, rgba(20, 20, 40, 0.9), rgba(255, 215, 0, 0.15));
        border-radius: 25px;
        padding: 2.5rem;
        border: 2px solid rgba(255, 215, 0, 0.4);
        transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        color: #E8E8E8;
        text-decoration: none;
        display: block;
        position: relative;
        overflow: hidden;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
    }
    
    .app-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 30px 60px rgba(255, 215, 0, 0.4);
        border-color: rgba(255, 215, 0, 0.8);
    }
    
    .app-icon {
        font-size: 3rem;
        margin-bottom: 1.5rem;
        display: block;
        filter: drop-shadow(0 0 15px rgba(255, 215, 0, 0.7));
        position: relative;
        z-index: 1;
    }
    
    .app-title {
        font-size: 1.4rem;
        font-weight: 600;
        margin-bottom: 0.8rem;
        color: #ffd700;
        text-shadow: 0 0 15px rgba(255, 215, 0, 0.6);
        position: relative;
        z-index: 1;
    }
    
    .app-description {
        font-size: 1rem;
        opacity: 0.9;
        line-height: 1.6;
        position: relative;
        z-index: 1;
    }
    
    .stats-container {
        display: flex;
        justify-content: space-around;
        margin: 4rem 0;
        flex-wrap: wrap;
        gap: 2rem;
    }
    
    .stat-item {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(135deg, rgba(20, 20, 40, 0.8), rgba(255, 215, 0, 0.1));
        border-radius: 20px;
        min-width: 180px;
        border: 2px solid rgba(255, 215, 0, 0.3);
        transition: all 0.4s ease;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
    }
    
    .stat-item:hover {
        transform: translateY(-10px) scale(1.05);
        border-color: rgba(255, 215, 0, 0.8);
        box-shadow: 0 20px 40px rgba(255, 215, 0, 0.3);
    }
    
    .stat-number {
        font-size: 3rem;
        font-weight: 700;
        color: #ffd700;
        display: block;
        text-shadow: 0 0 20px rgba(255, 215, 0, 0.6);
    }
    
    .stat-label {
        font-size: 1rem;
        color: #E8E8E8;
        margin-top: 0.8rem;
        font-weight: 500;
    }
    
    .selectbox-container {
        background: linear-gradient(135deg, rgba(20, 20, 40, 0.9), rgba(255, 215, 0, 0.1));
        border-radius: 20px;
        padding: 2rem;
        border: 2px solid rgba(255, 215, 0, 0.3);
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }
    
    .selectbox-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #ffd700;
        margin-bottom: 1rem;
        text-align: center;
        text-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
    }
    
    .stButton > button {
        background: linear-gradient(45deg, #ffd700, #ff6b35);
        color: #000;
        border: none;
        border-radius: 30px;
        padding: 1rem 2rem;
        font-weight: 700;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 8px 25px rgba(255, 215, 0, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 15px 40px rgba(255, 215, 0, 0.6);
    }
    
    .stButton > button[kind="secondary"] {
        background: linear-gradient(135deg, rgba(20, 20, 40, 0.8), rgba(255, 215, 0, 0.1)) !important;
        color: #E8E8E8 !important;
        border: 1px solid rgba(255, 215, 0, 0.3) !important;
    }
    
    .stSidebar .stButton > button {
        width: 100%;
        margin-bottom: 0.5rem;
        border-radius: 15px;
        padding: 0.8rem 1rem;
        font-size: 0.95rem;
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
    
    @keyframes gradientFlow {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div class="hero-container">
        <div class="hero-title">🚀 LLMs Playground</div>
        <div class="hero-subtitle">Khám phá sức mạnh của AI với bộ công cụ tương tác thông minh</div>
        <p style="color: #E8E8E8; font-size: 1.2rem; margin-top: 1rem; position: relative; z-index: 1;">
            Chào mừng bạn đến với không gian thực nghiệm AI tiên tiến nhất! 
            Trải nghiệm các mô hình ngôn ngữ lớn và ứng dụng AI một cách dễ dàng và trực quan.
        </p>
    </div>
""", unsafe_allow_html=True)

# Stats Section
st.markdown("""
    <div class="stats-container">
        <div class="stat-item">
            <span class="stat-number">🎯</span>
            <div class="stat-label">Dễ sử dụng</div>
        </div>
        <div class="stat-item">
            <span class="stat-number">⚡</span>
            <div class="stat-label">Nhanh chóng</div>
        </div>
        <div class="stat-item">
            <span class="stat-number">🔧</span>
            <div class="stat-label">Đa chức năng</div>
        </div>
        <div class="stat-item">
            <span class="stat-number">🌟</span>
            <div class="stat-label">Chất lượng cao</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Features Section
st.markdown("## ✨ Tính năng nổi bật")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="feature-card">
            <span class="feature-icon">🤖</span>
            <div class="feature-title">AI Playground</div>
            <p>Tương tác trực tiếp với các mô hình AI mạnh mẽ. Thực nghiệm với các prompt khác nhau và khám phá khả năng của AI.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="feature-card">
            <span class="feature-icon">🎨</span>
            <div class="feature-title">Giao diện thân thiện</div>
            <p>Thiết kế hiện đại, trực quan và dễ sử dụng. Không cần kiến thức kỹ thuật để bắt đầu sử dụng.</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="feature-card">
            <span class="feature-icon">⚡</span>
            <div class="feature-title">Hiệu suất cao</div>
            <p>Xử lý nhanh chóng với khả năng tương tác thời gian thực. Tối ưu hóa cho trải nghiệm người dùng tốt nhất.</p>
        </div>
    """, unsafe_allow_html=True)

# Applications Section
st.markdown("## 🎯 Các ứng dụng có sẵn")

st.markdown("""
    <div class="selectbox-container">
        <div class="selectbox-title">📱 Khám phá các ứng dụng AI mạnh mẽ</div>
        <p style="text-align: center; color: #E8E8E8; margin-top: 1rem;">
            Sử dụng Navigation Bar bên trái để chuyển đổi giữa các ứng dụng
        </p>
    </div>
""", unsafe_allow_html=True)

# Display available apps as cards
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="app-card" style="margin-top: 1rem;">
            <span class="app-icon">🏠</span>
            <div class="app-title">Trang chủ</div>
            <div class="app-description">
                Trang chủ của LLMs Playground với tổng quan về tất cả các tính năng và ứng dụng có sẵn.
                Điểm khởi đầu để khám phá thế giới AI.
            </div>
            <div style="margin-top: 1rem; text-align: center;">
                <span style="color: #ffd700; font-weight: 600;">📍 Đang xem</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="app-card" style="margin-top: 1rem; opacity: 0.6;">
            <span class="app-icon">🚧</span>
            <div class="app-title">Sắp ra mắt</div>
            <div class="app-description">
                Chúng tôi đang phát triển thêm nhiều ứng dụng AI thú vị khác. 
                Hãy quay lại kiểm tra trong thời gian tới!
            </div>
            <div style="margin-top: 1rem; text-align: center;">
                <span style="color: #ff9500; font-weight: 600;">🔜 Coming Soon</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Quick access section
st.markdown("---")
st.markdown("### ⚡ Truy cập nhanh")

quick_col1, quick_col2, quick_col3 = st.columns(3)

with quick_col1:
    if st.button("� Trang chủ", type="primary", use_container_width=True):
        st.rerun()  # Refresh current page

with quick_col2:
    if st.button("📊 Dashboard", type="secondary", use_container_width=True, disabled=True):
        st.info("🚧 Sắp ra mắt!")

with quick_col3:
    if st.button("🔧 Cài đặt", type="secondary", use_container_width=True, disabled=True):
        st.info("🚧 Sắp ra mắt!")

# Quick Start Section
st.markdown("## 🚀 Hướng dẫn sử dụng")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
        **Cách bắt đầu:**
        1. 🎯 Sử dụng **Navigation Selectbox** bên trái để chọn ứng dụng
        2. � Hiện tại chỉ có **Trang chủ** - các app khác đang được phát triển
        3. � **Dashboard** và **Cài đặt** sẽ sớm được ra mắt
        4. � Theo dõi các cập nhật mới từ AI4DEV
        5. 💡 Đóng góp ý kiến để cải thiện ứng dụng
        
        **Tính năng sắp tới:**
        - 🤖 AI Chat với nhiều mô hình
        - � Dashboard phân tích usage
        - 🔧 Cài đặt tùy chỉnh interface
        - 🎨 Theme editor
        - 📈 Analytics và reporting
    """)

with col2:
    st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(20, 20, 40, 0.9), rgba(255, 215, 0, 0.1));
                    border-radius: 20px; padding: 2rem; text-align: center;
                    border: 2px solid rgba(255, 215, 0, 0.3); margin-top: 1rem;">
            <h4 style="color: #ffd700; margin-bottom: 1rem;">🎯 Đang phát triển</h4>
            <p style="color: #E8E8E8; margin-bottom: 1.5rem; font-size: 0.9rem;">
                Nhiều tính năng thú vị đang được phát triển!<br>
                Hãy quay lại để khám phá những cập nhật mới.
            </p>
            <div style="color: #ff9500; font-size: 0.8rem;">
                🔜 Coming Soon...
            </div>
        </div>
    """, unsafe_allow_html=True)

# About Section
st.markdown("## 📖 Giới thiệu dự án")

st.markdown("""
    <div style="background: rgba(255,255,255,0.05); padding: 2rem; border-radius: 15px; margin: 1rem 0;">
        <p style="color: #E8E8E8; line-height: 1.6; margin: 0;">
            <strong>LLMs Playground</strong> là một dự án thuộc khóa học <strong>AI4DEV</strong>, 
            được thiết kế để cung cấp một môi trường thân thiện và mạnh mẽ cho việc thực nghiệm 
            với các mô hình AI tiên tiến. Dự án này giúp người dùng dễ dàng tiếp cận và sử dụng 
            công nghệ AI mà không cần kiến thức lập trình sâu.
        </p>
    </div>
""", unsafe_allow_html=True)

# Tips Section
st.markdown("## 💡 Mẹo sử dụng")

tip_col1, tip_col2 = st.columns(2)

with tip_col1:
    st.markdown("""
        **🎯 Prompt hiệu quả:**
        - Sử dụng ngôn ngữ rõ ràng, cụ thể
        - Cung cấp context đầy đủ
        - Thử nghiệm với nhiều phong cách khác nhau
    """)

with tip_col2:
    st.markdown("""
        **⚙️ Tối ưu hóa:**
        - Điều chỉnh temperature cho creativity
        - Sử dụng max_tokens phù hợp
        - Thử nghiệm với nhiều model khác nhau
    """)

# Footer
st.markdown("""
    <div style="text-align: center; padding: 3rem; color: #B8B8B8; 
                border-top: 2px solid rgba(255, 215, 0, 0.3); margin-top: 4rem;
                background: linear-gradient(135deg, rgba(20, 20, 40, 0.8), rgba(255, 215, 0, 0.05));
                border-radius: 25px 25px 0 0;">
        <p>
            🎓 Được phát triển trong khóa học <strong>AI4DEV</strong><br>
            🚀 Assignment 3: LLMs Playground<br>
            💝 Được tạo ra với ❤️ và công nghệ AI
        </p>
    </div>
""", unsafe_allow_html=True)
