import streamlit as st

st.set_page_config(
    page_title="Meu Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

landing = st.Page("landing.py", title="Home", icon="🏠")
dashboard = st.Page("dashboard.py", title="Dashboard", icon="📊")

pg = st.navigation([landing, dashboard])
pg.run()
