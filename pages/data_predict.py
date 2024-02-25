import streamlit as st


def data_predict():
    st.title("Data Prediction Page")
    st.write("Welcome to the Data Prediction Page")
    predict = st.button("Predict")
    if predict:
        st.write("DONE!")
    # Add your data prediction code here

