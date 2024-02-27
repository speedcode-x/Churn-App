import streamlit as st


def predict_display():
    st.title("Data Prediction Page")
    st.write("Welcome to the Data Prediction Page")
    st.write("Please enter the required information to make a prediction.")

    # Input fields for prediction
    st.subheader("Input Information")
    # feature1 = st.number_input("Feature 1", min_value=0.0)
    # feature2 = st.number_input("Feature 2", min_value=0.0)
 
    with st.form('feature'):
        # split in to columns
        col1,col2 = st.columns(2)

        with col1:
            st.header('Personal information')
            feature1 = st.selectbox("Senior Citizen", (True, False))

            feature2 = st.selectbox("Partner",(True, False))

            feature3 = st.selectbox("Phone Service",(True, False))

            feature4 = st.number_input("Dependents",min_value=0, max_value= 10)

            feature5 = st.selectbox("Online Security",(True, False))

        with col2:
            st.header('Other Information')
            feature6 = st.selectbox("Online Backup",(True, False))

            feature7 = st.selectbox("Device Protection",(True, False))

            feature8 = st.selectbox("Tech Support",(True, False))

            feature9 = st.selectbox("StreamingTV",(True, False))

            feature10 = st.selectbox("Streaming Movies",(True, False))

            feature11 = st.selectbox("Contract",("One year", 'Month-to-month', "Two years"))

            feature12 = st.selectbox("Paperless Billing",(True, False))

            feature13 = st.selectbox("Payment Method",("Electronic check", "Mailed check","Bank Transfer (automatic)",))

            feature14 = st.number_input("Monthly Charges",min_value=0.0)

            feature15 = st.number_input("Total Charges",min_value=0.0)

          
            feature17 = st.selectbox("Multiple Lines",(True, False))

            feature18 = st.selectbox("Internet Service",('DSL', "Fiber optic"))

            feature19 = st.slider("Tenure")

        # Submit button to make prediction
        st.form_submit_button ('Predict') 

        # if submit_button:
        #     # Make prediction
        #     prediction, probability = make_prediction(pipeline, encoder)
        #     # Display prediction
        #     st.markdown(prediction)

   


