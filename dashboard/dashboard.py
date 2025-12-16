import streamlit as st
import requests

st.title("Gold & Silver Price Dashboard")

API_URL = "http://127.0.0.1:5000/prices"

response = requests.get(API_URL)
data = response.json()

if not data:
    st.warning("No data available")
else:
    st.table(data)
