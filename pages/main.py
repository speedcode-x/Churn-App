import streamlit as st



st.set_page_config(
    page_icon=':house:',
    page_title="Churn Prediction App",
    layout='wide'
)


from dashboard import dashboard_display as dashboard
from data import data_display as data
from home import home_display as home
from history import history_display as history
from predict import predict_display as predict

def main():
    pages = {
       "🏠Home ": home,
        "📊Data ": data,
        "🎯Predict ": predict,
        "🕒History ": history,
        "📈Dashboard ": dashboard
    }

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))

     # Apply CSS to underline selected item
    css = """
    <style>
    .sidebar-item-selected {
        text-decoration: underline;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

    page = pages[selection]
    page()

if __name__ == "__main__":
    main()
