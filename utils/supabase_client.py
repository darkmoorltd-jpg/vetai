
import streamlit as st
from supabase import create_client

def get_service_client():
    url = st.secrets["supabase"]["url"]
    key = st.secrets["supabase"]["service_key"]
    return create_client(url, key)

def deduct_scan(user_id, amount=1):
    client = get_service_client()
    try:
        res = client.table("user_scans").select("scans_remaining").eq("user_id", user_id).execute()
        current = res.data[0]["scans_remaining"] if res.data else 30
        new_total = max(0, current - amount)
        client.table("user_scans").update({"scans_remaining": new_total}).eq("user_id", user_id).execute()
        return new_total
    except Exception as e:
        st.error(f"Error deducting scan: {e}")
        return 0
