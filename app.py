
import streamlit as st
from utils.style import apply_global_style
from utils.auth import sign_up, sign_in, sign_out, get_current_user

st.set_page_config(page_title="VETAI – Livestock Health", page_icon="🐄", layout="wide")
apply_global_style()

# Initialize user
if "user" not in st.session_state:
    st.session_state.user = None

# Sidebar Auth
with st.sidebar:
    st.markdown("## 🐄 Account")
    user = get_current_user()
    if user is None:
        auth_choice = st.radio("Login / Signup", ["Login", "Signup"])
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if auth_choice == "Signup":
            first_name = st.text_input("First Name (optional)")
            last_name = st.text_input("Last Name (optional)")
            if st.button("Create Account"):
                if email and password:
                    with st.spinner("Creating..."):
                        user, err = sign_up(email, password, first_name, last_name)
                    if user:
                        st.session_state.user = user
                        st.success("Account created! 30 free scans added.")
                        st.rerun()
                    else:
                        st.error(err)
                else:
                    st.warning("Email and password required.")
        else:
            if st.button("Login"):
                if email and password:
                    with st.spinner("Logging in..."):
                        user, err = sign_in(email, password)
                    if user:
                        st.session_state.user = user
                        st.success("Logged in!")
                        st.rerun()
                    else:
                        st.error(err)
                else:
                    st.warning("Email and password required.")
    else:
        st.write(f"Logged in as: **{user.email}**")
        if st.button("Logout"):
            sign_out()
            st.rerun()

# Hero
st.markdown('<div class="hero-title">🐄 VETAI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Livestock Health AI</div>', unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center; margin: 2rem 0;">
    <span style="font-size:1.2rem; color:#8892b0;">Snap a photo. Identify the disease. Save your animal.</span>
</div>
""", unsafe_allow_html=True)

# Quick Stats
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Animals", "Cattle, Poultry, Goats")
with col2:
    st.metric("Diseases", "20+")
with col3:
    st.metric("Per Scan", "₦200")
with col4:
    st.metric("Offline", "Ready")

st.markdown("---")
st.subheader("🚀 Quick Access")
col1, col2, col3 = st.columns(3)
with col1:
    st.page_link("pages/1_Scan_Animal.py", label="📸 Scan Animal", use_container_width=True)
with col2:
    st.page_link("pages/2_My_Herd.py", label="🐄 My Herd", use_container_width=True)
with col3:
    st.page_link("pages/3_Buy_Scans.py", label="💳 Buy Scans", use_container_width=True)

st.caption("Powered by Darkmoor Ltd")
