import streamlit as st
import pandas as pd

st.title("🛒 SuperKart Sales Forecast")

uploaded_file = st.file_uploader("Upload sales data CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of uploaded data:")
    st.dataframe(df.head())

    # Placeholder for prediction
    st.success("✅ Forecasting logic goes here...")
