import pandas as pd
import streamlit as st

st.title("Semakin tinggi tingkat pendidikan, Semakin tinggi pula upahnya?")

st.write('Data Tingkat Penyelesaian Pendidikan')
data_pendidikan = pd.read_excel('data/source/Tingkat Penyelesaian Pendidikan Menurut Jenjang Pendidikan dan Provinsi.xlsx')
st.dataframe(data_pendidikan)

st.write('Upah Rata-Rata Per jam')
data_pendidikan = pd.read_excel('data/source/Upah Rata - Rata Per Jam Pekerja Menurut Provinsi.xlsx')
st.dataframe(data_pendidikan)