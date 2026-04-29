#===================================================================================
# Nama : Najwa Hanifa Sholiha Asy Syifa SM
# NIM : J0403251113
# Kelas : B2
#===================================================================================

#===================================================================================
# Latihan 1 
#===================================================================================

"""
Jawaban Analisis Latihan 1 
 1. Node yang dikunjungi pertama kali adalah 'Rumah'. Hal ini karena 'Rumah' 
    ditentukan sebagai titik awal (start node) saat memanggil fungsi bfs.
 2. BFS cocok untuk mencari jalur terdekat karena cara kerjanya yang 
    mengeksplorasi "level demi level". Karena itu, BFS akan mengecek semua node di 
    jarak terdekat dahulu sebelum pindah ke level yang lebih jauh. Jadi, 
    jalur yang pertama kali ditemukan dipastikan adalah yang paling pendek.
 3. Urutan kunjungan akan berubah jika urutan penulisan node tetangga di dalam 
    list graph diganti. Meskipun secara level sama, BFS akan memproses 
    tetangga berdasarkan urutan mereka di dalam antrean (queue).
"""