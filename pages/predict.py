import streamlit as st
import pandas as pd
import numpy as np
import joblib







st.cache_resource(show_spinner="model loading")
def load_logistic_pipeline():
    pipeline = joblib.load("models/logistic_model.joblib")
    return pipeline

def load_svc_model():
    pipeline = joblib.load("models/sgd_pipeline.joblib")
    return pipeline

st.cache_resource
def select_model():
    cols1, cols2 = st.columns(2)
    with cols1:
        st.selectbox('select a model',options=["Logistic Model","SVC Model"],key="selected model")

    with cols2:
        pass

    if st.session_state['selected model'] == "Logistic Model":
        pipeline = load_logistic_pipeline()
    else:
        pipeline = load_svc_model()

    encoder = joblib.load("models/encoder.joblib")

    return pipeline, encoder
    
def make_prediction(pipeline, encoder):
    SeniorCitizen = st.session_state["snr citizen"]
    Partner = st.session_state["partner"]
    Dependents = st.session_state["dependents"]
    PhoneService = st.session_state["phone service"]
    MultipleLines = st.session_state["multiplelines"]
    InternetService = st.session_state["internet service"]
    OnlineSecurity = st.session_state["online security"]
    OnlineBackup = st.session_state["online backup"]
    DeviceProtection =st.session_state["device protection"]
    TechSupport = st.session_state["tech support"]
    StreamingTV = st.session_state["streamingtv"]
    StreamingMovies = st.session_state["streaming movies"]
    Contract = st.session_state["contract"]
    PaperlessBilling = st.session_state["paperless billing"]
    PaymentMethod = st.session_state["payment method"]
    MonthlyCharges= st.session_state["monthly charges"]
    TotalCharges = st.session_state["total charges"]
    tenure = st.session_state["tenure"]
  
  # Define columns and create DataFrame
    columns = ["SeniorCitizen", "Partner", "Dependents",
        "PhoneService", "MultipleLines", "InternetService",
       "OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport",
       "StreamingTV", "StreamingMovies", 'Contract', "PaperlessBilling",
       "PaymentMethod", "MonthlyCharges", "TotalCharges","tenure"]

    
    data = [[ SeniorCitizen, Partner, Dependents,
        PhoneService, MultipleLines, InternetService,
       OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport,
       StreamingTV, StreamingMovies, Contract, PaperlessBilling,
       PaymentMethod, MonthlyCharges, TotalCharges,tenure]]
    

    #Create a Dataframe
    df = pd.DataFrame(data, columns=columns)

    
    # Make prediction
    predict = pipeline.predict(df)
    # prediction = int(predict[0])
   

          



def predict_display():
    st.title("Data Prediction Page")
    st.write("Welcome to the Data Prediction Page")
    st.write("Please enter the required information to make a prediction.")

   

    st.title('Make a Prediction')
    
    # select_model()

   
    # Input fields for prediction
    st.subheader("Input Information")
    # feature1 = st.number_input("Feature 1", min_value=0.0)
    # feature2 = st.number_input("Feature 2", min_value=0.0)
 
    with st.form('feature'):
        pipeline, encoder = select_model()
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
            feature17 = st.selectbox("Multiple Lines",(True, False), key="multiplelines")

            feature18 = st.selectbox("Internet Service",('DSL', "Fiber optic"),key="internet service")

            feature19 = st.slider("Tenure", key="tenure")

        # Submit button to make prediction
        st.form_submit_button ('Predict',on_click=make_prediction, kwargs=dict(pipeline = pipeline,encoder = encoder)) 

        # if submit_button:
        #     # Make prediction
        #     prediction, probability = make_prediction(pipeline, encoder)
        #     # Display prediction
        #     st.markdown(prediction)
   
    st.write(st.session_state)


