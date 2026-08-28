
import streamlit as st
from utils.style import apply_global_style

st.set_page_config(page_title="My Herd", page_icon="🐄", layout="wide")
apply_global_style()

st.markdown('<h2 style="text-align:center;">🐄 My Herd</h2>', unsafe_allow_html=True)
st.info("Your animal health records will appear here.")
