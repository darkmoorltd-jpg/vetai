
import streamlit as st

def apply_global_style():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;500;600;700&display=swap');
    :root {
        --bg: #0a0e17;
        --surface: #111827;
        --border: #1f2a44;
        --green: #00c853;
        --cyan: #00e5ff;
        --text: #e0e0e0;
        --dim: #8892b0;
    }
    .stApp {
        background: radial-gradient(ellipse at 20% 50%, #0d1b2a 0%, #0a0e17 70%);
        color: var(--text);
    }
    header[data-testid="stHeader"] { background: transparent; }
    footer {visibility: hidden;}
    .hero-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 4.5rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(135deg, #00c853 0%, #69f0ae 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
    }
    .subtitle {
        text-align: center;
        font-size: 1.4rem;
        color: var(--dim);
        letter-spacing: 2px;
        margin-top: -10px;
    }
    .card {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 0.5rem 0;
    }
    .stButton > button {
        background: linear-gradient(135deg, #00c853, #69f0ae);
        color: #0a0e17;
        border: none;
        border-radius: 8px;
        font-weight: bold;
        padding: 0.6rem 1.5rem;
    }
    </style>
    """, unsafe_allow_html=True)
