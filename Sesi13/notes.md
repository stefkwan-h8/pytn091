## Guide Pengolahan Data

0. Misalkan file adalah file csv, atau excel, kita bisa buka raw file nya untuk melihat apakah ada data yang bisa kita rapiin

1. import data
    - biasanya kumasukkan ke dalam sebuah DataFrame supaya mudah dilihat, mudah dibaca.

2. data handling
    1. data cleaning
        - missing values, dihapus atau diisi, atau kalau mau dibiarkan, berikan penjelasan kenapa dibiarkan
        - invalid values, kalau ada data yang tidak masuk akal, kita hapus atau kita ganti
        - data types, misalkan kolom tanggal kita ubah jadi tipe data datetime. kolom angka kalau data type object, berarti ada yang bukan angka di kolom tersebut, bisa dicari dan dihapus, baru kolom data tersebut kita convert jadi type number: int / float.
        - ganti judul kolom
    2. data exploration
        - kita coba cari pattern/ pola dalam data kita. Bisa dengan teknik agregasi, statistik deskriptif, visualisasi
        - misalkan scatter plot untuk mencari korelasi dua set data, misal 1 fitur dengan target.
        - coba cari insight supaya lebih familiar dengan data yang ada, dan kita bisa tau kira2 ekspektasi bentuk data ini seperti apa.
        - setelah lebih familiar dengan data, kita bisa membuat pertanyaan (kalau di assignment pertanyaan sudah dibuatkan)
        - mau menambah/ mengurangi jumlah kolom boleh
        - mau memilih fitur yang akan digunakan sebagai training data
    3. data preparation
        - encoding, data tipe text diubah jadi numerik
        - scaling, data antar para fitur kita ubah untuk memiliki skala yang sama
        - split, pisahkan data jadi 2 grup: train data, dan test data

3. pilih dan latih model
    - gunakan data train untuk melatih model

4. evaluasi
    - pilih metric untuk evaluasi model (regression R squared, classification confusion matrix)
    - gunakan data test untuk mengevaluasi model

5. tuning
    - balik ke step 1-4 untuk mencoba "tweak" model nya biar lebih akurat. * jangan bergantuk pada accuracy saja karena...


Model regression bisa kena issue overfitting. akurasi sangat tinggi tapi begitu kita pakai untuk test data, atau data yang bukan di dalam train data, dia tidak bisa prediksi dengan baik.

Model classification bisa berat sebelah atau tidak punya keahlian memprediksi kategori tertentu. Semua hasil model ini selalu jenis A, jenis B tidak pernah ditebak. Walaupun akurasi tinggi, ini bukan model yang membuat prediksi dengan baik.
