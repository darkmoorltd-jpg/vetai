
import requests
import streamlit as st

def get_treatment_advice(disease, animal):
    """Get AI treatment advice from DeepSeek."""
    try:
        api_key = st.secrets["deepseek"]["api_key"]
    except:
        api_key = ""
    if not api_key:
        return f"Treatment advice for {disease} in {animal} will be available soon."

    prompt = f"Give practical treatment advice for {disease} in {animal}. Include organic and chemical options."
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "system", "content": "You are VETAI, a livestock health expert."},
                     {"role": "user", "content": prompt}],
        "max_tokens": 300
    }
    try:
        r = requests.post("https://api.deepseek.com/v1/chat/completions", headers=headers, json=payload, timeout=15)
        if r.status_code == 200:
            return r.json()["choices"][0]["message"]["content"].strip()
        else:
            return f"Advice unavailable (API error {r.status_code})"
    except Exception as e:
        return f"Advice unavailable: {e}"
