import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000/prices"

st.set_page_config(page_title="Gold & Silver Dashboard", layout="centered")

st.title("🥇 Gold & Silver Price Dashboard")

try:
    response = requests.get(API_URL, timeout=5)
    response.raise_for_status()
    data = response.json()

    if not data:
        st.warning("No price data available.")
    else:
        st.table(data)

except Exception as e:
    st.error("Unable to connect to backend API")
    st.code(str(e))
