#===========================================================
# Nama : Najwa Hanifa Sholiha Asy Syifa SM
# NIM : J0403251113
# Kelas : B2
# Praktikum 12:  - Graph II: Shortest Path
#===========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur 
#=========================================================== 

# representasi graph berbobot (kayak peta, tapi tiap jalan ada nilainya)
graph = { 
    'A': {'B': 4, 'C': 2},   # dari A ke B = 4, ke C = 2
    'B': {'D': 5},           # dari B ke D = 5
    'C': {'D': 1},           # dari C ke D = 1
    'D': {}                  # D udah tujuan akhir
} 

# hitung total bobot jalur pertama (A -> B -> D)
jalur_1 = graph['A']['B'] + graph['B']['D'] 

# hitung total bobot jalur kedua (A -> C -> D)
jalur_2 = graph['A']['C'] + graph['C']['D'] 

# nampilin hasil masing-masing jalur
print("Jalur 1: A -> B -> D =", jalur_1) 
print("Jalur 2: A -> C -> D =", jalur_2) 

# bandingin mana yang lebih kecil
if jalur_1 < jalur_2: 
    print("Jalur terpendek adalah A -> B -> D") 
else: 
    print("Jalur terpendek adalah A -> C -> D") 


#===========================================================
# Jawaban Analisis
#===========================================================

# 1. Berapa total bobot jalur A -> B -> D?
# Total bobot jalur A -> B -> D adalah 9, yang didapat dari penjumlahan bobot
# dari A ke B sebesar 4 dan dari B ke D sebesar 5.

# 2. Berapa total bobot jalur A -> C -> D?
# Total bobot jalur A -> C -> D adalah 3, yaitu dari A ke C sebesar 2 dan
# dari C ke D sebesar 1.

# 3. Jalur mana yang dipilih sebagai jalur terpendek?
# Jalur yang dipilih adalah A -> C -> D karena memiliki total bobot yang lebih
# kecil dibandingkan jalur A -> B -> D.

# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah langkah paling sedikit?
# Karena yang menjadi patokan utama adalah total bobot, bukan jumlah langkah.
# Sebuah jalur memungkinkan memiliki langkah yang lebih sedikit, tetapi jika
# bobotnya besar maka hasilnya tetap lebih lama dibandingkan jalur lain yang
# memiliki lebih banyak langkah namun bobotnya lebih kecil