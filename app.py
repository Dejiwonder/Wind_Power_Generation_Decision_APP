
import streamlit as st
import pandas as pd

# Load CSVs
day365_df = pd.read_csv("C:/Users/Acer\Desktop/ML project/Wind_Power_Generation_Decision_APP/artifacts/day365_comparison.csv")
day366_df = pd.read_csv("C:/Users/Acer\Desktop/ML project/Wind_Power_Generation_Decision_APP/artifacts/day366_forecast.csv")

# Title
st.title("🔋 Wind Power Forecast Dashboard")

# Day 365 Comparison
st.subheader("📊 Day 365: Actual vs Forecasted Power")
st.dataframe(day365_df.style.format({
    "Actual Power (MW)": "{:.2f}",
    "Forecasted Power (MW)": "{:.2f}",
    "Absolute Error": "{:.2f}",
    "Error (%)": "{:.2f}"
}))

# Day 366 Forecast
st.subheader("🔮 Day 366: Forecasted Power")
st.dataframe(day366_df.style.format({
    "Forecasted Power (MW)": "{:.2f}"
}))