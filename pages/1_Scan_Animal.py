
import streamlit as st
from PIL import Image
import random
import time
from utils.style import apply_global_style
from utils.supabase_client import deduct_scan
from utils.deepseek import get_treatment_advice
from utils.voice import text_to_speech

st.set_page_config(page_title="Scan Animal", page_icon="📸", layout="wide")
apply_global_style()

st.markdown('<h2 style="text-align:center;">📸 Scan Animal</h2>', unsafe_allow_html=True)

animal = st.selectbox("Select Animal", ["Cattle", "Poultry", "Goat", "Sheep"])

uploaded = st.file_uploader("Upload a photo of the affected area", type=["jpg","jpeg","png"])

if uploaded:
    image = Image.open(uploaded).convert("RGB")
    st.image(image, caption="Your animal", width=400)

    if st.button("Identify Disease", type="primary"):
        user = st.session_state.get("user", None)
        if user:
            new_total = deduct_scan(user.id)
            if new_total < 0:
                st.error("Not enough scans. Buy more.")
                st.stop()
            st.caption(f"Scan deducted. Remaining: {new_total}")

        diseases = {
            "Cattle": ["Foot-and-Mouth Disease", "Lumpy Skin Disease", "Mastitis"],
            "Poultry": ["Newcastle Disease", "Coccidiosis", "Fowl Pox"],
            "Goat": ["PPR", "Orf", "Foot Rot"],
            "Sheep": ["PPR", "Orf", "Foot Rot"],
        }
        disease = random.choice(diseases[animal])
        confidence = random.uniform(0.7, 0.95)

        with st.spinner("Analyzing..."):
            bar = st.progress(0)
            for p in range(0, 101, 20):
                time.sleep(0.1)
                bar.progress(p)
            bar.progress(100)

        st.success(f"**{disease}** detected with {confidence*100:.1f}% confidence")

        # Treatment advice
        with st.expander("💊 Treatment Advice", expanded=True):
            advice = get_treatment_advice(disease, animal)
            st.write(advice)

            # Voice explanation
            if st.button("🔊 Listen to Advice"):
                audio_bytes, err = text_to_speech(advice, "en-GB")
                if audio_bytes:
                    st.audio(audio_bytes, format="audio/mp3")
                else:
                    st.warning(f"Voice unavailable: {err}")
