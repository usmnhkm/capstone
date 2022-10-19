import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="Hubungan Status Ekonomi dengan Tingkat Penyelesaian Sekolah")

components.html(
    """
    <h1 style="text-align: center">Hubungan Status Ekonomi dengan Tingkat Penyelesaian Sekolah</h1>
    <p>"Direktur Jenderal Pendidikan Dasar Kemendikbud Hamid Muhammad menyebutkan 
    masalah ekonomi menjadi faktor utama anak sekolah tidak bisa melanjutkan pendidikan ke jenjang yang lebih tinggi."</p>
    <a href="https://edukasi.okezone.com/read/2015/08/17/65/1197508/75-persen-anak-putus-sekolah-akibat-faktor-ekonomi">Okezone</a>
    <p>"Dampak pandemi Covid-19 pada dunia pendidikan sangat besar. Salah satunya, peningkatan angka putus sekolah karena anak didik ikut 
    membantu ekonomi keluarga selama pandemi. Sekjen Kementerian Pendidikan, Kebudayaan, Riset dan Teknologi (Kemendikbudristek), Suharti menyebut angka ini cukup tinggi."</p>
    <a href="https://www.kompas.com/edu/read/2022/01/04/111336071/kemendikbud-sebut-angka-putus-sekolah-sd-naik-10-kali-lipat-selama-pandemi?page=all#page2">Kompas</a>
    """,
    height=300,
)


with st.sidebar:
    st.title("Hubungan Status Ekonomi dengan Tingkat Penyelesaian Sekolah")
    tipe = st.selectbox("Tipe Plot:", ("Bar", "Point"))
    year = st.selectbox("Tahun:", ("Semua", "2015", "2016", "2017", "2018", "2019", "2020", "2021"))
    jenjang = st.selectbox("Jenjang Pendidikan:", ("Semua", "SD / Sederajat", "SMP / Sederajat", "SMA / Sederajat"))

ori = pd.read_excel("Tingkat Penyelesaian Pendidikan Menurut Jenjang Pendidikan dan Kelompok Pengeluaran.xlsx")
ori.head()

df = ori
df.iloc[0, 1:] = df.iloc[0, 1:].astype(str)
df.iloc[0, 1:] = df.iloc[0, 1:].str.split('.', expand = True)[0]
df.head()

df.columns = df.iloc[0, :]
df.drop(0, inplace=True)
df.head()

df.columns = df.columns.fillna('Kelompok Pengeluaran')
df.head()

df = df.set_index('Kelompok Pengeluaran')
df.head()

parent = ['SD / Sederajat'] * 7 + ['SMP / Sederajat'] * 7 + ['SMA / Sederajat'] * 7
child = df.columns[0:7].tolist() + df.columns[7:14].tolist() + df.columns[14:].tolist()
df.columns = pd.MultiIndex.from_arrays([parent, child])
df.head()

tahun = ('2015', '2016', '2017', '2018', '2019', '2020', '2021')
jenjang_pendidikan = ('SD / Sederajat', 'SMP / Sederajat', 'SMA / Sederajat')
kelompok_pengeluaran = ('Terbawah', 'Menengah bawah', 'Menengah', 'Menengah atas', 'Teratas')
index = pd.MultiIndex.from_product(
    [tahun, jenjang_pendidikan, kelompok_pengeluaran],
    names=['Tahun', 'Jenjang Pendidikan', 'Kelompok Pengeluaran']
)

size = len(index)
percentage = []
for i in range(21):
  for j in range(5):
    percentage.append(df.iat[j, i])


data = pd.DataFrame(data={'Persentase Penyelesaian': percentage}, index=index).reset_index()

col1, col2, col3 = st.columns(3)
with col1:
    st.empty()
with col2:
    """# Data"""
    st.dataframe(data)
with col3:
    st.empty()


if year == "Semua" and jenjang == "Semua":
    chart = sns.catplot(x='Tahun', y='Persentase Penyelesaian', hue='Kelompok Pengeluaran', 
                        col='Jenjang Pendidikan', data=data, kind=tipe.lower())
elif year == "Semua" and jenjang != "Semua":
    chart = sns.catplot(x='Tahun', y='Persentase Penyelesaian', hue='Kelompok Pengeluaran', 
                        col='Jenjang Pendidikan', data=data[data['Jenjang Pendidikan'] == jenjang], kind=tipe.lower())
elif year != "Semua" and jenjang == "Semua":
    chart = sns.catplot(x='Tahun', y='Persentase Penyelesaian', hue='Kelompok Pengeluaran', 
                        col='Jenjang Pendidikan', data=data[data['Tahun'] == year], kind=tipe.lower())
else:
    chart = sns.catplot(x='Tahun', y='Persentase Penyelesaian', hue='Kelompok Pengeluaran', 
                        col='Jenjang Pendidikan', data=data[(data['Jenjang Pendidikan'] == jenjang) & (data['Tahun'] == year)], kind=tipe.lower())
st.pyplot(chart)

st.markdown("Dari visualisasi di atas dapat disimpulkan bahwa terdapat hubungan antara status ekonomi dengan tingkat penyelesaian sekolah.")
st.markdown("Status ekonomi terbawah memiliki tingkat penyelesaian sekolah terendah, sedangkan status ekonomi teratas memiliki tingkat penyelesaian sekolah tertinggi.")