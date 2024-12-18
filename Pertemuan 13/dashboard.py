import streamlit as st

st.title("Di dalam sini adalah halaman dashboard dalam streamlit kami!")
st.session_state["Nabung"] 

jumlah = 0
for session in st.session_state["Nabung"]:
    jumlah += session["Jumlah"]

st.write("Total nominal menabung anda sebesar: ", jumlah)