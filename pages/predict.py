import streamlit as st
import pandas as pd
import numpy as np
import joblib


@st.cache_resource(show_spinner="model loading")
def load_forest_pipeline():
    pipeline = joblib.load("models/logistic_model.joblib")
    return pipeline

def load_svc_model():
    pipeline = joblib.load("models/sgd_pipeline.joblib")
    return pipeline


def select_model():
    cols1, cols2 = st.columns(2)
    with cols1:
        st.selectbox('select a model',options=["Logistic Model","SVC Model"],key="select model")

    with cols2:
        pass

def predict_display():
    st.title("Data Prediction Page")
    st.write("Welcome to the Data Prediction Page")
    st.write("Please enter the required information to make a prediction.")

   

    st.title('Make a Prediction')
    
    select_model()

   
    # Input fields for prediction
    st.subheader("Input Information")
    # feature1 = st.number_input("Feature 1", min_value=0.0)
    # feature2 = st.number_input("Feature 2", min_value=0.0)
 
    with st.form('feature'):
        # split in to columns
        col1,col2 = st.columns(2)

        with col1:
            st.header('Personal information')
            feature1 = st.selectbox("Senior Citizen", (True, False), key="snr citizen")

            feature2 = st.selectbox("Partner",(True, False), key="partner")

            feature3 = st.selectbox("Phone Service",(True, False),key="phone service")

            feature4 = st.number_input("Dependents",min_value=0, max_value= 10,key="dependents")

            feature5 = st.selectbox("Online Security",(True, False), key="online security")

        with col2:
            st.header('Other Information')
            feature6 = st.selectbox("Online Backup",(True, False), key="online backup")

            feature7 = st.selectbox("Device Protection",(True, False), key="device protection")

            feature8 = st.selectbox("Tech Support",(True, False), key="tech support")

            feature9 = st.selectbox("StreamingTV",(True, False), key="streamingtv")

            feature10 = st.selectbox("Streaming Movies",(True, False),key="streaming movies")

            feature11 = st.selectbox("Contract",("One year", 'Month-to-month', "Two years"), key="contract")

            feature12 = st.selectbox("Paperless Billing",(True, False), key="paperless billing")

            feature13 = st.selectbox("Payment Method",("Electronic check", "Mailed check","Bank Transfer (automatic)",), key="payment method")

            feature14 = st.number_input("Monthly Charges",min_value=0.0, key="monthly charges")

            feature15 = st.number_input("Total Charges",min_value=0.0, key="total charges")
            feature17 = st.selectbox("Multiple Lines",(True, False))

            feature18 = st.selectbox("Internet Service",('DSL', "Fiber optic"),key="internet service")

            feature19 = st.slider("Tenure", key="tenure")

        # Submit button to make prediction
        st.form_submit_button ('Predict') 

        # if submit_button:
        #     # Make prediction
        #     prediction, probability = make_prediction(pipeline, encoder)
        #     # Display prediction
        #     st.markdown(prediction)
   
    st.write(st.session_state)


