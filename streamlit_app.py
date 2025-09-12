import streamlit as st
from main import create_blog
import os
from dotenv import load_dotenv

load_dotenv()

# Page config
st.set_page_config(
    page_title="AI Blog Research Generator",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional CSS - Compact Design with Black Sidebar
st.markdown("""
<style>
    /* Main app styling */
    .stApp { 
        background-color: #ffffff; 
        color: #2c3e50; 
    }
    .main { 
        background-color: #ffffff; 
        color: #2c3e50;
        padding-top: 1rem !important;
    }
    
    /* Header styling - Compact */
    .header-box {
        background: linear-gradient(135deg, #f8f9fa, #e9ecef);
        padding: 1rem 1.5rem;
        border-radius: 10px;
        margin-bottom: 1.5rem;
        border: 1px solid #dee2e6;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        display: flex;
        align-items: center;
        gap: 15px;
    }
    
    .title { 
        color: #2c3e50; 
        font-size: 1.8rem; 
        font-weight: 800;
        margin: 0;
    }
    
    .subtitle { 
        color: #6c757d; 
        font-size: 0.9rem; 
        margin-top: 0.3rem;
    }
    
    /* Sidebar styling - Black like Clinical Protocol */
    .css-1d391kg {
        background-color: #1a1a1a !important;
    }
    
    .css-1544g2n {
        background-color: #1a1a1a !important;
        border-right: 1px solid #333 !important;
        padding-top: 1rem !important;
    }
    
    /* Sidebar header */
    .css-1544g2n h3 {
        color: #ffffff !important;
        font-size: 1.1rem !important;
        margin-bottom: 1rem !important;
        padding-left: 0.5rem !important;
    }
    
    /* Sidebar buttons - White with rounded corners */
    .css-1544g2n .stButton button {
        background-color: #ffffff !important;
        color: #2c3e50 !important;
        border: none !important;
        border-radius: 8px !important;
        width: 100% !important;
        margin-bottom: 0.5rem !important;
        padding: 0.6rem 1rem !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1) !important;
    }
    
    .css-1544g2n .stButton button:hover {
        background-color: #f8f9fa !important;
        color: #007bff !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15) !important;
    }
    
    /* Content boxes - Compact */
    .content-box {
        background: linear-gradient(145deg, #ffffff, #f8f9fa);
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #e9ecef;
        margin: 0.5rem 0;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        height: fit-content;
    }
    
    /* Output box styling - Fixed with proper containment */
    .output-box {
        background: #ffffff;
        border: 1px solid #dee2e6;
        border-radius: 8px;
        padding: 1.5rem;
        min-height: 400px;
        max-height: 600px;
        overflow-y: auto;
        overflow-x: hidden;
        font-family: 'Georgia', serif;
        line-height: 1.6;
        color: #2c3e50;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
        word-wrap: break-word;
        white-space: pre-wrap;
        width: 100%;
        box-sizing: border-box;
    }
    
    /* Ensure content inside output box doesn't overflow */
    .output-box * {
        max-width: 100% !important;
        word-wrap: break-word !important;
        overflow-wrap: break-word !important;
    }
    
    .output-box h1, .output-box h2, .output-box h3, .output-box h4, .output-box h5, .output-box h6 {
        color: #2c3e50 !important;
        margin-top: 1.5rem !important;
        margin-bottom: 0.8rem !important;
        line-height: 1.3 !important;
    }
    
    .output-box p {
        margin-bottom: 1rem !important;
        text-align: justify !important;
    }
    
    .output-box ul, .output-box ol {
        padding-left: 1.5rem !important;
        margin-bottom: 1rem !important;
    }
    
    .output-box li {
        margin-bottom: 0.5rem !important;
    }
    
    /* Stats styling - Compact row */
    .stats-row {
        display: flex;
        gap: 0.75rem;
        margin-bottom: 1rem;
    }
    
    .stat-card {
        background: #f8f9fa;
        padding: 0.8rem;
        border-radius: 6px;
        text-align: center;
        border: 1px solid #e9ecef;
        flex: 1;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }
    
    .stat-num { 
        font-size: 1.5rem; 
        font-weight: bold; 
        color: #2c3e50; 
    }
    .stat-label { 
        font-size: 0.75rem; 
        color: #6c757d; 
    }
    
    /* Form elements */
    .stTextArea textarea {
        background-color: #ffffff !important;
        color: #2c3e50 !important;
        border: 1px solid #dee2e6 !important;
        border-radius: 6px !important;
        min-height: 80px !important;
    }
    
    .stTextArea textarea:focus {
        border-color: #007bff !important;
        box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25) !important;
    }
    
    .stSelectbox select {
        background-color: #ffffff !important;
        color: #2c3e50 !important;
        border: 1px solid #dee2e6 !important;
        border-radius: 6px !important;
    }
    
    /* Generate button - Black with WHITE TEXT */
    .generate-btn button {
        background-color: #1a1a1a !important;
        color: white !important;
        border: none !important;
        border-radius: 6px !important;
        padding: 0.75rem 1.5rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
    }
    
    .generate-btn button:hover {
        background-color: #333333 !important;
        color: white !important;
    }
    
    /* Download area - Compact */
    .download-area {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 6px;
        border: 1px solid #e9ecef;
        margin-top: 1rem;
    }
    
    .download-area .stDownloadButton button {
        background-color: #28a745 !important;
        color: white !important;
        border: none !important;
        border-radius: 4px !important;
        padding: 0.5rem 1rem !important;
        font-size: 0.9rem !important;
    }
    
    .download-area .stDownloadButton button:hover {
        background-color: #218838 !important;
    }
    
    /* Section headers - Smaller */
    .content-box h3 {
        color: #2c3e50 !important;
        margin-top: 0 !important;
        font-size: 1.3rem !important;
        margin-bottom: 1rem !important;
    }
    
    /* Progress bar */
    .stProgress .st-bo {
        background-color: #e9ecef !important;
    }
    
    .stProgress .st-bp {
        background-color: #1a1a1a !important;
    }
    
    /* Footer - Compact */
    .footer {
        text-align: center; 
        padding: 1rem; 
        color: #6c757d;
        border-top: 1px solid #e9ecef;
        margin-top: 1rem;
        font-size: 0.9rem;
    }
    
    /* Remove extra padding */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .header-box {
            flex-direction: column;
            text-align: center;
        }
        
        .stats-row {
            flex-direction: column;
        }
        
        .output-box {
            max-height: 400px;
            min-height: 300px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Header - Compact with logo on left
st.markdown("""
<div class="header-box">
    <img src="https://s3ktech.ai/wp-content/uploads/2025/03/S3Ktech-Logo.png" width="80" style="border-radius: 6px;">
    <div>
        <h1 class="title">AI Blog Research Generator</h1>
        <p class="subtitle">Professional blog creation powered by advanced AI agents</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Sidebar - Black theme
st.sidebar.markdown("### Quick Topics")
topics = [
    "AI in Healthcare", "Digital Marketing", "Cybersecurity", "Remote Work",
    "Blockchain Tech", "Climate Solutions", "Mental Health", "Data Science"
]

selected_topic = None
for topic in topics:
    if st.sidebar.button(topic, key=topic, use_container_width=True):
        selected_topic = topic

# Main Layout - Single page
col1, col2 = st.columns([1, 1.2])

with col1:
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    st.markdown("### Configure Your Blog")
    
    # Topic input - Smaller
    default_value = selected_topic if selected_topic else ""
    user_prompt = st.text_area(
        "Blog Topic:",
        value=default_value,
        placeholder="Enter your blog topic or research question...",
        height=80
    )
    
    # Options - Side by side
    col_tone, col_length = st.columns(2)
    with col_tone:
        tone = st.selectbox("Tone", ["Professional", "Conversational", "Technical"])
    with col_length:
        length = st.selectbox("Length", ["Short", "Medium", "Long"])
    
    # Generate button - Black
    st.markdown('<div class="generate-btn">', unsafe_allow_html=True)
    if st.button("Generate Blog", use_container_width=True):
        if user_prompt:
            with st.spinner("Generating your blog..."):
                try:
                    progress = st.progress(0)
                    progress.progress(50)
                    
                    results = create_blog(user_prompt)
                    progress.progress(100)
                    
                    st.session_state.blog_content = str(results)
                    st.session_state.blog_topic = user_prompt
                    st.success(" Blog generated!")
                    
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("Please enter a topic first")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    st.markdown("###  Generated Content")
    
    if 'blog_content' in st.session_state:
        # Stats - Compact
        content = st.session_state.blog_content
        word_count = len(content.split())
        char_count = len(content)
        read_time = max(1, word_count // 200)
        
        st.markdown(f"""
        <div class="stats-row">
            <div class="stat-card">
                <div class="stat-num">{word_count}</div>
                <div class="stat-label">Words</div>
            </div>
            <div class="stat-card">
                <div class="stat-num">{char_count}</div>
                <div class="stat-label">Characters</div>
            </div>
            <div class="stat-card">
                <div class="stat-num">{read_time}</div>
                <div class="stat-label">Min Read</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Content display - Properly contained and scrollable
        st.markdown('<div class="output-box">', unsafe_allow_html=True)
        st.markdown(content)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Download section - Compact
        st.markdown('<div class="download-area">', unsafe_allow_html=True)
        st.markdown("**📥 Download Options**")
        
        col_d1, col_d2 = st.columns(2)
        with col_d1:
            st.download_button(
                "⬇️ Markdown",
                data=content,
                file_name=f"{st.session_state.blog_topic.replace(' ', '_')[:20]}.md",
                mime="text/markdown",
                use_container_width=True
            )
        with col_d2:
            plain_text = content.replace('#', '').replace('*', '').replace('`', '')
            st.download_button(
                "⬇️ Text",
                data=plain_text,
                file_name=f"{st.session_state.blog_topic.replace(' ', '_')[:20]}.txt",
                mime="text/plain",
                use_container_width=True
            )
        st.markdown('</div>', unsafe_allow_html=True)
        
    else:
        st.markdown("""
        <div class="output-box">
            <div style="text-align: center; padding: 2rem; color: #6c757d;">
                <h4>Ready to Create?</h4>
                <p>Enter your topic and click generate to see your professional blog content here.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer - Compact
st.markdown("""
<div class="footer">
    Built with LangGraph • Gemini • Serper • Streamlit | Powered by <strong style="color: #2c3e50;">S3K Technologies</strong>
</div>
""", unsafe_allow_html=True)