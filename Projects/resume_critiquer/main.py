import streamlit as st
import PyPDF2
import io
import os
import google.generativeai as genai
from dotenv import load_dotenv
import time

load_dotenv()

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap');

    .main {
        padding: 2rem;
        font-family: 'Inter', sans-serif;
        background: linear-gradient(135deg, #f5f7ff 0%, #ffffff 100%);
    }
    .stApp {
        max-width: 1100px;
        margin: 0 auto;
    }
    .upload-section {
        padding: 3rem;
        border-radius: 20px;
        border: 1px solid rgba(75, 93, 255, 0.1);
        margin: 2rem 0;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.12);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .upload-section:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(75, 93, 255, 0.15);
        border: 1px solid rgba(75, 93, 255, 0.2);
    }
    .header-section {
        background: linear-gradient(135deg, #4B5DFF 0%, #6772FF 50%, #837DFF 100%);
        padding: 4rem 2rem;
        border-radius: 24px;
        color: white;
        margin-bottom: 3rem;
        box-shadow: 0 15px 35px rgba(75, 93, 255, 0.2);
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    .header-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 100%);
        z-index: 1;
    }
    .analysis-section {
        background: rgba(255, 255, 255, 0.95);
        padding: 3rem;
        border-radius: 20px;
        margin-top: 2rem;
        border-left: 5px solid #4B5DFF;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        backdrop-filter: blur(10px);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .analysis-section:hover {
        box-shadow: 0 15px 35px rgba(75, 93, 255, 0.15);
    }
    .stButton>button {
        background: linear-gradient(135deg, #4B5DFF, #6772FF);
        color: white;
        border: none;
        padding: 1rem 2rem;
        border-radius: 12px;
        font-weight: 600;
        letter-spacing: 0.5px;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 15px rgba(75, 93, 255, 0.2);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(75, 93, 255, 0.3);
        background: linear-gradient(135deg, #6772FF, #837DFF);
    }
    .step-card {
        background: rgba(255, 255, 255, 0.95);
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        backdrop-filter: blur(10px);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        height: 100%;
        border: 1px solid rgba(75, 93, 255, 0.1);
    }
    .step-card:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 15px 35px rgba(75, 93, 255, 0.15);
        border: 1px solid rgba(75, 93, 255, 0.2);
    }
    h1 {
        font-family: 'Poppins', sans-serif;
        font-weight: 700 !important;
        margin-bottom: 1.5rem !important;
        font-size: 2.5rem !important;
        background: linear-gradient(to right, #FFFFFF, #E8EAFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .caption-text {
        opacity: 0.9;
        font-size: 0.95rem;
        line-height: 1.5;
        color: #4a5568;
    }
    .stProgress > div > div {
        background: linear-gradient(to right, #4B5DFF, #837DFF);
        border-radius: 10px;
    }
    .success-message {
        padding: 1.2rem;
        border-radius: 12px;
        background: linear-gradient(135deg, #E8F5E9, #F1F8E9);
        border-left: 5px solid #4CAF50;
        margin: 1.5rem 0;
        box-shadow: 0 4px 15px rgba(76, 175, 80, 0.1);
    }
    .file-uploader {
        border: 2px dashed rgba(75, 93, 255, 0.2);
        border-radius: 12px;
        padding: 2rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    .file-uploader:hover {
        border-color: #4B5DFF;
        background: rgba(75, 93, 255, 0.05);
    }
    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #4B5DFF, #6772FF);
        border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #6772FF, #837DFF);
    }
</style>
""", unsafe_allow_html=True)

# Header Section with enhanced design
st.markdown('<div class="header-section">', unsafe_allow_html=True)
st.title("✨ AI Resume Critiquer")
st.markdown("""
<p style='font-size: 1.3rem; margin-top: 1.5rem; opacity: 0.9; line-height: 1.6;'>
Transform your resume into a powerful career tool with AI-powered insights and personalized recommendations
</p>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

# Enhanced File upload section
st.markdown('<div class="upload-section">', unsafe_allow_html=True)
col1, col2 = st.columns([3, 2])
with col1:
    st.markdown('<div class="file-uploader">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("📄 Drop your resume here", type=["pdf", "txt"])
    if uploaded_file:
        st.success(f"✨ Successfully uploaded: {uploaded_file.name}")
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown("""
    <h4 style='color: #4B5DFF; margin-bottom: 1rem;'>Target Position</h4>
    """, unsafe_allow_html=True)
    job_role = st.text_input("🎯 Enter your desired role", placeholder="e.g., Software Engineer")
    analyze = st.button("🔍 Analyze Resume", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")

if analyze and uploaded_file:
    try:
        with st.spinner('🤖 Analyzing your resume...'):
            file_content = extract_text_from_file(uploaded_file)
            
            if not file_content.strip():
                st.error("❌ File appears to be empty...")
                st.stop()
            
            # Animated progress
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)  # Smooth animation
                progress_bar.progress(i + 1)
            
            prompt = f"""Please analyze this resume and provide constructive feedback. 
            Focus on the following aspects:
            1. Content clarity and impact
            2. Skills presentation
            3. Experience descriptions
            4. Specific improvements for {job_role if job_role else 'general job applications'}
            
            Resume content:
            {file_content}
            
            Please provide your analysis in a clear, structured format with specific recommendations.
            Use markdown formatting for better readability."""
            
            # Generate response using Gemini
            response = model.generate_content(prompt)
            
            # Display results with animation
            st.markdown('<div class="analysis-section">', unsafe_allow_html=True)
            st.markdown("""
            <h3 style='color: #4B5DFF; margin-bottom: 1.5rem;'>
                📊 Analysis Results
            </h3>
            """, unsafe_allow_html=True)
            st.markdown("---")
            st.markdown(response.text)
            st.markdown('</div>', unsafe_allow_html=True)
            
            progress_bar.empty()
            
            # Enhanced success message
            st.markdown("""
            <div class='success-message'>
                ✅ Analysis completed successfully! Review the detailed feedback above.
            </div>
            """, unsafe_allow_html=True)
    
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")

# Enhanced footer
st.markdown("---")
st.markdown("""
<div class='footer-section' style='background: rgba(255, 255, 255, 0.95); padding: 3rem; border-radius: 20px; box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);'>
    <h3 style='color: #4B5DFF; margin-bottom: 2.5rem; font-family: Poppins, sans-serif;'>How It Works</h3>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class='step-card'>
        <h4 style='color: #4B5DFF; margin-bottom: 1rem;'>1. 📤 Upload Resume</h4>
        <p class='caption-text'>Simply drag and drop your PDF or TXT format resume for instant analysis</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class='step-card'>
        <h4 style='color: #4B5DFF; margin-bottom: 1rem;'>2. 🎯 Define Your Goal</h4>
        <p class='caption-text'>Specify your target role for tailored recommendations</p>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class='step-card'>
        <h4 style='color: #4B5DFF; margin-bottom: 1rem;'>3. 🤖 Get Expert Insights</h4>
        <p class='caption-text'>Receive detailed AI analysis and actionable improvements</p>
    </div>
    """, unsafe_allow_html=True)

# Enhanced footer note
st.markdown("""
<div style='text-align: center; margin-top: 4rem; padding: 2rem;'>
    <p style='opacity: 0.8; font-size: 0.9rem; line-height: 1.5;'>
        Made with 💙 using Streamlit and Gemini AI<br>
        <span style='opacity: 0.6; font-size: 0.8rem;'>Elevate your career prospects with AI-powered resume analysis</span>
    </p>
</div>
""", unsafe_allow_html=True)