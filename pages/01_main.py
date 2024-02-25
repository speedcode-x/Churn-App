import streamlit as st



st.set_page_config(
    page_icon=':house:',

    layout='wide'
)


from dashboard import dashboard_display as dashboard
from data_predict import data_predict 
from home import home_display as home
from history import history_display as history






def main():
    pages = {
        "Home": home,
        "Data Predict": data_predict,
        "History": history,
        "Dashboard": dashboard
    }

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))

    page = pages[selection]
    page()

if __name__ == "__main__":
    main()
