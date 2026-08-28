
import streamlit as st
from utils.style import apply_global_style

st.set_page_config(page_title="Buy Scans", page_icon="💳", layout="wide")
apply_global_style()

st.markdown('<h2 style="text-align:center;">💳 Buy Scans</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("### 100 Scans – ₦20,000")
    if st.button("Select 100", use_container_width=True):
        st.session_state.plan = "100"
with col2:
    st.markdown("### 300 Scans – ₦50,000")
    if st.button("Select 300", use_container_width=True):
        st.session_state.plan = "300"

if "plan" in st.session_state:
    st.success(f"Selected plan: {st.session_state.plan} scans")
    st.info("Paystack integration coming soon.")
