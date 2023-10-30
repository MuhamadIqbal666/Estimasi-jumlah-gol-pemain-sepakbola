# Laporan Proyek Machine Learning
### Nama : Muhamad Iqbal
### Nim : 211351088
### Kelas : Pagi B

## Domain Proyek

Proyek estimasi jumlah gol dalam liga dapat melibatkan penggunaan data historis dan analisis statistik untuk memprediksi jumlah gol yang mungkin terjadi selama musim kompetisi tertentu. Dengan mengintegrasikan data seperti performa tim dan pemain, kecenderungan gol pada pertandingan sebelumnya.

## Business Understanding

Dapat membantu para analis dan penggemar sepak bola untuk mendapatkan informasi data historis dan statistik pada club club terkait

Bagian laporan ini mencakup:

### Problem Statements

Aksesibilitas informasi gol secara real-time dan komprehensif untuk para analis dan penggemar sepak bola, menyediakan informasi gol yang dapat dipersonalisasi sesuai preferensi pengguna.

### Goals

Agar lebih mudah bagi para analis dan penggemar sepak bola dalam mencari informasi data historis dan statistik

    ### Solution statements
    - Menyediakan platform yang memungkinkan analisis mendalam terhadap tren dan pola terkait gol dalam berbagai kompetisi         sepak bola.
    - Mengembangkan model machine learning dengan menggunakan metode Regresi Linier.

## Data Understanding
Menggunakan dataset yang berasal dari kaggle yang berisi informasi mengenai jumlah gol, yang mencakup berbagai variabel yang berkaitan dengan olahraga sepak bola.<br> 
[top football leagues scores](https://www.kaggle.com/datasets/mohamedhanyyy/top-football-leagues-scorers/data)

Selanjutnya uraikanlah seluruh variabel atau fitur pada data. Sebagai contoh:  

### Variabel-variabel pada Heart Failure Prediction Dataset adalah sebagai berikut:
- Country : Negara yang menjalankan liga
- League : Pertandingan yang bersekala
- Club : Sebuah team
- Player Names : Nama Pemain
- Matches_Played : Jumlah pertandingan yang sudah dimainkan dalam kompetisi
- Substitution : Pemain yang masuk ke pertandingan untuk menggantikan pemain lain
- Mins : Durasi pertandingan
- Goals : Jumlah gol yang dicetak oleh para pemain
- xG : mengukur peluang seberapa besar suatu tembakan akan menghasilkan gol
- xG_Per_Avg_Match : jumlah rata-rata peluang gol yang diharapkan dalam setiap pertandingan
- Shots : Jumlah tembakan dihasilkan
- OnTarget : Jumlah tembakan yang diarahkan tepat ke gawang lawan
- Shots_Per_Avg_Match : Rata-rata jumlah percobaan tembakan yang dilakukan oleh seorang pemain dalam setiap pertandingan
- On_Target_Per_Avg_Match : rata-rata jumlah percobaan tembakan ke arah gawang lawan yang dilakukan oleh seorang pemain dalam setiap pertandingan.
- Year : Tahun dijalankannya liga (2016-2020)

## Data Preparation

## Data Collection

Untuk data yang digunakan menggunakan dataset dengan nama top footballleagues scores yang didapat di website kaggle.

## Data Discovery and Profiling

Dikarnakan menggunakan google collab maka harus mengimport file dan mengupload token yang di download dari kaggle terlebih dahulu agar bisa mendownload file dataset dari kaggle melalui google colab

```bash
from google.colab import files
files.upload()
```

## Modeling
Tahapan ini membahas mengenai model machine learning yang digunakan untuk menyelesaikan permasalahan. Anda perlu menjelaskan tahapan dan parameter yang digunakan pada proses pemodelan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan kelebihan dan kekurangan dari setiap algoritma yang digunakan.
- Jika menggunakan satu algoritma pada solution statement, lakukan proses improvement terhadap model dengan hyperparameter tuning. **Jelaskan proses improvement yang dilakukan**.
- Jika menggunakan dua atau lebih algoritma pada solution statement, maka pilih model terbaik sebagai solusi. **Jelaskan mengapa memilih model tersebut sebagai model terbaik**.

## Evaluation
Pada bagian ini anda perlu menyebutkan metrik evaluasi yang digunakan. Lalu anda perlu menjelaskan hasil proyek berdasarkan metrik evaluasi yang digunakan.

Sebagai contoh, Anda memiih kasus klasifikasi dan menggunakan metrik **akurasi, precision, recall, dan F1 score**. Jelaskan mengenai beberapa hal berikut:
- Penjelasan mengenai metrik yang digunakan
- Menjelaskan hasil proyek berdasarkan metrik evaluasi

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

## Deployment
pada bagian ini anda memberikan link project yang diupload melalui streamlit share. boleh ditambahkan screen shoot halaman webnya.

**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.

