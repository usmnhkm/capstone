import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(layout="wide", page_title="Semakin tinggi tingkat pendidikan, semakin tinggi pula upah yang diterima?")

st.markdown("<h1 style='text-align: center; color: grey;'>Semakin tinggi tingkat pendidikan, semakin tinggi pula upah yang diterima?</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: grey;'>Perbandingan upah berdasarkan tingkat pendidikan</h2>", unsafe_allow_html=True)
st.write('')
st.write('')
#ump
st.markdown("<h3 style='text-align: left; color: black; text-size: 14;'>Data UMP Indonesia tahun 2022</h3>", unsafe_allow_html=True)
data_ump = pd.read_csv('data/data_fix/ump.csv', index_col='Provinsi')
ump_2022 = data_ump['2022']
st.bar_chart(data=ump_2022)
ump_2022_avg = ump_2022.mean()
st.write('Pada tahun 2022 rata-rata upah minimum provinsi di indonesia ada pada angka ' + str(ump_2022_avg))