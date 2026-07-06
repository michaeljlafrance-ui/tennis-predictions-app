import streamlit as st

st.title("🎾 ATP Tennis Prediction Engine")
st.write("Welcome! This app will eventually use machine learning to predict ATP match outcomes.")

if st.button("Run Model Simulations"):
    st.success("System online! Future simulations will output predictions here.")
else:
    st.info("Click the button above to run the predictive engine.")
