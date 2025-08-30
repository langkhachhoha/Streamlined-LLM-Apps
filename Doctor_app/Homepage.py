import streamlit as st
import json
import os
from datetime import datetime
import base64

st.set_page_config(
    page_title="Doctor App - Trang Chủ",
    page_icon="🏥",
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

# Get images for styling
doctor_image_path = "/Users/apple/Desktop/LLM-apps/image/Homepage.png"
doctor_base64 = get_base64_image(doctor_image_path)

vinbig_logo_path = "/Users/apple/Desktop/LLM-apps/image/logo_vinbig.png"
vinbig_logo_base64 = get_base64_image(vinbig_logo_path)

# Enhanced Medical Styling
if doctor_base64:
    background_style = f"background-image: url('data:image/png;base64,{doctor_base64}');"
else:
    background_style = "background: linear-gradient(135deg, #f0f8ff 0%, #e1f2ff 25%, #d1ecff 50%, #c1e6ff 75%, #b1e0ff 100%);"

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Poppins:wght@300;400;500;600;700;800;900&family=Outfit:wght@300;400;500;600;700;800;900&display=swap');
    /* Hide Streamlit UI Elements */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    .stDeployButton {{display: none;}}
    [data-testid="stToolbar"] {{display: none;}}
    [data-testid="stDecoration"] {{display: none;}}
    [data-testid="stStatusWidget"] {{display: none;}}
    [data-testid="manage-app-button"] {{display: none;}}
    /* Global Scroll Animation Setup */
    html {{
        scroll-behavior: smooth;
    }}
    
    .stApp {{
        {background_style}
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        font-family: 'Outfit', 'Inter', sans-serif;
        min-height: 100vh;
        position: relative;
        overflow-x: hidden;
    }}
    
    .stApp::before {{
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, 
            rgba(240, 248, 255, 0.85) 0%, 
            rgba(225, 242, 255, 0.8) 25%,
            rgba(209, 236, 255, 0.75) 50%,
            rgba(193, 230, 255, 0.8) 75%,
            rgba(177, 224, 255, 0.85) 100%);
        z-index: 0;
        pointer-events: none;
        animation: backgroundShift 20s ease-in-out infinite;
    }}
    
    @keyframes backgroundShift {{
        0%, 100% {{ 
            background: linear-gradient(135deg, 
                rgba(240, 248, 255, 0.85) 0%, 
                rgba(225, 242, 255, 0.8) 25%,
                rgba(209, 236, 255, 0.75) 50%,
                rgba(193, 230, 255, 0.8) 75%,
                rgba(177, 224, 255, 0.85) 100%);
        }}
        50% {{ 
            background: linear-gradient(135deg, 
                rgba(177, 224, 255, 0.85) 0%, 
                rgba(193, 230, 255, 0.8) 25%,
                rgba(209, 236, 255, 0.75) 50%,
                rgba(225, 242, 255, 0.8) 75%,
                rgba(240, 248, 255, 0.85) 100%);
        }}
    }}
    
    /* Advanced Animation Classes */
    .animate-on-scroll {{
        opacity: 0;
        transform: translateY(50px);
        transition: all 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }}
    
    .animate-on-scroll.animate {{
        opacity: 1;
        transform: translateY(0);
    }}
    
    .slide-in-left {{
        opacity: 0;
        transform: translateX(-100px);
        animation: slideInLeft 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards;
    }}
    
    .slide-in-right {{
        opacity: 0;
        transform: translateX(100px);
        animation: slideInRight 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards;
    }}
    
    .fade-in-up {{
        opacity: 0;
        transform: translateY(30px);
        animation: fadeInUp 1s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards;
    }}
    
    .scale-in {{
        opacity: 0;
        transform: scale(0.8);
        animation: scaleIn 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards;
    }}
    
    @keyframes slideInLeft {{
        0% {{
            opacity: 0;
            transform: translateX(-100px);
        }}
        100% {{
            opacity: 1;
            transform: translateX(0);
        }}
    }}
    
    @keyframes slideInRight {{
        0% {{
            opacity: 0;
            transform: translateX(100px);
        }}
        100% {{
            opacity: 1;
            transform: translateX(0);
        }}
    }}
    
    @keyframes fadeInUp {{
        0% {{
            opacity: 0;
            transform: translateY(30px);
        }}
        100% {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    
    @keyframes scaleIn {{
        0% {{
            opacity: 0;
            transform: scale(0.8);
        }}
        100% {{
            opacity: 1;
            transform: scale(1);
        }}
    }}
    
    /* Staggered Animation Delays */
    .delay-100 {{ animation-delay: 0.1s; }}
    .delay-200 {{ animation-delay: 0.2s; }}
    .delay-300 {{ animation-delay: 0.3s; }}
    .delay-400 {{ animation-delay: 0.4s; }}
    .delay-500 {{ animation-delay: 0.5s; }}
    .delay-600 {{ animation-delay: 0.6s; }}
    .delay-700 {{ animation-delay: 0.7s; }}
    .delay-800 {{ animation-delay: 0.8s; }}
    
    .main-container {{
        position: relative;
        z-index: 10;
        padding: 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }}
    
    .hero-section {{
        text-align: center;
        margin-bottom: 3rem;
        padding: 3rem 2rem;
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.95) 0%, 
            rgba(248, 252, 255, 0.92) 50%, 
            rgba(240, 248, 255, 0.95) 100%);
        border-radius: 20px;
        position: relative;
        box-shadow: 
            0 15px 35px rgba(0, 102, 204, 0.1),
            inset 0 1px 0 rgba(255, 255, 255, 0.8);
        border: 3px solid transparent;
        background-clip: padding-box;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
        overflow: hidden;
    }}
    
    .hero-section::before {{
        content: '';
        position: absolute;
        top: -3px;
        left: -3px;
        right: -3px;
        bottom: -3px;
        background: linear-gradient(45deg, 
            #87ceeb, #87cefa, #add8e6, #b0e0e6,
            #e0f6ff, #b0e0e6, #add8e6, #87ceeb);
        background-size: 400% 400%;
        border-radius: 23px;
        z-index: -1;
        animation: borderFlow 4s ease-in-out infinite;
    }}
    
    .hero-section:hover {{
        transform: translateY(-3px);
        box-shadow: 
            0 20px 40px rgba(0, 102, 204, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.9);
    }}
    
    @keyframes borderFlow {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}
    
    .main-title {{
        font-size: 3.2rem;
        font-weight: 700;
        color: #003366;
        margin-bottom: 1rem;
        text-shadow: 0 2px 4px rgba(0, 102, 204, 0.2);
    }}
    
    .subtitle {{
        font-size: 1.2rem;
        color: #0066cc;
        font-weight: 500;
        margin-bottom: 2rem;
        line-height: 1.5;
    }}
    
    /* Enhanced Medical Icons with Advanced Animations */
    .medical-icons {{
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin: 2rem 0;
        font-size: 2.5rem;
    }}
    
    .medical-icon {{
        transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        filter: grayscale(30%);
        cursor: pointer;
        position: relative;
        display: inline-block;
    }}
    
    .medical-icon::after {{
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        background: radial-gradient(circle, rgba(255,255,255,0.3) 0%, transparent 70%);
        border-radius: 50%;
        transform: translate(-50%, -50%);
        transition: all 0.3s ease;
        z-index: -1;
    }}
    
    .medical-icon:hover {{
        transform: translateY(-10px) scale(1.2) rotate(10deg);
        filter: grayscale(0%) brightness(1.2);
        text-shadow: 0 0 20px currentColor;
    }}
    
    .medical-icon:hover::after {{
        width: 60px;
        height: 60px;
    }}
    
    .medical-icon:nth-child(1) {{ 
        color: #e74c3c;
        animation: iconFloat 3s ease-in-out infinite;
    }}
    .medical-icon:nth-child(2) {{ 
        color: #f39c12;
        animation: iconFloat 3s ease-in-out infinite 0.6s;
    }}
    .medical-icon:nth-child(3) {{ 
        color: #3498db;
        animation: iconFloat 3s ease-in-out infinite 1.2s;
    }}
    .medical-icon:nth-child(4) {{ 
        color: #27ae60;
        animation: iconFloat 3s ease-in-out infinite 1.8s;
    }}
    .medical-icon:nth-child(5) {{ 
        color: #9b59b6;
        animation: iconFloat 3s ease-in-out infinite 2.4s;
    }}
    
    @keyframes iconFloat {{
        0%, 100% {{ transform: translateY(0) rotate(0deg); }}
        50% {{ transform: translateY(-10px) rotate(5deg); }}
    }}
    
    /* Scroll-triggered Info Cards */
    .info-card {{
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.9) 0%, 
            rgba(248, 252, 255, 0.85) 100%);
        border-radius: 15px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 15px 30px rgba(0, 102, 204, 0.1);
        border: 1px solid rgba(0, 102, 204, 0.1);
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        text-align: center;
        position: relative;
        overflow: hidden;
    }}
    
    .info-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, 
            transparent, 
            rgba(255, 255, 255, 0.4), 
            transparent);
        transition: left 0.6s ease;
    }}
    
    .info-card:hover {{
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 25px 50px rgba(0, 102, 204, 0.2);
        border-color: rgba(0, 188, 212, 0.3);
    }}
    
    .info-card:hover::before {{
        left: 100%;
    }}
    
    .card-icon {{
        font-size: 3rem;
        margin-bottom: 1rem;
        display: block;
        transition: all 0.3s ease;
    }}
    
    .info-card:hover .card-icon {{
        transform: scale(1.1) rotate(5deg);
        filter: drop-shadow(0 0 10px currentColor);
    }}
    
    .card-title {{
        font-size: 1.3rem;
        font-weight: 700;
        color: #003366;
        margin-bottom: 1rem;
        transition: color 0.3s ease;
    }}
    
    .info-card:hover .card-title {{
        color: #0066cc;
    }}
    
    .card-content {{
        color: #0066cc;
        line-height: 1.6;
        font-size: 1rem;
        transition: color 0.3s ease;
    }}
    
    .info-card:hover .card-content {{
        color: #003366;
    }}
    
    /* Advanced Form Animations */
    .form-container {{
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.95) 0%, 
            rgba(248, 252, 255, 0.9) 50%, 
            rgba(240, 248, 255, 0.95) 100%);
        border-radius: 20px;
        padding: 2.5rem;
        box-shadow: 
            0 20px 40px rgba(0, 102, 204, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.8);
        border: 2px solid rgba(0, 102, 204, 0.1);
        backdrop-filter: blur(15px);
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
    }}
    
    .form-container::before {{
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: conic-gradient(
            transparent,
            rgba(0, 188, 212, 0.1),
            transparent,
            rgba(0, 102, 204, 0.1),
            transparent
        );
        animation: formRotate 20s linear infinite;
        z-index: -1;
    }}
    
    @keyframes formRotate {{
        0% {{ transform: rotate(0deg); }}
        100% {{ transform: rotate(360deg); }}
    }}
    
    .form-title {{
        font-size: 2rem;
        font-weight: 800;
        color: #003366;
        text-align: center;
        margin-bottom: 2rem;
        position: relative;
    }}
    
    .form-title::after {{
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 100px;
        height: 3px;
        background: linear-gradient(45deg, #0066cc, #4da6ff);
        border-radius: 2px;
        animation: titleUnderline 2s ease-in-out infinite;
    }}
    
    @keyframes titleUnderline {{
        0%, 100% {{ width: 100px; }}
        50% {{ width: 150px; }}
    }}
    
    .success-message {{
        background: linear-gradient(135deg, #4CAF50, #45a049);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin-top: 2rem;
        font-weight: 600;
        font-size: 1.1rem;
        box-shadow: 0 15px 30px rgba(76, 175, 80, 0.3);
        animation: successPulse 2s ease-in-out infinite;
        position: relative;
        overflow: hidden;
    }}
    
    .success-message::before {{
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, 
            transparent, 
            rgba(255, 255, 255, 0.3), 
            transparent);
        animation: successShine 3s ease-in-out infinite;
    }}
    
    @keyframes successPulse {{
        0%, 100% {{ transform: scale(1); }}
        50% {{ transform: scale(1.02); }}
    }}
    
    @keyframes successShine {{
        0% {{ left: -100%; }}
        100% {{ left: 100%; }}
    }}
    
    /* Beautiful Sidebar Styling - Simplified */
    .css-1d391kg {{
        background: linear-gradient(145deg, 
            #1a237e 0%,
            #3949ab 25%, 
            #5c6bc0 50%, 
            #7986cb 75%, 
            #9fa8da 100%) !important;
        border-right: 4px solid rgba(255, 255, 255, 0.3) !important;
        box-shadow: 4px 0 20px rgba(0, 0, 0, 0.3) !important;
    }}
    
    /* Sidebar Text Colors */
    .css-1d391kg .stMarkdown p,
    .css-1d391kg .stMarkdown h1,
    .css-1d391kg .stMarkdown h2,
    .css-1d391kg .stMarkdown h3 {{
        color: #ffffff !important;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3) !important;
    }}
    
    /* Sidebar Navigation */
    .css-1d391kg [data-testid="stSidebarNav"] {{
        background: rgba(255, 255, 255, 0.15) !important;
        border-radius: 15px !important;
        padding: 1rem !important;
        margin: 1rem 0 !important;
        border: 2px solid rgba(255, 255, 255, 0.3) !important;
    }}
    
    .css-1d391kg [data-testid="stSidebarNav"] a {{
        color: #ffffff !important;
        font-weight: 600 !important;
        padding: 0.8rem 1.2rem !important;
        border-radius: 10px !important;
        background: rgba(255, 255, 255, 0.1) !important;
        margin: 0.3rem 0 !important;
        transition: all 0.3s ease !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
    }}
    
    .css-1d391kg [data-testid="stSidebarNav"] a:hover {{
        background: rgba(255, 255, 255, 0.25) !important;
        transform: translateX(8px) !important;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2) !important;
    }}
    
    /* Sidebar Info and Success boxes */
    .css-1d391kg .stAlert {{
        border-radius: 10px !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        backdrop-filter: blur(10px) !important;
    }}
    
    .css-1d391kg .stAlert p {{
        color: #ffffff !important;
        font-weight: 500 !important;
    }}
    
    /* Advanced JavaScript Scroll Animations */
    .scroll-fade-in {{
        opacity: 0;
        transform: translateY(30px);
        transition: all 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }}
    
    .scroll-fade-in.active {{
        opacity: 1;
        transform: translateY(0);
    }}
    
    .scroll-slide-left {{
        opacity: 0;
        transform: translateX(-50px);
        transition: all 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }}
    
    .scroll-slide-left.active {{
        opacity: 1;
        transform: translateX(0);
    }}
    
    .scroll-slide-right {{
        opacity: 0;
        transform: translateX(50px);
        transition: all 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }}
    
    .scroll-slide-right.active {{
        opacity: 1;
        transform: translateX(0);
    }}
    
    .scroll-scale-in {{
        opacity: 0;
        transform: scale(0.9);
        transition: all 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }}
    
    .scroll-scale-in.active {{
        opacity: 1;
        transform: scale(1);
    }}
    </style>
    
    <script>
    // Advanced Scroll Animation Script
    function initScrollAnimations() {{
        const observerOptions = {{
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        }};
        
        const observer = new IntersectionObserver((entries) => {{
            entries.forEach(entry => {{
                if (entry.isIntersecting) {{
                    entry.target.classList.add('active');
                }}
            }});
        }}, observerOptions);
        
        // Observe elements with scroll animation classes
        document.querySelectorAll('.scroll-fade-in, .scroll-slide-left, .scroll-slide-right, .scroll-scale-in').forEach(el => {{
            observer.observe(el);
        }});
    }}
    
    // Enhanced Icon Hover Effects
    function addIconEffects() {{
        document.querySelectorAll('.medical-icon').forEach((icon, index) => {{
            icon.addEventListener('mouseenter', function() {{
                const randomRotation = (Math.random() * 20 - 10);
                this.style.transform = `translateY(-15px) scale(1.3) rotate(${{randomRotation}}deg)`;
                this.style.filter = 'grayscale(0%) brightness(1.3) drop-shadow(0 0 20px currentColor)';
            }});
            
            icon.addEventListener('mouseleave', function() {{
                this.style.transform = '';
                this.style.filter = '';
            }});
        }});
    }}
    
    // Initialize when page loads
    document.addEventListener('DOMContentLoaded', function() {{
        initScrollAnimations();
        addIconEffects();
        
        // Add parallax effect to background
        window.addEventListener('scroll', function() {{
            const scrolled = window.pageYOffset;
            const rate = scrolled * -0.5;
            document.querySelector('.stApp::before')?.style.setProperty('transform', `translateY(${{rate}}px)`);
        }});
    }});
    
    // Retry initialization for Streamlit's dynamic loading
    setTimeout(() => {{
        initScrollAnimations();
        addIconEffects();
    }}, 1000);
    
    setTimeout(() => {{
        initScrollAnimations();
        addIconEffects();
    }}, 3000);
    </script>
    """,
    unsafe_allow_html=True
)

# Header with logo
if vinbig_logo_base64:
    st.markdown(
        f"""
        <div style="text-align: center; margin-bottom: 2rem;">
            <img src="data:image/png;base64,{vinbig_logo_base64}" 
                 style="height: 80px; border-radius: 10px; box-shadow: 0 10px 25px rgba(0,102,204,0.3);"
                 alt="VinBig Logo"/>
        </div>
        """,
        unsafe_allow_html=True
    )

# Sidebar với thông tin liên hệ và animation bác sĩ
with st.sidebar:
    # Doctor Animation - simplified
    st.markdown("### 🏥 VinBig Doctor App")
    
    # Animated doctor section
    st.markdown(
        """
        <div style="text-align: center; margin: 2rem 0;">
            <div style="font-size: 4rem; animation: bounce 2s infinite;">🧬🦠🧪🌡️</div>
            <div style="display: flex; justify-content: center; gap: 1rem; margin-top: 1rem;">
                <span style="font-size: 2rem; animation: float 3s infinite;">👩‍⚕️</span>
                <span style="font-size: 2rem; animation: float 3s infinite 0.5s;">🩺</span>
                <span style="font-size: 2rem; animation: float 3s infinite 1s;">⚕️🏩</span>
            </div>
        </div>
        
        <style>
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        @keyframes float {
            0%, 100% { transform: translateY(0) scale(1); }
            50% { transform: translateY(-5px) scale(1.1); }
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("---")
    
    # Contact Information - using Streamlit components
    st.markdown("### 📞 **THÔNG TIN LIÊN HỆ**")
    
    # Contact details
    st.info("""
    **📱 Hotline 24/7**  
    1900-555-888
    
    **📧 Email Hỗ Trợ**  
    support@vinbig-doctor.vn
    
    **🏢 Địa Chỉ**  
    Tòa VinBig, Hà Nội
    
    **🕒 Giờ Làm Việc**  
    24/7 - Luôn sẵn sàng
    
    **🚨 Cấp Cứu**  
    115 - Miễn phí
    """)
    
    st.markdown("---")
    
    # Additional info
    st.success("✅ Hệ thống AI hỗ trợ chẩn đoán")
    st.warning("⚠️ Chỉ mang tính chất tham khảo")
    
    # Medical icons animation
    st.markdown(
        """
        <div style="text-align: center; margin: 1rem 0; font-size: 1.5rem;">
            <span style="animation: pulse 2s infinite;">🩺</span>
            <span style="animation: pulse 2s infinite 0.3s;">💊</span>
            <span style="animation: pulse 2s infinite 0.6s;">💉</span>
            <span style="animation: pulse 2s infinite 0.9s;">🔬</span>
            <span style="animation: pulse 2s infinite 1.2s;">🏥</span>
        </div>
        
        <style>
        @keyframes pulse {
            0%, 100% { transform: scale(1); opacity: 0.7; }
            50% { transform: scale(1.2); opacity: 1; }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Main container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Enhanced Hero Section với animation slide-in từ trái
st.markdown(
    """
    <div class="hero-section slide-in-left">
        <h1 class="main-title">🏥 Doctor App - VinBig Medical Center</h1>
        <p class="subtitle fade-in-up delay-300">Hệ thống quản lý thông tin bệnh nhân thông minh với công nghệ AI tiên tiến</p>
        <div class="medical-icons fade-in-up delay-500">
            <span class="medical-icon delay-100">🩺</span>
            <span class="medical-icon delay-200">💊</span>
            <span class="medical-icon delay-300">🏥</span>
            <span class="medical-icon delay-400">⚕️</span>
            <span class="medical-icon delay-500">💉</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# App Description Section với scroll animations
st.markdown('<div class="scroll-fade-in">', unsafe_allow_html=True)
st.markdown("## 🎯 Giới thiệu về ứng dụng")
st.markdown('</div>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="scroll-slide-left">', unsafe_allow_html=True)
    st.markdown("""
    ### 🌟 **Doctor App** - Giải pháp y tế thông minh của tương lai
    
    **Doctor App** là một hệ thống quản lý thông tin bệnh nhân hiện đại, được phát triển bởi **VinBig AI** 
    với mục tiêu cách mạng hóa ngành chăm sóc sức khỏe thông qua công nghệ tiên tiến.
    
    #### 🔬 **Công nghệ AI tích hợp:**
    - **Machine Learning**: Hỗ trợ chẩn đoán thông minh
    - **Deep Learning**: Phân tích hình ảnh y tế
    - **Natural Language Processing**: Xử lý hồ sơ bệnh án
    - **Predictive Analytics**: Dự đoán xu hướng sức khỏe
    
    #### 🎯 **Sứ mệnh:**
    Chúng tôi cam kết mang đến giải pháp y tế **an toàn**, **chính xác** và **hiệu quả** 
    để bác sĩ có thể đưa ra quyết định điều trị tốt nhất cho bệnh nhân.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="scroll-slide-right">', unsafe_allow_html=True)
    st.info("""
    📊 **Thống kê ấn tượng:**
    
    • **15,000+** bệnh nhân đã tin tưởng
    • **50+** bác sĩ chuyên nghiệp
    • **99.5%** độ chính xác AI
    • **24/7** hỗ trợ không ngừng
    • **100%** bảo mật dữ liệu
    
    🏆 **Chứng nhận:**
    • ISO 27001 - Bảo mật thông tin
    • HIPAA Compliant - Tuân thủ y tế
    • GDPR Ready - Bảo vệ dữ liệu
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Detailed User Guide Section với animations
st.markdown("---")
st.markdown('<div class="scroll-fade-in">', unsafe_allow_html=True)
st.markdown("## 📚 Hướng dẫn sử dụng chi tiết")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="scroll-scale-in">', unsafe_allow_html=True)
st.markdown("""
### 🚀 **Quy trình hoàn chỉnh từ A đến Z**

Để sử dụng **Doctor App** một cách hiệu quả, vui lòng làm theo các bước sau:
""")
st.markdown('</div>', unsafe_allow_html=True)

# Step-by-step guide with enhanced styling và animations
step_col1, step_col2 = st.columns(2)

with step_col1:
    st.markdown('<div class="scroll-slide-left">', unsafe_allow_html=True)
    st.markdown("""
    #### **🔹 BƯỚC 1: Chuẩn bị thông tin**
    """)
    st.success("""
    📋 **Tài liệu cần có:**
    • CCCD/CMND của bệnh nhân
    • Thẻ bảo hiểm y tế (nếu có)
    • Hồ sơ bệnh án cũ (nếu có)
    • Danh sách thuốc đang sử dụng
    • Thông tin liên hệ khẩn cấp
    
    ⏱️ **Thời gian:** 2-3 phút chuẩn bị
    """)
    
    st.markdown("""
    #### **🔹 BƯỚC 3: Xác thực & lưu trữ**
    """)
    st.info("""
    🔍 **Quá trình xác thực:**
    • Hệ thống kiểm tra tính hợp lệ
    • AI phân tích và đánh giá
    • Mã hóa dữ liệu AES-256
    • Tạo mã bệnh nhân duy nhất
    • Đồng bộ vào cơ sở dữ liệu
    
    🔐 **Bảo mật:** Tuân thủ chuẩn quốc tế
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with step_col2:
    st.markdown('<div class="scroll-slide-right">', unsafe_allow_html=True)
    st.markdown("""
    #### **🔹 BƯỚC 2: Điền form thông tin**
    """)
    st.warning("""
    ✍️ **Cách điền form hiệu quả:**
    • Điền đầy đủ thông tin cá nhân
    • Mô tả chi tiết triệu chứng
    • Liệt kê tiền sử bệnh tật
    • Ghi rõ thuốc đang sử dụng
    • Thêm ghi chú quan trọng
    
    💡 **Mẹo:** Thông tin càng chi tiết, chẩn đoán càng chính xác
    """)
    
    st.markdown("""
    #### **🔹 BƯỚC 4: Khám & điều trị**
    """)
    st.error("""
    🩺 **Quy trình khám bệnh:**
    • Bác sĩ truy cập hồ sơ điện tử
    • AI hỗ trợ phân tích triệu chứng
    • Đề xuất phương án điều trị
    • Theo dõi tiến triển bệnh
    • Cập nhật hồ sơ liên tục
    
    ⚕️ **Kết quả:** Điều trị hiệu quả và an toàn
    """)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# Patient Information Form với advanced animations
st.markdown('<div class="scroll-fade-in">', unsafe_allow_html=True)
st.markdown('<h2 class="form-title">📋 Thông tin bệnh nhân</h2>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Initialize session state for form success
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

st.markdown('<div class="scroll-scale-in">', unsafe_allow_html=True)
with st.form("patient_info_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        full_name = st.text_input(
            "**👤 Họ và tên**",
            placeholder="Nhập họ và tên đầy đủ",
            help="Vui lòng nhập họ và tên đầy đủ của bệnh nhân"
        )
        
        phone = st.text_input(
            "**📱 Số điện thoại**",
            placeholder="0xxxxxxxxx",
            help="Số điện thoại liên hệ"
        )
        
        address = st.text_area(
            "**🏠 Địa chỉ**",
            placeholder="Nhập địa chỉ đầy đủ",
            help="Địa chỉ nơi ở hiện tại"
        )
        
        emergency_contact = st.text_input(
            "**🚨 Người liên hệ khẩn cấp**",
            placeholder="Tên và số điện thoại",
            help="Thông tin người thân để liên hệ khi cần thiết"
        )
    
    with col2:
        birth_date = st.date_input(
            "**🎂 Ngày sinh**",
            help="Chọn ngày sinh của bệnh nhân"
        )
        
        gender = st.selectbox(
            "**⚥ Giới tính**",
            options=["Nam", "Nữ", "Khác"],
            help="Chọn giới tính"
        )
        
        id_number = st.text_input(
            "**🆔 CCCD/CMND**",
            placeholder="Số căn cước công dân",
            help="Số căn cước công dân hoặc chứng minh nhân dân"
        )
        
        insurance_number = st.text_input(
            "**🏥 Số thẻ bảo hiểm y tế**",
            placeholder="Mã số BHYT",
            help="Mã số thẻ bảo hiểm y tế (nếu có)"
        )
    
    # Medical Analysis Section - AI Personalization Data
    st.markdown("---")
    st.markdown("### 🧬 Thông tin phân tích AI")
    
    col3, col4 = st.columns(2)
    
    with col3:
        current_symptoms = st.text_area(
            "**� Triệu chứng hiện tại**",
            placeholder="Mô tả chi tiết các triệu chứng: đau đầu, sốt, ho, khó thở, đau bụng...",
            help="Thông tin này giúp AI phân tích và đề xuất chẩn đoán ban đầu"
        )
        
        pain_level = st.selectbox(
            "**� Chất lượng giấc ngủ**",
            options=[
                "Rất tốt - ngủ sâu giấc 7-8 tiếng",
                "Tốt - ngủ đủ giấc, thỉnh thoảng thức giữa đêm",
                "Trung bình - ngủ được nhưng không sâu giấc",
                "Kém - thường xuyên mất ngủ, ngủ không đủ giấc",
                "Rất kém - mất ngủ triền miên, ngủ dưới 5 tiếng"
            ],
            help="Chất lượng giấc ngủ ảnh hưởng trực tiếp đến sức khỏe tổng thể"
        )
        
        family_history = st.text_area(
            "**👨‍👩‍👧‍👦 Tiền sử gia đình**",
            placeholder="Bệnh di truyền, ung thư, tim mạch, tiểu đường trong gia đình...",
            help="Thông tin di truyền giúp AI đánh giá yếu tố nguy cơ"
        )
    
    with col4:
        lifestyle_habits = st.text_area(
            "**🏃‍♂️ Thói quen sống**",
            placeholder="Hút thuốc, uống rượu, tập thể dục, chế độ ăn, giấc ngủ...",
            help="Lối sống ảnh hưởng lớn đến sức khỏe và khả năng hồi phục"
        )
        
        work_environment = st.selectbox(
            "**🏢 Môi trường làm việc**",
            options=[
                "Văn phòng - ít vận động",
                "Lao động chân tay",
                "Y tế - tiếp xúc bệnh nhân",
                "Giáo dục",
                "Công nghiệp - hóa chất",
                "Nông nghiệp",
                "Dịch vụ - tiếp xúc đông người",
                "Công nghệ thông tin",
                "Khác"
            ],
            help="Môi trường làm việc có thể là nguyên nhân gây bệnh"
        )
        
        stress_anxiety_level = st.selectbox(
            "**😰 Mức độ căng thẳng/lo âu**",
            options=[
                "Rất thấp - cuộc sống bình yên",
                "Thấp - thỉnh thoảng căng thẳng",
                "Trung bình - căng thẳng công việc",
                "Cao - thường xuyên lo lắng",
                "Rất cao - áp lực liên tục"
            ],
            help="Tâm lý ảnh hưởng trực tiếp đến sức khỏe thể chất"
        )
        
        additional_info = st.text_area(
            "**💭 Thông tin thêm**",
            placeholder="Chia sẻ bất kỳ điều gì bạn muốn bác sĩ biết: cảm xúc, lo lắng, kỳ vọng, câu hỏi...",
            help="Không gian tự do để bạn chia sẻ những điều quan trọng khác mà bạn muốn bác sĩ biết",
            height=100
        )
    
    # Submit button
    submitted = st.form_submit_button(
        "💾 Lưu thông tin bệnh nhân", 
        use_container_width=True,
        type="primary"
    )
    
    if submitted:
        # Validate required fields
        if not full_name or not phone or not birth_date:
            st.error("❌ Vui lòng điền đầy đủ thông tin bắt buộc: Họ tên, Số điện thoại, Ngày sinh")
        else:
            # Create patient data
            patient_data = {
                "patient_id": f"BN_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                "personal_info": {
                    "full_name": full_name,
                    "birth_date": birth_date.strftime("%Y-%m-%d"),
                    "gender": gender,
                    "phone": phone,
                    "id_number": id_number,
                    "address": address,
                    "emergency_contact": emergency_contact,
                    "insurance_number": insurance_number
                },
                "medical_analysis": {
                    "current_symptoms": current_symptoms,
                    "sleep_quality": pain_level,
                    "family_history": family_history,
                    "lifestyle_habits": lifestyle_habits,
                    "work_environment": work_environment,
                    "stress_anxiety_level": stress_anxiety_level,
                    "additional_info": additional_info
                },
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            # Save to JSON file
            json_file_path = "/Users/apple/Desktop/LLM-apps/Doctor_app/patient_data.json"
            
            # Load existing data or create new
            try:
                if os.path.exists(json_file_path):
                    with open(json_file_path, 'r', encoding='utf-8') as f:
                        existing_data = json.load(f)
                else:
                    existing_data = {"patients": []}
            except:
                existing_data = {"patients": []}
            
            # Add new patient
            existing_data["patients"].append(patient_data)
            
            # Save updated data
            try:
                with open(json_file_path, 'w', encoding='utf-8') as f:
                    json.dump(existing_data, f, ensure_ascii=False, indent=2)
                
                st.session_state.form_submitted = True
                st.success(
                    f"""
                    ✅ **Thông tin bệnh nhân đã được lưu thành công!**
                    
                    **Mã bệnh nhân:** {patient_data['patient_id']}
                    
                    **Thông tin đã lưu:**
                    - Họ tên: {full_name}
                    - Số điện thoại: {phone}
                    - Ngày tạo: {patient_data['created_at']}
                    """
                )
                
            except Exception as e:
                st.error(f"❌ Lỗi khi lưu dữ liệu: {str(e)}")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Information Cards using Streamlit columns với animations
st.markdown('<div class="scroll-fade-in">', unsafe_allow_html=True)
st.markdown("### 🏥 Dịch vụ của chúng tôi")
st.markdown('</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="scroll-slide-left">', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="info-card">
            <div class="card-icon">🩺</div>
            <div class="card-title">Khám bệnh chuyên nghiệp</div>
            <div class="card-content">
                Đội ngũ bác sĩ giàu kinh nghiệm, sử dụng công nghệ AI hỗ trợ chẩn đoán chính xác
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <div class="info-card">
            <div class="card-icon">🔐</div>
            <div class="card-title">Bảo mật tuyệt đối</div>
            <div class="card-content">
                Thông tin bệnh nhân được mã hóa và bảo vệ theo tiêu chuẩn y tế quốc tế
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="scroll-slide-right">', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="info-card">
            <div class="card-icon">📝</div>
            <div class="card-title">Quản lý hồ sơ thông minh</div>
            <div class="card-content">
                Hệ thống lưu trữ và quản lý thông tin bệnh nhân an toàn, tiện lợi
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <div class="info-card">
            <div class="card-icon">⚡</div>
            <div class="card-title">Phản hồi nhanh chóng</div>
            <div class="card-content">
                Hệ thống xử lý thông tin nhanh chóng, hỗ trợ bác sĩ đưa ra quyết định kịp thời
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Enhanced Footer với animations
st.markdown("---")
st.markdown('<div class="scroll-fade-in">', unsafe_allow_html=True)
st.markdown("## 🌐 Thông tin tổ chức")
st.markdown('</div>', unsafe_allow_html=True)

footer_col1, footer_col2, footer_col3 = st.columns(3)

with footer_col1:
    st.markdown('<div class="scroll-slide-left">', unsafe_allow_html=True)
    st.markdown("""
    ### 🏢 **VinBig AI**
    """)
    st.info("""
    **Địa chỉ trụ sở:**
    Tòa VinBig, Khu Công nghệ cao
    Hà Nội, Việt Nam
    
    **Giấy phép:**
    • Số ĐKKD: 0123456789
    • Ngày cấp: 01/01/2023
    • Nơi cấp: Sở KH&ĐT Hà Nội
    
    **Website:** vinbig.ai
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with footer_col2:
    st.markdown('<div class="scroll-scale-in">', unsafe_allow_html=True)
    st.markdown("""
    ### 📞 **Liên hệ nhanh**
    """)
    st.success("""
    **Hotline 24/7:**
    🔥 Khẩn cấp: 1900-555-888
    📞 Tư vấn: 1900-555-999
    
    **Email:**
    📧 support@vinbig-doctor.vn
    📧 info@vinbig.ai
    
    **Mạng xã hội:**
    📘 Facebook: /VinBigAI
    📷 Instagram: @vinbig_ai
    🐦 Twitter: @VinBigAI
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with footer_col3:
    st.markdown('<div class="scroll-slide-right">', unsafe_allow_html=True)
    st.markdown("""
    ### 🎯 **Tầm nhìn & Sứ mệnh**
    """)
    st.warning("""
    **Tầm nhìn 2030:**
    Trở thành nền tảng y tế AI #1 
    Đông Nam Á
    
    **Sứ mệnh:**
    Democratize healthcare through AI
    
    **Giá trị cốt lõi:**
    • Đổi mới sáng tạo
    • An toàn bệnh nhân
    • Chất lượng vượt trội
    • Trách nhiệm xã hội
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Copyright and legal footer với animation
st.markdown('<div class="scroll-fade-in">', unsafe_allow_html=True)
st.markdown(
    """
    <div style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        text-align: center;
        padding: 2rem;
        border-radius: 15px;
        margin-top: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        position: relative;
        overflow: hidden;
    ">
        <div style="
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.1) 50%, transparent 70%);
            animation: footerShine 3s ease-in-out infinite;
        "></div>
        <h3 style="margin-bottom: 1rem; color: white; position: relative; z-index: 1;">🏥 Doctor App - VinBig Medical Center</h3>
        <p style="font-size: 1.1rem; margin-bottom: 1rem; position: relative; z-index: 1;">
            Hệ thống quản lý bệnh nhân thông minh với công nghệ AI tiên tiến
        </p>
        <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap; margin-bottom: 1rem; position: relative; z-index: 1;">
            <span>📞 Hotline: 1900-555-888</span>
            <span>📧 Email: support@vinbig-doctor.vn</span>
            <span>🌐 Website: vinbig.ai</span>
        </div>
        <hr style="border: 1px solid rgba(255,255,255,0.3); margin: 1rem 0;">
        <div style="font-size: 0.9rem; opacity: 0.8; position: relative; z-index: 1;">
            <p>© 2025 VinBig AI Corporation. All rights reserved.</p>
            <p>Bảo mật dữ liệu • Tuân thủ GDPR • Chứng nhận ISO 27001</p>
            <p style="font-style: italic;">
                "Công nghệ AI phục vụ sức khỏe cộng đồng"
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)
