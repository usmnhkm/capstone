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

#data_upah
st.markdown("<h3 style='text-align: left; color: black; text-size: 14;'>Data Tingkat Kelulusan tiap jenjang</h3>", unsafe_allow_html=True)
dp = pd.read_csv('data/data_fix/data_pendidikan.csv', index_col='Provinsi')
st.dataframe(dp)
dp_sd_2021 = dp['SD_2021']
dp_smp_2021 = dp['SMP_2021']
dp_sma_2021 = dp['SMA_2021']
col1,col2,col3 = st.columns(3)

with col1:
    st.markdown("<h3 style='text-align: center; color: black; text-size: 12;'>Data Tingkat Kelulusan SD tahun 2021</h3>", unsafe_allow_html=True)
    st.bar_chart(data=dp_sd_2021)

with col2:
    st.markdown("<h3 style='text-align: center; color: black; text-size: 12;'>Data Tingkat Kelulusan SMP tahun 2021</h3>", unsafe_allow_html=True)
    st.bar_chart(data=dp_smp_2021)

with col3:
    st.markdown("<h3 style='text-align: center; color: black; text-size: 12;'>Data Tingkat Kelulusan SMA tahun 2021</h3>", unsafe_allow_html=True)
    st.bar_chart(data=dp_sma_2021)


# data_upah

upah_pekerja_bebas = pd.read_csv('data/data_fix/upah_pekerja_bebas.csv', on_bad_lines='skip')
upah_wirausaha = pd.read_csv('data/data_fix/upah_wirausaha.csv')

col4, col5 = st.columns(2)

with col4:
    st.dataframe(upah_pekerja_bebas)

with col5:
    st.dataframe(upah_wirausaha)