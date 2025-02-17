import streamlit as st
import requests
import json
from datetime import datetime
import pandas as pd


st.set_page_config(
    page_title="AI News Article Generator",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
    <style>
    /* Main app styling */
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #1f2937;
        padding: 2rem 1rem;
    }
    
    /* Sidebar title */
    .css-1d391kg .css-1629p8f h1 {
        color: white !important;
        font-size: 1.5rem !important;
        margin-bottom: 2rem;
    }
    
    /* Sidebar text and sliders */
    .css-1d391kg .css-81oif8 {
        color: #e5e7eb !important;
    }
    
    /* Updated slider color */
    .css-1d391kg .stSlider > div > div > div > div {
        background-color: #69b716 !important;
    }
    
    /* Header styling */
    .header {
        background-color: #1f2937;
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 1rem;
    }
    
    /* Main content area */
    .main-content {
        background-color: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Input field styling */
    .stTextInput > div > div > input {
        border-radius: 8px;
        border: 2px solid #e5e7eb;
        padding: 0.75rem;
        font-size: 1rem;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #69B716;
        color: white;
        padding: 0.75rem 2rem;
        border-radius: 8px;
        border: none;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #45a049;
        transform: translateY(-2px);
    }
    
    /* Updated download button styling to match generate article button */
    .stDownloadButton > button {
        background-color: #69B716 !important;
        color: white !important;
        padding: 0.75rem 2rem !important;
        border-radius: 8px !important;
        border: none !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    
    .stDownloadButton > button:hover {
        background-color: #45a049 !important;
        transform: translateY(-2px) !important;
    }
    
    /* Tips section */
    .tips-section {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #4CAF50;
    }
    
    .tips-section h3 {
        color: #1f2937;
        margin-bottom: 1rem;
    }
    
    /* Article container */
    .article-container {
        background-color: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-top: 2rem;
    }
    
    /* Footer styling */
    .footer {
        background-color: #1f2937;
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin-top: 2rem;
    }
    
    /* Text colors */
    h1, h2, h3, p {
        color: #1f2937 !important;
    }
    
    .white-text {
        color: white !important;
    }
    
    .tips-text {
        color: #4b5563 !important;
    }
    </style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown("""
        <div class="header">
            <img src="https://hebbkx1anhila5yf.public.blob.vercel-storage.com/image-rafpP6QDE2DSPHXoPzGo4i4uKebarm.png" style="width: 40px; height: 40px;">
            <div>
                <h1 class="white-text">AI News Article Generator</h1>
                <p class="white-text" style="margin: 0;">Transform your headlines into full-length news articles using AI</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown('<h1 class="white-text">Settings</h1>', unsafe_allow_html=True)
        tone = st.select_slider(
            "Article Tone",
            options=["Formal", "Neutral", "Casual"],
            value="Neutral"
        )
        
        length = st.slider(
            "Word Length",
            min_value=200,
            max_value=1000,
            value=500,
            step=50
        )
        
        st.markdown("---")
        st.markdown('<h2 class="white-text">History</h2>', unsafe_allow_html=True)
        if 'history' in st.session_state:
            for item in st.session_state.history:
                st.markdown(f'<p class="white-text">- {item["headline"]}</p>', unsafe_allow_html=True)
    

    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="main-content">', unsafe_allow_html=True)
        st.markdown('<h2>Enter Your Headline</h2>', unsafe_allow_html=True)
        headline = st.text_input(
            "",
            placeholder="Type your headline here...",
            key="headline_input"
        )
        
        if st.button("Generate Article", key="generate_btn"):
            if headline:
                with st.spinner("Generating your article..."):
                    try:
                        response = requests.post(
                            "http://localhost:8000/generate-article",
                            json={
                                "headline": headline,
                                "tone": tone.lower(),
                                "length": length
                            }
                        )
                        
                        if response.status_code == 200:
                            article_data = response.json()
                            
                            if 'history' not in st.session_state:
                                st.session_state.history = []
                            st.session_state.history.append({
                                'headline': headline,
                                'generated_at': article_data['generated_at']
                            })
                            
                            st.markdown(
                                f"""
                                <div class="article-container">
                                    <h2>{article_data['headline']}</h2>
                                    <p><i>Generated on {article_data['generated_at']}</i></p>
                                    <p>{article_data['article']}</p>
                                    <p><b>Word count:</b> {article_data['word_count']}</p>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )
                            
                            st.download_button(
                                "Download Article",
                                article_data['article'],
                                file_name=f"article_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                                mime="text/plain"
                            )
                    except Exception as e:
                        st.error(f"Error generating article: {str(e)}")
            else:
                st.warning("Please enter a headline first!")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="tips-section">
                <h3>Tips for Better Results</h3>
                <ul class="tips-text">
                    <li>Be specific with your headline</li>
                    <li>Include key details (Who, What, Where, When)</li>
                    <li>Choose the appropriate tone for your target audience</li>
                    <li>Adjust length based on your needs</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
        if 'history' in st.session_state and st.session_state.history:
            st.markdown('<div class="main-content">', unsafe_allow_html=True)
            st.subheader("Your Analytics")
            df = pd.DataFrame(st.session_state.history)
            st.metric("Articles Generated", len(df))
            st.line_chart(df.groupby('generated_at').size())
            st.markdown('</div>', unsafe_allow_html=True)
    

    st.markdown("""
        <div class="footer">
            <p class="white-text">Developed by Saurabh Kumar</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()