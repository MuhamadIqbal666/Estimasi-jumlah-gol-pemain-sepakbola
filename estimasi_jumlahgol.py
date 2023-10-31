import pickle
import streamlit as st
import numpy as np

# Memuat model
try:
    model = pickle.load(open('estimasi_jumlahgol.sav', 'rb'))
except FileNotFoundError:
    st.error("File model tidak ditemukan.")
    st.stop()

st.title('Estimasi jumlah gol Pemain bola')

Player_Names = st.text_input('Input Nama Pemain')
Country = st.text_input('Input Negara Kompetisi Liga')
League = st.text_input('Input Kompetesi Liga')
Club = st.text_input('Input Club Pemain')
Matches_Played = st.number_input('Jumlah Pertandingan yang telah dimainkan (max : 38)', 0)
Mins = st.number_input('Jumlah menit bermain (max : 4177)', 0)
Shots = st.number_input('Jumlah Tembakan (max:208)', 0)
OnTarget = st.number_input('Jumlah Tembakan yang tepat sasaran (max:208)', 0)
Year = st.selectbox('Pilih Tahun', ['2016', '2017', '2018', '2019', '2020'])

predict = ''

if st.button('Estimasi jumlah gol'):
    try:
        n_features = [[Mins, Matches_Played, Shots, OnTarget, int(Year)]]
        n_features = np.array(n_features)
        predict = model.predict(n_features)
        st.write('Estimasi jumlah gol yang dihasilkan: ', int(predict[0]), 'Gol')
    except Exception as e:
        st.error(f"Terjadi kesalahan saat melakukan prediksi: {str(e)}")
