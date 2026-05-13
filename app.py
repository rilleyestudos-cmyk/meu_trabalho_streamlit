import streamlit as st

landing = st.Page("landing.py", title="Home", icon="🏠")
dashboard = st.Page("dashboard.py", title="Dashboard", icon="📊")

pg = st.navigation([landing, dashboard])
st.set_page_config(
    page_title="Meu Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)
pg.run()
