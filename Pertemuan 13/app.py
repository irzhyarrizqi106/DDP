import streamlit as st

st.write("Selamat datang di halaman streamlit")

dashboard = st.Page("./pages/dashboard.py", title="Dashboard")
nabung = st.Page("./pages/nabung.py", title="Nabung")

pg = st.navigation({
    "Dasar": [dashboard],
    "Keuangan": [nabung],
})

if "Nabung" not in st.session_state:
    st.session_state["Nabung"] = []
    
pg.run()
