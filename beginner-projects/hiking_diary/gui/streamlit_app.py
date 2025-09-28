import streamlit as st

st.title("Mapa turistických tras🏞️")

uploaded_file = st.file_uploader("Nahraj GPX súbor", type=["gpx"])

if uploaded_file:
    st.success(f"Súbor nahratý: {uploaded_file.name}")
