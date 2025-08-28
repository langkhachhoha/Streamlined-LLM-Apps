import streamlit as st
import requests
import json
import pandas as pd
import base64
import os

st.set_page_config(
    page_title="Diabetes Doctor - AI Health Consultant",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to encode image to base64
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

# Get doctor image
doctor_image_path = "/Users/apple/Desktop/LLM-apps/image/Doctor.png"
doctor_base64 = get_base64_image(doctor_image_path)

# Get doctor_1 image for form section
doctor_1_image_path = "/Users/apple/Desktop/LLM-apps/image/Doctor_1.png"
doctor_1_base64 = get_base64_image(doctor_1_image_path)

# Get doctor_2 to doctor_5 images for other sections
doctor_2_image_path = "/Users/apple/Desktop/LLM-apps/image/Doctor_2.png"
doctor_2_base64 = get_base64_image(doctor_2_image_path)

doctor_3_image_path = "/Users/apple/Desktop/LLM-apps/image/Doctor_3.png"
doctor_3_base64 = get_base64_image(doctor_3_image_path)

doctor_4_image_path = "/Users/apple/Desktop/LLM-apps/image/Doctor_4.png"
doctor_4_base64 = get_base64_image(doctor_4_image_path)

doctor_5_image_path = "/Users/apple/Desktop/LLM-apps/image/Doctor_5.png"
doctor_5_base64 = get_base64_image(doctor_5_image_path)

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
        background: linear-gradient(135deg, 
            rgba(240, 248, 255, 0.75) 0%, 
            rgba(225, 242, 255, 0.7) 25%,
            rgba(209, 236, 255, 0.65) 50%,
            rgba(193, 230, 255, 0.7) 75%,
            rgba(177, 224, 255, 0.75) 100%);
        z-index: 0;
        pointer-events: none;
    }}
    """ + """
    
    .floating-elements {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 1;
    }
    
    .floating-icon {
        position: absolute;
        font-size: 2rem;
        opacity: 0.1;
        animation: float 6s ease-in-out infinite;
    }
    
    .floating-icon:nth-child(1) { top: 10%; left: 10%; animation-delay: 0s; }
    .floating-icon:nth-child(2) { top: 20%; right: 15%; animation-delay: 1s; }
    .floating-icon:nth-child(3) { top: 60%; left: 5%; animation-delay: 2s; }
    .floating-icon:nth-child(4) { bottom: 20%; right: 10%; animation-delay: 3s; }
    .floating-icon:nth-child(5) { bottom: 40%; left: 20%; animation-delay: 4s; }
    .floating-icon:nth-child(6) { top: 50%; left: 80%; animation-delay: 5s; }
    .floating-icon:nth-child(7) { top: 80%; right: 5%; animation-delay: 6s; }
    .floating-icon:nth-child(8) { top: 5%; right: 50%; animation-delay: 7s; }
    .floating-icon:nth-child(9) { bottom: 60%; left: 40%; animation-delay: 8s; }
    .floating-icon:nth-child(10) { top: 30%; left: 60%; animation-delay: 9s; }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(180deg); }
    }
    
    .main-container {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.98) 0%, rgba(248, 252, 255, 0.96) 100%);
        backdrop-filter: blur(20px);
        border-radius: 25px;
        padding: 3rem 4rem;
        margin: 1rem auto;
        max-width: 1400px;
        box-shadow: 
            0 25px 50px rgba(0, 100, 200, 0.12),
            0 0 0 1px rgba(255,255,255,0.8),
            inset 0 1px 0 rgba(255,255,255,0.9);
        border: 2px solid rgba(0, 102, 204, 0.15);
        position: relative;
        overflow: hidden;
        z-index: 10;
    }
    
    .main-container::before {
        content: '';
        position: absolute;
        top: -2px;
        left: -2px;
        right: -2px;
        bottom: -2px;
        background: linear-gradient(45deg, #0066cc, #0080ff, #4da6ff, #80c0ff, #0066cc);
        background-size: 300% 300%;
        border-radius: 27px;
        z-index: -1;
        animation: borderFlow 15s linear infinite;
    }
    
    @keyframes borderFlow {
        0% { background-position: 0% 50%; }
        100% { background-position: 300% 50%; }
    }
    
    .medical-title {
        font-size: 3.2rem;
        font-weight: 900;
        background: linear-gradient(45deg, #003366, #0066cc, #0080ff, #4da6ff);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.3em;
        text-align: center;
        animation: titleFlow 4s ease-in-out infinite;
        font-family: 'Outfit', sans-serif;
        text-shadow: 0 0 20px rgba(0, 102, 204, 0.2);
        position: relative;
    }
    
    @keyframes titleFlow {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .medical-title::before {
        content: '🩺';
        position: absolute;
        left: -80px;
        top: 50%;
        transform: translateY(-50%);
        font-size: 3rem;
        animation: logoRotate 4s ease-in-out infinite;
    }
    
    .medical-title::after {
        content: '⚕️';
        position: absolute;
        right: -80px;
        top: 50%;
        transform: translateY(-50%);
        font-size: 3rem;
        animation: logoRotate 4s ease-in-out infinite reverse;
    }
    
    @keyframes logoRotate {
        0%, 100% { 
            transform: translateY(-50%) rotate(0deg) scale(1);
            opacity: 0.8;
        }
        25% { 
            transform: translateY(-60%) rotate(90deg) scale(1.1);
            opacity: 1;
        }
        50% { 
            transform: translateY(-50%) rotate(180deg) scale(1.2);
            opacity: 0.9;
        }
        75% { 
            transform: translateY(-40%) rotate(270deg) scale(1.1);
            opacity: 1;
        }
    }
    
    .subtitle {
        font-size: 1.2em;
        background: linear-gradient(45deg, #003366, #4da6ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 1.5em;
        font-weight: 600;
        letter-spacing: 0.5px;
    }
    
    .doctor-badge {
        background: linear-gradient(135deg, #003366, #0066cc, #0080ff);
        background-size: 200% 200%;
        border-radius: 20px;
        padding: 1.2rem;
        margin-bottom: 1.2rem;
        border: 2px solid rgba(255,255,255,0.3);
        box-shadow: 0 12px 25px rgba(0, 51, 102, 0.25);
        position: relative;
        overflow: hidden;
        animation: badgeShimmer 6s ease-in-out infinite, float 4s ease-in-out infinite;
    }
    
    @keyframes badgeShimmer {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    @keyframes heartbeat {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.2); }
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 0.9; transform: scale(1); }
        50% { opacity: 1; transform: scale(1.02); }
    }
    
    .doctor-badge::before {
        content: '👨‍⚕️👩‍⚕️💊🔬🩺⚕️';
        position: absolute;
        top: 10px;
        right: 20px;
        font-size: 1.5rem;
        animation: iconFloat 3s ease-in-out infinite;
    }
    
    .doctor-badge::after {
        content: '🏥💉🧬❤️🫀🩻';
        position: absolute;
        bottom: 10px;
        left: 20px;
        font-size: 1.2rem;
        animation: iconFloat 3s ease-in-out infinite 1.5s;
        opacity: 0.7;
    }
    
    @keyframes iconFloat {
        0%, 100% { transform: translateY(0) rotate(0deg); }
        50% { transform: translateY(-10px) rotate(5deg); }
    }
    
        .health-form {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(248, 250, 255, 0.9) 100%);
        border-radius: 25px;
        padding: 3rem;
        margin: 2rem auto;
        max-width: 1200px;
        border: 3px solid rgba(0, 102, 204, 0.3);
        box-shadow: 
            0 25px 50px rgba(0, 102, 204, 0.15),
            inset 0 1px 0 rgba(255,255,255,0.8);
        position: relative;
        backdrop-filter: blur(15px);
    }
    
    .health-form::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
        animation: shimmer 5s infinite;
    }
    
    @keyframes shimmer {
        0% { left: -100%; }
        100% { left: 100%; }
    }
    
    .form-section {
        margin-bottom: 2rem;
        padding: 2rem;
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(240, 248, 255, 0.9) 100%);
        border-radius: 20px;
        border: 2px solid rgba(0, 102, 204, 0.3);
        position: relative;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
        box-shadow: 0 15px 35px rgba(0, 51, 102, 0.2);
        color: #003366;
        overflow: hidden;
    }
    
    .form-section::before {
        content: '🩺';
        position: absolute;
        top: 10px;
        left: 15px;
        font-size: 1.5rem;
        opacity: 0.2;
        animation: cornerFloat 4s ease-in-out infinite;
    }
    
    .form-section::after {
        content: '⚕️';
        position: absolute;
        bottom: 10px;
        right: 15px;
        font-size: 1.5rem;
        opacity: 0.2;
        animation: cornerFloat 4s ease-in-out infinite 2s;
    }
    
    @keyframes cornerFloat {
        0%, 100% { transform: scale(1) rotate(0deg); opacity: 0.2; }
        50% { transform: scale(1.2) rotate(10deg); opacity: 0.4; }
    }
    
    .form-section:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 45px rgba(0, 51, 102, 0.3);
        border-color: rgba(0, 102, 204, 0.5);
    }
    
    .form-section:hover::before,
    .form-section:hover::after {
        opacity: 0.6;
        animation-duration: 2s;
    }
    
    .section-title {
        font-size: 1.4em;
        font-weight: 700;
        color: #003366;
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 0.8rem;
        position: relative;
        text-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }
    
    .section-title::before {
        content: '✨';
        animation: sparkle 3s ease-in-out infinite;
        color: #0066cc;
        font-size: 1.2em;
    }
    
    @keyframes sparkle {
        0%, 100% { transform: scale(1) rotate(0deg); }
        50% { transform: scale(1.1) rotate(180deg); }
    }
    
    @keyframes blink {
        0% { 
            color: #ffffff; 
            text-shadow: 2px 2px 4px rgba(0,0,0,0.8), 0 0 20px rgba(255,255,255,0.8); 
        }
        25% { 
            color: #00ffff; 
            text-shadow: 2px 2px 4px rgba(0,0,0,0.8), 0 0 30px rgba(0,255,255,1); 
        }
        50% { 
            color: #ffff00; 
            text-shadow: 2px 2px 4px rgba(0,0,0,0.8), 0 0 40px rgba(255,255,0,1); 
        }
        75% { 
            color: #ff6600; 
            text-shadow: 2px 2px 4px rgba(0,0,0,0.8), 0 0 30px rgba(255,102,0,1); 
        }
        100% { 
            color: #ffffff; 
            text-shadow: 2px 2px 4px rgba(0,0,0,0.8), 0 0 20px rgba(255,255,255,0.8); 
        }
    }
    
    .prediction-card {
        background: linear-gradient(135deg, #0066cc, #0080ff, #4da6ff);
        background-size: 200% 200%;
        border-radius: 30px;
        padding: 3rem;
        margin: 3rem 0;
        text-align: center;
        box-shadow: 
            0 30px 60px rgba(0, 102, 204, 0.3),
            inset 0 1px 0 rgba(255,255,255,0.3);
        border: 3px solid rgba(255,255,255,0.4);
        animation: cardFloat 4s ease-in-out infinite;
        position: relative;
        overflow: hidden;
    }
    
    @keyframes cardFloat {
        0%, 100% { 
            transform: translateY(0) scale(1);
            background-position: 0% 50%;
        }
        50% { 
            transform: translateY(-10px) scale(1.02);
            background-position: 100% 50%;
        }
    }
    
    .prediction-card.high-risk {
        background: linear-gradient(135deg, #cc3300, #ff4444, #ff6666);
        box-shadow: 0 30px 60px rgba(204, 51, 0, 0.4);
        animation: dangerPulse 3s ease-in-out infinite;
    }
    
    @keyframes dangerPulse {
        0%, 100% { 
            box-shadow: 0 30px 60px rgba(204, 51, 0, 0.4);
            transform: scale(1);
        }
        50% { 
            box-shadow: 0 40px 80px rgba(204, 51, 0, 0.6);
            transform: scale(1.02);
        }
    }
    
    .prediction-card.low-risk {
        background: linear-gradient(135deg, #00cc66, #00ff80, #66ffaa);
        box-shadow: 0 30px 60px rgba(0, 204, 102, 0.4);
        animation: successGlow 3s ease-in-out infinite;
    }
    
    @keyframes successGlow {
        0%, 100% { 
            box-shadow: 0 30px 60px rgba(0, 204, 102, 0.4);
            transform: scale(1);
        }
        50% { 
            box-shadow: 0 40px 80px rgba(0, 204, 102, 0.6);
            transform: scale(1.02);
        }
    }
    
    .prediction-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        animation: spotlight 4s linear infinite;
    }
    
    @keyframes spotlight {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .risk-icon {
        font-size: 4rem;
        margin-bottom: 1.5rem;
        animation: iconBounce 2s ease-in-out infinite;
        position: relative;
        z-index: 2;
    }
    
    @keyframes iconBounce {
        0%, 100% { transform: translateY(0) scale(1); }
        50% { transform: translateY(-15px) scale(1.1); }
    }
    
    .prediction-text {
        font-size: 2rem;
        font-weight: 800;
        margin-bottom: 1.5rem;
        text-shadow: 0 4px 8px rgba(0,0,0,0.3);
        position: relative;
        z-index: 2;
        font-family: 'Outfit', sans-serif;
    }
    
    .confidence-bar {
        background: rgba(255,255,255,0.3);
        border-radius: 15px;
        height: 15px;
        margin: 1.5rem 0;
        overflow: hidden;
        position: relative;
        z-index: 2;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.2);
    }
    
    .confidence-fill {
        height: 100%;
        border-radius: 15px;
        background: linear-gradient(90deg, rgba(255,255,255,0.8), rgba(255,255,255,1));
        transition: width 2s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .confidence-fill::after {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.6), transparent);
        animation: confidenceShine 2s infinite;
    }
    
    @keyframes confidenceShine {
        0% { left: -100%; }
        100% { left: 100%; }
    }
    
    .medical-advice {
        background: linear-gradient(135deg, #0066cc, #0080ff, #4da6ff);
        background-size: 200% 200%;
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        border: 3px solid rgba(255,255,255,0.3);
        box-shadow: 0 20px 40px rgba(0, 102, 204, 0.3);
        animation: adviceShimmer 6s ease-in-out infinite;
        position: relative;
        overflow: hidden;
    }
    
    @keyframes adviceShimmer {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .medical-advice::before {
        content: '💡��⚕️';
        position: absolute;
        top: 15px;
        right: 20px;
        font-size: 1.2rem;
        animation: adviceIcons 4s ease-in-out infinite;
    }
    
    @keyframes adviceIcons {
        0%, 100% { transform: rotate(0deg) scale(1); }
        50% { transform: rotate(10deg) scale(1.1); }
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #0066cc, #0080ff, #4da6ff) !important;
        background-size: 200% 200% !important;
        color: white !important;
        border: none !important;
        border-radius: 20px !important;
        padding: 1rem 3rem !important;
        font-size: 1.3em !important;
        font-weight: 700 !important;
        box-shadow: 0 15px 35px rgba(0, 102, 204, 0.4) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        width: 100% !important;
        animation: buttonPulse 4s ease-in-out infinite !important;
        position: relative !important;
        overflow: hidden !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
    }
    
    @keyframes buttonPulse {
        0%, 100% { 
            background-position: 0% 50%;
            transform: scale(1);
        }
        50% { 
            background-position: 100% 50%;
            transform: scale(1.02);
        }
    }
    
    .stButton > button:hover {
        transform: translateY(-5px) scale(1.05) !important;
        box-shadow: 0 25px 50px rgba(0, 102, 204, 0.6) !important;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
        transition: left 0.5s;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
        .medical-info {
        background: linear-gradient(135deg, rgba(0, 102, 204, 0.1), rgba(77, 166, 255, 0.05));
        border-left: 4px solid #0066cc;
        padding: 0.8rem 1rem;
        margin: 0.6rem 0;
        border-radius: 10px;
        font-size: 0.9em;
        color: #003366;
        font-weight: 600;
        box-shadow: 0 4px 12px rgba(0, 102, 204, 0.2);
        transition: all 0.3s ease;
        border: 1px solid rgba(0, 102, 204, 0.3);
    }
    
    .medical-info:hover {
        transform: translateX(8px);
        box-shadow: 0 6px 20px rgba(0, 102, 204, 0.3);
        background: linear-gradient(135deg, rgba(0, 102, 204, 0.15), rgba(77, 166, 255, 0.1));
    }
    
    .medical-info::before {
        content: '💊';
        position: absolute;
        right: 10px;
        top: 50%;
        transform: translateY(-50%);
        font-size: 1rem;
        animation: pillFloat 4s ease-in-out infinite;
    }
    
    @keyframes pillFloat {
        0%, 100% { transform: translateY(-50%) rotate(0deg); }
        50% { transform: translateY(-55%) rotate(180deg); }
    }
    
    /* Enhanced Radio Button Styling */
    .stRadio > div {
        background: linear-gradient(135deg, rgba(70, 130, 180, 0.7), rgba(100, 149, 237, 0.6), rgba(135, 206, 250, 0.5)) !important;
        border-radius: 12px !important;
        padding: 1rem !important;
        border: 2px solid rgba(255, 255, 255, 0.4) !important;
        transition: all 0.3s ease !important;
        backdrop-filter: blur(10px) !important;
        box-shadow: 0 4px 12px rgba(70, 130, 180, 0.3) !important;
        margin-bottom: 0.8rem !important;
    }
    
    .stRadio > div:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(70, 130, 180, 0.4) !important;
        border-color: rgba(255, 255, 255, 0.6) !important;
        background: linear-gradient(135deg, rgba(70, 130, 180, 0.8), rgba(100, 149, 237, 0.7), rgba(135, 206, 250, 0.6)) !important;
    }
    
    .stRadio > div > label {
        display: flex !important;
        align-items: center !important;
        padding: 0.5rem !important;
        font-weight: 600 !important;
        color: #ffffff !important;
        cursor: pointer !important;
        text-shadow: 0 1px 2px rgba(0,0,0,0.3) !important;
    }
    
    .stRadio > div > label > div:first-child {
        margin-right: 0.8rem !important;
    }
    
    /* Radio button circle styling */
    .stRadio input[type="radio"] {
        width: 18px !important;
        height: 18px !important;
        margin-right: 0.8rem !important;
        accent-color: #ffffff !important;
    }
    
    /* Enhanced Number Input Styling */
    .stNumberInput > div > div {
        background: rgba(255, 255, 255, 0.9) !important;
        border-radius: 12px !important;
        border: 2px solid rgba(255, 255, 255, 0.3) !important;
        transition: all 0.3s ease !important;
        backdrop-filter: blur(10px) !important;
        box-shadow: 0 4px 12px rgba(0, 51, 102, 0.1) !important;
    }
    
    .stNumberInput > div > div > input {
        color: #003366 !important;
        font-weight: 600 !important;
        background: transparent !important;
        border: none !important;
    }
    
    .stNumberInput > div > div:hover,
    .stNumberInput > div > div:focus-within {
        border-color: white !important;
        box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.3) !important;
        transform: translateY(-2px) !important;
    }
    
    /* Enhanced Selectbox Styling */
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.9) !important;
        border-radius: 12px !important;
        border: 2px solid rgba(255, 255, 255, 0.3) !important;
        transition: all 0.3s ease !important;
        backdrop-filter: blur(10px) !important;
        box-shadow: 0 4px 12px rgba(0, 51, 102, 0.1) !important;
    }
    
    .stSelectbox > div > div:hover,
    .stSelectbox > div > div:focus-within {
        border-color: white !important;
        box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.3) !important;
        transform: translateY(-2px) !important;
    }
    
    .stNumberInput > div > div:hover {
        border-color: rgba(0, 102, 204, 0.4) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(0, 102, 204, 0.2) !important;
    }
    
    .stNumberInput > div > div:focus-within {
        border-color: #0066cc !important;
        box-shadow: 0 0 0 3px rgba(0, 102, 204, 0.1) !important;
    }
    
    /* Enhanced Select Box Styling */
    .stSelectbox > div > div {
        background: linear-gradient(135deg, rgba(255,255,255,0.98) 0%, rgba(248,252,255,0.95) 100%) !important;
        border-radius: 12px !important;
        border: 2px solid rgba(0, 102, 204, 0.25) !important;
        transition: all 0.3s ease !important;
        backdrop-filter: blur(10px) !important;
        box-shadow: 0 4px 12px rgba(0, 102, 204, 0.1) !important;
    }
    
    .stSelectbox > div > div:hover {
        border-color: rgba(0, 102, 204, 0.4) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(0, 102, 204, 0.2) !important;
    }
    
    /* Enhanced Metric Styling */
    .stMetric {
        background: linear-gradient(135deg, rgba(0, 102, 204, 0.08) 0%, rgba(77, 166, 255, 0.05) 100%) !important;
        border-radius: 12px !important;
        padding: 1rem !important;
        border: 2px solid rgba(0, 102, 204, 0.2) !important;
        transition: all 0.3s ease !important;
        backdrop-filter: blur(10px) !important;
        box-shadow: 0 4px 12px rgba(0, 102, 204, 0.1) !important;
    }
    
    .stMetric:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(0, 102, 204, 0.15) !important;
    }
    
    /* Enhanced Form Layout with Prominent Border */
    .stForm {
        margin: 2rem 0 !important;
        padding: 3rem !important;
        border: 4px solid transparent !important;
        border-radius: 25px !important;
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.98), rgba(240, 248, 255, 0.95)) !important;
        box-shadow: 
            0 0 30px rgba(0, 102, 204, 0.4),
            0 0 60px rgba(0, 102, 204, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 0.8) !important;
        position: relative !important;
        transition: all 0.4s ease !important;
        backdrop-filter: blur(15px) !important;
    }
    
    .stForm::before {
        content: '' !important;
        position: absolute !important;
        top: -4px !important;
        left: -4px !important;
        right: -4px !important;
        bottom: -4px !important;
        background: linear-gradient(45deg, 
            #ff6b6b, #4ecdc4, #45b7d1, #96ceb4, 
            #ffeaa7, #dda0dd, #98d8c8, #f7dc6f) !important;
        background-size: 400% 400% !important;
        border-radius: 25px !important;
        z-index: -1 !important;
        animation: gradientShift 3s ease infinite !important;
    }
    
    .stForm:hover {
        transform: translateY(-3px) !important;
        box-shadow: 
            0 0 40px rgba(0, 102, 204, 0.6),
            0 0 80px rgba(0, 102, 204, 0.3),
            inset 0 1px 0 rgba(255, 255, 255, 0.9) !important;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .stForm > div {
        gap: 1rem !important;
    }
    
    /* Remove extra spacing */
    .main .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
    }
    
    /* Label styling */
    .stRadio label, .stNumberInput label, .stSelectbox label {
        font-weight: 700 !important;
        color: #003366 !important;
        margin-bottom: 0.8rem !important;
        font-size: 1.1rem !important;
        text-shadow: 0 1px 2px rgba(0,0,0,0.1) !important;
        display: block !important;
    }
    
    /* Radio button question text styling */
    .stRadio > div > label > div:last-child {
        font-weight: 800 !important;
        color: #ffffff !important;
        font-size: 1rem !important;
        text-shadow: 0 1px 2px rgba(0,0,0,0.4) !important;
    }
    
    .feature-importance {
        background: linear-gradient(135deg, #0066cc, #0080ff, #4da6ff);
        background-size: 200% 200%;
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        border: 3px solid rgba(255,255,255,0.3);
        box-shadow: 0 20px 40px rgba(0, 102, 204, 0.3);
        animation: importanceGlow 6s ease-in-out infinite;
        position: relative;
        overflow: hidden;
    }
    
    @keyframes importanceGlow {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .feature-importance::before {
        content: '🧠📊🔬⚡';
        position: absolute;
        top: 15px;
        right: 20px;
        font-size: 1.5rem;
        animation: brainPulse 3s ease-in-out infinite;
    }
    
    @keyframes brainPulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.2); }
    }
    
    /* Footer styling */
    .footer-container {
        background: linear-gradient(135deg, #0066cc, #0080ff, #4da6ff);
        border-radius: 20px;
        margin-top: 2rem;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 15px 30px rgba(0, 102, 204, 0.3);
        border: 2px solid rgba(255,255,255,0.3);
        position: relative;
        overflow: hidden;
    }
    
    .footer-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        animation: footerShine 4s infinite;
    }
    
    @keyframes footerShine {
        0% { left: -100%; }
        100% { left: 100%; }
    }
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 12px;
    }
    
    ::-webkit-scrollbar-track {
        background: linear-gradient(45deg, #b3d9ff, #e6f3ff);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(45deg, #0066cc, #4da6ff);
        border-radius: 10px;
        border: 2px solid rgba(255,255,255,0.3);
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(45deg, #0052a3, #0080ff);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add floating elements
st.markdown(
    """
    <div class="floating-elements">
        <div class="floating-icon">🩺</div>
        <div class="floating-icon">💊</div>
        <div class="floating-icon">🔬</div>
        <div class="floating-icon">❤️</div>
        <div class="floating-icon">⚕️</div>
        <div class="floating-icon">👨‍⚕️</div>
        <div class="floating-icon">👩‍⚕️</div>
        <div class="floating-icon">🏥</div>
        <div class="floating-icon">💉</div>
        <div class="floating-icon">🧬</div>
    </div>
    """,
    unsafe_allow_html=True
)

# Main title with VinBig logo
# st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Add VinBig logo header with medical decorations
if vinbig_logo_base64:
    st.markdown(
        f"""
        <div style="text-align: center; margin-bottom: 2rem; position: relative; animation: logoFloat 6s ease-in-out infinite;">
            <div style="display: inline-flex; align-items: center; justify-content: center; gap: 2rem; padding: 1.5rem; background: linear-gradient(135deg, rgba(255,255,255,0.95), rgba(240,248,255,0.9)); border-radius: 25px; box-shadow: 0 20px 40px rgba(0,102,204,0.2); border: 3px solid rgba(0,102,204,0.3); backdrop-filter: blur(15px);">
                <div style="font-size: 3rem; animation: medicalIcons 4s ease-in-out infinite;">👨‍⚕️</div>
                <img src="data:image/png;base64,{vinbig_logo_base64}" 
                     style="height: 80px; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,102,204,0.3); animation: logoGlow 3s ease-in-out infinite;" 
                     alt="VinBig Logo"/>
                <div style="font-size: 3rem; animation: medicalIcons 4s ease-in-out infinite 2s;">👩‍⚕️</div>
            </div>
            <div style="margin-top: 1rem; display: flex; justify-content: center; gap: 1.5rem; font-size: 2rem;">
                <span style="animation: float 3s ease-in-out infinite;">🏥</span>
                <span style="animation: float 3s ease-in-out infinite 0.5s;">⚕️</span>
                <span style="animation: float 3s ease-in-out infinite 1s;">🩺</span>
                <span style="animation: float 3s ease-in-out infinite 1.5s;">💊</span>
                <span style="animation: float 3s ease-in-out infinite 2s;">🔬</span>
            </div>
        </div>
        <style>
        @keyframes logoFloat {{
            0%, 100% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-10px); }}
        }}
        @keyframes logoGlow {{
            0%, 100% {{ filter: brightness(1) drop-shadow(0 0 10px rgba(0,102,204,0.3)); }}
            50% {{ filter: brightness(1.1) drop-shadow(0 0 20px rgba(0,102,204,0.6)); }}
        }}
        @keyframes medicalIcons {{
            0%, 100% {{ transform: scale(1) rotate(0deg); }}
            25% {{ transform: scale(1.1) rotate(5deg); }}
            50% {{ transform: scale(1.2) rotate(0deg); }}
            75% {{ transform: scale(1.1) rotate(-5deg); }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    # Fallback with just medical decorations if logo not found
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 2rem; position: relative; animation: logoFloat 6s ease-in-out infinite;">
            <div style="display: inline-flex; align-items: center; justify-content: center; gap: 2rem; padding: 1.5rem; background: linear-gradient(135deg, rgba(255,255,255,0.95), rgba(240,248,255,0.9)); border-radius: 25px; box-shadow: 0 20px 40px rgba(0,102,204,0.2); border: 3px solid rgba(0,102,204,0.3); backdrop-filter: blur(15px);">
                <div style="font-size: 4rem; animation: medicalIcons 4s ease-in-out infinite;">👨‍⚕️</div>
                <div style="font-size: 3rem; font-weight: 900; background: linear-gradient(45deg, #003366, #0066cc, #0080ff, #4da6ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: titleFlow 4s ease-in-out infinite;">VinBig AI</div>
                <div style="font-size: 4rem; animation: medicalIcons 4s ease-in-out infinite 2s;">👩‍⚕️</div>
            </div>
            <div style="margin-top: 1rem; display: flex; justify-content: center; gap: 1.5rem; font-size: 2rem;">
                <span style="animation: float 3s ease-in-out infinite;">🏥</span>
                <span style="animation: float 3s ease-in-out infinite 0.5s;">⚕️</span>
                <span style="animation: float 3s ease-in-out infinite 1s;">🩺</span>
                <span style="animation: float 3s ease-in-out infinite 1.5s;">💊</span>
                <span style="animation: float 3s ease-in-out infinite 2s;">🔬</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('<h1 class="medical-title">🩺 Diabetes Doctor</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">AI-Powered Diabetes Risk Assessment | Trusted Medical Consultation</p>', unsafe_allow_html=True)

# Doctor introduction with enhanced styling
st.markdown(
    """
    <div class="doctor-badge">
        <h3 style="color: #ffffff; margin: 0 0 1rem 0; font-weight: 700; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">
            🏥 Chào mừng đến với Diabetes Doctor
        </h3>
        <p style="margin: 0; color: #ffffff; line-height: 1.8; font-weight: 500; text-shadow: 0 1px 2px rgba(0,0,0,0.2);">
            Hệ thống AI tiên tiến được phát triển bởi các chuyên gia y tế, sử dụng thuật toán K-Nearest Neighbors 
            để đánh giá nguy cơ mắc bệnh tiểu đường. Vui lòng điền đầy đủ thông tin để nhận được tư vấn chính xác nhất.
        </p>
        <div style="margin-top: 1.5rem; padding: 1rem; background: rgba(255,255,255,0.1); border-radius: 10px; border-left: 4px solid #4da6ff; animation: pulse 3s ease-in-out infinite;">
            <p style="margin: 0; color: #ffffff; font-style: italic; font-weight: 600; text-align: center; text-shadow: 0 1px 2px rgba(0,0,0,0.2);">
                💡 "Phòng bệnh hơn chữa bệnh - Kiểm tra sức khỏe định kỳ để bảo vệ tương lai"
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Create form
with st.form("diabetes_assessment_form"):
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 2rem; padding: 1.5rem; background: linear-gradient(135deg, rgba(0, 102, 204, 0.1), rgba(77, 166, 255, 0.05)); border-radius: 15px; border: 2px solid rgba(0, 102, 204, 0.2);">
            <h2 style="color: #003366; font-weight: 800; font-size: 1.8rem; margin-bottom: 0.5rem; text-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                🩺 Đái Tháo Đường - Đừng coi thường
            </h2>
            <p style="color: #0066cc; font-weight: 600; font-size: 1.1rem; margin: 0; font-style: italic;">
                Phát hiện sớm - Điều trị kịp thời - Sống khỏe mạnh
            </p>
            <div style="margin-top: 1rem; display: flex; justify-content: center; gap: 1rem; font-size: 1.5rem;">
                <span style="animation: heartbeat 2s infinite;">❤️</span>
                <span style="animation: heartbeat 2s infinite 0.5s;">💪</span>
                <span style="animation: heartbeat 2s infinite 1s;">🏃‍♂️</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Section 1: Basic Health Indicators
    if doctor_1_base64:
        section_bg_style = f"background-image: url('data:image/png;base64,{doctor_1_base64}'); background-size: cover; background-position: center; background-repeat: no-repeat; background-attachment: fixed;"
    else:
        section_bg_style = "background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(240, 248, 255, 0.9) 100%);"
    
    st.markdown(
        f"""
        <div class="form-section" style="{section_bg_style}">
            <div class="section-title" style="animation: blink 3s infinite; font-weight: 800; font-size: 1.6em;">
                🩺 Các chỉ số sức khỏe cơ bản
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        high_bp = st.radio(
            "Có bị cao huyết áp không?",
            options=[0, 1],
            format_func=lambda x: "Không" if x == 0 else "Có",
            key="high_bp"
        )
        st.markdown('<div class="medical-info">Huyết áp > 140/90 mmHg</div>', unsafe_allow_html=True)
    
    with col2:
        high_chol = st.radio(
            "Có bị cholesterol cao không?",
            options=[0, 1],
            format_func=lambda x: "Không" if x == 0 else "Có",
            key="high_chol"
        )
        st.markdown('<div class="medical-info">Cholesterol toàn phần > 240 mg/dL</div>', unsafe_allow_html=True)
    
    with col3:
        chol_check = st.radio(
            "Đã kiểm tra cholesterol trong 5 năm qua?",
            options=[0, 1],
            format_func=lambda x: "Không" if x == 0 else "Có",
            key="chol_check"
        )
        st.markdown('<div class="medical-info">Khuyến nghị kiểm tra định kỳ</div>', unsafe_allow_html=True)
    
    # BMI Input Section with Height and Weight
    if doctor_2_base64:
        section_bg_style_2 = f"background-image: url('data:image/png;base64,{doctor_2_base64}'); background-size: cover; background-position: center; background-repeat: no-repeat; background-attachment: fixed;"
    else:
        section_bg_style_2 = "background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(240, 248, 255, 0.9) 100%);"
    
    st.markdown(
        f"""
        <div class="form-section" style="{section_bg_style_2}">
            <div class="section-title" style="animation: blink 3s infinite; font-weight: 800; font-size: 1.6em;">
                📊 Thông tin cơ thể và BMI
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        height = st.number_input(
            "Chiều cao (cm)",
            min_value=100.0,
            max_value=250.0,
            value=170.0,
            step=0.5,
            key="height",
            help="Nhập chiều cao của bạn bằng cm"
        )
        st.markdown('<div class="medical-info">Chiều cao trung bình: Nam 168cm, Nữ 158cm</div>', unsafe_allow_html=True)
    
    with col2:
        weight = st.number_input(
            "Cân nặng (kg)",
            min_value=30.0,
            max_value=200.0,
            value=65.0,
            step=0.1,
            key="weight",
            help="Nhập cân nặng của bạn bằng kg"
        )
        st.markdown('<div class="medical-info">Cân nặng khỏe mạnh phụ thuộc vào chiều cao</div>', unsafe_allow_html=True)
    
    with col3:
        # Calculate BMI automatically
        if height > 0:
            bmi = weight / ((height/100) ** 2)
        else:
            bmi = 0
        
        st.metric(
            label="BMI tự động tính",
            value=f"{bmi:.1f}",
            help="BMI được tính từ cân nặng và chiều cao"
        )
        
        # BMI interpretation with enhanced styling
        if bmi < 18.5:
            bmi_status = "Thiếu cân"
            bmi_color = "#0066cc"
            bmi_icon = "⬇️"
        elif bmi < 25:
            bmi_status = "Bình thường"
            bmi_color = "#00cc66"
            bmi_icon = "✅"
        elif bmi < 30:
            bmi_status = "Thừa cân"
            bmi_color = "#ffaa00"
            bmi_icon = "⚠️"
        else:
            bmi_status = "Béo phì"
            bmi_color = "#ff4444"
            bmi_icon = "🚨"
        
        st.markdown(
            f'''
            <div class="medical-info" style="border-left-color: {bmi_color}; background: linear-gradient(135deg, {bmi_color}20, {bmi_color}10);">
                {bmi_icon} <strong>Phân loại BMI: {bmi_status}</strong>
            </div>
            ''',
            unsafe_allow_html=True
        )
    
    # Section 2: Lifestyle Factors
    if doctor_3_base64:
        section_bg_style_3 = f"background-image: url('data:image/png;base64,{doctor_3_base64}'); background-size: cover; background-position: center; background-repeat: no-repeat; background-attachment: fixed;"
    else:
        section_bg_style_3 = "background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(240, 248, 255, 0.9) 100%);"
    
    st.markdown(
        f"""
        <div class="form-section" style="{section_bg_style_3}">
            <div class="section-title" style="animation: blink 3s infinite; font-weight: 800; font-size: 1.6em;">
                🚭 Lối sống và thói quen
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        smoker = st.radio(
            "Có hút thuốc không?",
            options=[0, 1],
            format_func=lambda x: "Không" if x == 0 else "Có",
            key="smoker"
        )
    
    with col2:
        phys_activity = st.radio(
            "Có tập thể dục thường xuyên không?",
            options=[0, 1],
            format_func=lambda x: "Không" if x == 0 else "Có",
            key="phys_activity"
        )
    
    with col3:
        hvy_alcohol = st.radio(
            "Có uống nhiều rượu bia không?",
            options=[0, 1],
            format_func=lambda x: "Không" if x == 0 else "Có",
            key="hvy_alcohol"
        )
    
    # Section 3: Medical History
    if doctor_4_base64:
        section_bg_style_4 = f"background-image: url('data:image/png;base64,{doctor_4_base64}'); background-size: cover; background-position: center; background-repeat: no-repeat; background-attachment: fixed;"
    else:
        section_bg_style_4 = "background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(240, 248, 255, 0.9) 100%);"
    
    st.markdown(
        f"""
        <div class="form-section" style="{section_bg_style_4}">
            <div class="section-title" style="animation: blink 3s infinite; font-weight: 800; font-size: 1.6em;">
                🫀 Tiền sử bệnh lý
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        stroke = st.radio(
            "Đã từng bị đột quỵ không?",
            options=[0, 1],
            format_func=lambda x: "Không" if x == 0 else "Có",
            key="stroke"
        )
        
        heart_disease = st.radio(
            "Có bệnh tim mạch không?",
            options=[0, 1],
            format_func=lambda x: "Không" if x == 0 else "Có",
            key="heart_disease"
        )
    
    with col2:
        any_healthcare = st.radio(
            "Có bảo hiểm y tế không?",
            options=[0, 1],
            format_func=lambda x: "Không" if x == 0 else "Có",
            key="any_healthcare"
        )
        
        no_doc_cost = st.radio(
            "Đã từng không đi khám vì chi phí cao?",
            options=[0, 1],
            format_func=lambda x: "Không" if x == 0 else "Có",
            key="no_doc_cost"
        )
    
    # Section 4: Nutrition and Health Status
    if doctor_5_base64:
        section_bg_style_5 = f"background-image: url('data:image/png;base64,{doctor_5_base64}'); background-size: cover; background-position: center; background-repeat: no-repeat; background-attachment: fixed;"
    else:
        section_bg_style_5 = "background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(240, 248, 255, 0.9) 100%);"
    
    st.markdown(
        f"""
        <div class="form-section" style="{section_bg_style_5}">
            <div class="section-title" style="animation: blink 3s infinite; font-weight: 800; font-size: 1.6em;">
                🥗 Dinh dưỡng và tình trạng sức khỏe
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        fruits = st.radio(
            "Có ăn trái cây hàng ngày không?",
            options=[0, 1],
            format_func=lambda x: "Không" if x == 0 else "Có",
            key="fruits"
        )
    
    with col2:
        veggies = st.radio(
            "Có ăn rau hàng ngày không?",
            options=[0, 1],
            format_func=lambda x: "Không" if x == 0 else "Có",
            key="veggies"
        )
    
    with col3:
        gen_hlth = st.selectbox(
            "Đánh giá sức khỏe tổng quát",
            options=[1, 2, 3, 4, 5],
            format_func=lambda x: {1: "Xuất sắc", 2: "Rất tốt", 3: "Tốt", 4: "Khá", 5: "Kém"}[x],
            key="gen_hlth"
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Motivational Quote before submit
    st.markdown(
        """
        <div style="text-align: center; margin: 2rem 0; padding: 1.2rem; background: linear-gradient(135deg, rgba(0, 153, 255, 0.1), rgba(0, 204, 153, 0.1)); border-radius: 12px; border: 1px solid rgba(0, 153, 255, 0.3);">
            <p style="color: #003366; font-weight: 700; font-size: 1.1rem; margin: 0; animation: pulse 4s ease-in-out infinite;">
                🌟 "Sức khỏe là tài sản quý giá nhất - Hãy chăm sóc nó mỗi ngày!" 🌟
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Submit button
    submitted = st.form_submit_button("🔍 Phân tích nguy cơ tiểu đường")

# Process form submission
if submitted:
    # Prepare data for prediction
    user_data = {
        'HighBP': high_bp,
        'HighChol': high_chol,
        'CholCheck': chol_check,
        'BMI': bmi,
        'Smoker': smoker,
        'Stroke': stroke,
        'HeartDiseaseorAttack': heart_disease,
        'PhysActivity': phys_activity,
        'Fruits': fruits,
        'Veggies': veggies,
        'HvyAlcoholConsump': hvy_alcohol,
        'AnyHealthcare': any_healthcare,
        'NoDocbcCost': no_doc_cost,
        'GenHlth': gen_hlth
    }
    
    with st.spinner('🔬 Đang phân tích dữ liệu y tế...'):
        try:
            # Send request to server
            response = requests.post(
                'http://localhost:5002/predict',
                json=user_data,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                prediction = result['prediction']
                probability = result['probability']
                
                # Display results
                if prediction == 1:
                    st.markdown(
                        f"""
                        <div class="prediction-card high-risk">
                            <div class="risk-icon">⚠️</div>
                            <div class="prediction-text" style="color: #dc2626;">
                                Nguy cơ cao mắc bệnh tiểu đường
                            </div>
                            <div class="confidence-bar">
                                <div class="confidence-fill" style="width: {probability*100:.1f}%; background: linear-gradient(90deg, #ef4444, #dc2626);"></div>
                            </div>
                            <p style="color: #7f1d1d; margin: 0;">Độ tin cậy: {probability*100:.1f}%</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    
                    st.markdown(
                        """
                        <div class="medical-advice">
                            <h4 style="color: #ffffff; margin: 0 0 1rem 0; font-weight: 700; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">🏥 Khuyến nghị y tế:</h4>
                            <ul style="color: #ffffff; margin: 0; padding-left: 1.5rem; font-weight: 500; text-shadow: 0 1px 2px rgba(0,0,0,0.2);">
                                <li>Nên đến gặp bác sĩ chuyên khoa nội tiết để kiểm tra chi tiết</li>
                                <li>Thực hiện xét nghiệm đường huyết đói và HbA1c</li>
                                <li>Điều chỉnh chế độ ăn uống, tăng cường vận động</li>
                                <li>Theo dõi cân nặng và huyết áp thường xuyên</li>
                                <li>Tránh stress và duy trì lối sống lành mạnh</li>
                            </ul>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        f"""
                        <div class="prediction-card low-risk">
                            <div class="risk-icon">✅</div>
                            <div class="prediction-text" style="color: #16a34a;">
                                Nguy cơ thấp mắc bệnh tiểu đường
                            </div>
                            <div class="confidence-bar">
                                <div class="confidence-fill" style="width: {(1-probability)*100:.1f}%; background: linear-gradient(90deg, #22c55e, #16a34a);"></div>
                            </div>
                            <p style="color: #14532d; margin: 0;">Độ tin cậy: {(1-probability)*100:.1f}%</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    
                    st.markdown(
                        """
                        <div class="medical-advice">
                            <h4 style="color: #ffffff; margin: 0 0 1rem 0; font-weight: 700; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">🌟 Khuyến nghị duy trì sức khỏe:</h4>
                            <ul style="color: #ffffff; margin: 0; padding-left: 1.5rem; font-weight: 500; text-shadow: 0 1px 2px rgba(0,0,0,0.2);">
                                <li>Tiếp tục duy trì lối sống lành mạnh hiện tại</li>
                                <li>Kiểm tra sức khỏe định kỳ 6-12 tháng/lần</li>
                                <li>Duy trì BMI trong khoảng bình thường (18.5-24.9)</li>
                                <li>Tập thể dục ít nhất 150 phút/tuần</li>
                                <li>Ăn nhiều rau xanh, trái cây và hạn chế đường</li>
                            </ul>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                
                # Feature importance explanation
                st.markdown(
                    """
                    <div class="feature-importance">
                        <h4 style="color: #ffffff; margin: 0 0 1rem 0; font-weight: 700; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">📊 Các yếu tố quan trọng trong đánh giá:</h4>
                        <p style="color: #ffffff; margin: 0; line-height: 1.8; font-weight: 500; text-shadow: 0 1px 2px rgba(0,0,0,0.2);">
                            Model AI đã phân tích các yếu tố chính: <strong>BMI, tình trạng sức khỏe tổng quát, 
                            cao huyết áp, cholesterol cao, hoạt động thể chất</strong> và các yếu tố khác 
                            để đưa ra kết quả dự đoán chính xác nhất.
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
            else:
                st.error(f"❌ Lỗi khi gửi dữ liệu: {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            st.error("❌ Không thể kết nối đến server. Vui lòng đảm bảo server đang chạy trên port 5002.")
        except requests.exceptions.Timeout:
            st.error("❌ Quá thời gian chờ phản hồi. Vui lòng thử lại.")
        except Exception as e:
            st.error(f"❌ Lỗi không xác định: {str(e)}")

# Footer with enhanced styling
st.markdown(
    """
    <div class="footer-container">
        <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
            <div style="font-size: 2rem; margin: 0 1rem;">🏥</div>
            <div style="font-size: 2rem; margin: 0 1rem;">👨‍⚕️</div>
            <div style="font-size: 2rem; margin: 0 1rem;">👩‍⚕️</div>
            <div style="font-size: 2rem; margin: 0 1rem;">💊</div>
            <div style="font-size: 2rem; margin: 0 1rem;">🔬</div>
        </div>
        <p style="color: #ffffff; margin: 0; font-size: 1rem; font-weight: 600; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">
            ⚠️ <strong>Lưu ý quan trọng:</strong> Kết quả này chỉ mang tính chất tham khảo. 
            Không thay thế cho việc thăm khám và tư vấn trực tiếp từ bác sĩ chuyên khoa.
        </p>
        <p style="color: rgba(255,255,255,0.8); margin: 1rem 0 0 0; font-size: 0.9em; font-weight: 500;">
            © 2024 Diabetes Doctor - Powered by AI & Medical Expertise ✨
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)
