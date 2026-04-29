#===================================================================================
# Nama : Najwa Hanifa Sholiha Asy Syifa SM
# NIM : J0403251113
# Kelas : B2
#===================================================================================

#===================================================================================
# Latihan 2 
#===================================================================================

"""
Jawaban Analisis Latihan 2 ---
 1. DFS masuk ke node terdalam terlebih dahulu karena menggunakan sistem Rekursif.
    Algoritma ini akan terus menelusuri satu cabang sampai tidak ada 
    lagi node yang bisa dikunjungi, baru kemudian kembali ke 
    atas untuk mengeksplorasi cabang lainnya.
 2. Jika urutan neighbor diubah, maka urutan penelusuran jalurnya akan berubah 
    drastis. DFS sangat bergantung pada urutan list tetangga; jalur mana yang 
    ditulis lebih dulu, itulah yang akan dijelajahi sampai ke dasar.
 3. Perbandingannya, BFS cenderung "melebar" dan mengecek semua tetangga 
    langsung dari sebuah node, sedangkan DFS cenderung "mendalam" dengan 
    menyelesaikan satu jalur eksplorasi hingga ujung sebelum pindah ke jalur lain.
"""