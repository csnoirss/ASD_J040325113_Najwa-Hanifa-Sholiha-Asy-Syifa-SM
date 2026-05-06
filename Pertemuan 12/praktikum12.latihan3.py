#===========================================================
# Nama : Najwa Hanifa Sholiha Asy Syifa SM
# NIM : J0403251113
# Kelas : B2
# Praktikum 12:  - Graph II: Shortest Path
# ========================================================== 
# Latihan 3: Implementasi Bellman-Ford 
# ========================================================== 
 
# weighted graph (di sini ada bobot negatif)
graph = { 
    'A': {'B': 5, 'C': 4},   # A ke B = 5, A ke C = 4
    'B': {},                 # B ga punya tetangga
    'C': {'B': -2}           # C ke B = -2 (ini yang negatif)
} 
 
def bellman_ford(graph, start): 
    """ 
    fungsi buat cari jarak terpendek dari node start 
    ke semua node lain pakai Bellman-Ford
    """ 
 
    # semua jarak awal dianggap jauh banget
    distances = {node: float('inf') for node in graph} 
 
    # jarak dari start ke dirinya sendiri = 0
    distances[start] = 0 
 
    # relaksasi dilakukan sebanyak jumlah node - 1
    for _ in range(len(graph) - 1): 
 
        # cek semua edge di graph
        for node in graph: 
            for neighbor, weight in graph[node].items(): 
 
                # kalau node ini udah punya jarak
                # dan ditemukan jalur lebih pendek ke neighbor
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]: 
                    
                    # update jarak ke yang lebih kecil
                    distances[neighbor] = distances[node] + weight 
 
    # balikin hasil akhir
    return distances 
 
# manggil fungsi dari node A
hasil = bellman_ford(graph, 'A') 
 
# nampilin hasil
print("Jarak terpendek dari node A:") 
for node, distance in hasil.items(): 
    print(node, "=", distance)


# ==========================================================
# Jawaban Analisis
# ==========================================================

# 1. Berapa bobot langsung dari A ke B?
# Bobot langsung dari A ke B adalah 5, sesuai dari graph yang ada.

# 2. Berapa total bobot jalur A -> C -> B?
# Total bobot jalur A -> C -> B adalah 4 + (-2) = 2.

# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
# Jalur yang lebih kecil adalah A -> C -> B dengan total bobot 2,
# dibandingkan jalur langsung A -> B yang bobotnya 5.

# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
# Karena Bellman-Ford mengecek semua kemungkinan jalur secara berulang,
# jadi walaupun ada bobot negatif tetap bisa menemukan hasil yang benar.

# 5. Apa yang dimaksud dengan proses relaksasi edge?
# Relaksasi itu proses ngecek apakah suatu jalur bisa dipersingkat.
# Kalau ternyata ada jalur yang lebih kecil, maka jaraknya di-update.

# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
# Dijkstra lebih cepat tapi cuma bisa dipakai kalau semua bobot positif.
# Sedangkan Bellman-Ford lebih fleksibel karena bisa handle bobot negatif,
# tapi prosesnya lebih lama karena harus ngecek berulang kali.