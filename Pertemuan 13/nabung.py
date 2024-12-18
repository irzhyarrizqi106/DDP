import streamlit as st

st.title("Sedangkan disini ialah halaman Nabung dalam streamlit kami!")

with st.form("nabung"):
    nama=st.text_input("Masukkan Nama: ")
    jumlah=st.number_input("Masukkan Jumlah: ")
    SubmitButtom=st.form_submit_button("Submit")
    # st.form_submit_button("Submit")
    if SubmitButtom:
        st.write("Nama: ", nama)
        st.write("Jumlah: ", jumlah)
        st.session_state['Nabung'].append({
            "Nama": nama,
            "Jumlah": jumlah
        })
        st.success("Data berhasil disimpan")