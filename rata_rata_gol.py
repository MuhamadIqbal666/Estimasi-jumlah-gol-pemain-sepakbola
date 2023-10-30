import pickle
import streamlit as st

# Memuat model
try:
    model = pickle.load(open('rata_rata_gol.sav', 'rb'))
except FileNotFoundError:
    st.error("File model tidak ditemukan.")
    st.stop()

st.title('Jumlah rata-rata gol per tahun pemain La Liga')

Player_Names = st.text_input('Input nama pemain')
Mins = st.number_input('Jumlah menit bermain', 0)
Goals = st.number_input('Jumlah gol', 0)
xG = st.number_input('Jumlah peluang yang menjadi gol', 0)
xG_Per_Avg_Match = st.number_input('Jumlah peluang yang menjadi gol per rata-rata pertandingan', 0)
Shots = st.number_input('Jumlah Tembakan', 0)
OnTarget = st.number_input('Jumlah Tembakan yang tepat sasaran', 0)
Shots_Per_Avg_Match = st.number_input('Jumlah Tembakan per rata-rata pertandingan', 0)
On_Target_Per_Avg_Match = st.number_input('Jumlah Tembakan yang tepat sasaran per rata-rata pertandingan', 0)
Year = st.selectbox('Pilih tahun', ['2016', '2017', '2018', '2019'])

predict = ''

if st.button('Rata-rata gol per tahun'):
    try:
        n_features = [[Mins, Goals, xG, xG_Per_Avg_Match, Shots, OnTarget, Shots_Per_Avg_Match, On_Target_Per_Avg_Match, int(Year)]]
        predict = model.predict(n_features)
        st.write('Rata-rata gol per tahun: ', predict)
    except Exception as e:
        st.error(f"Terjadi kesalahan saat melakukan prediksi: {str(e)}")
