#===========================================================
# Nama : Najwa Hanifa Sholiha Asy Syifa SM
# NIM : J0403251113
# Kelas : B2
# Praktikum 12:  - Graph II: Shortest Path
# ========================================================== 
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus 
# Algoritma: Dijkstra 
# ========================================================== 

import heapq  # buat priority queue (ambil yang jaraknya paling kecil dulu)

# graph lokasi kampus (tiap edge itu waktu tempuh dalam menit)
graph = { 
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},  # dari Gerbang ke Perpus 6 menit, ke Kantin 2 menit
    'Perpustakaan': {'Lab': 3},                   # dari Perpus ke Lab 3 menit
    'Kantin': {'Lab': 4, 'Aula': 7},              # dari Kantin ke Lab 4 menit, ke Aula 7 menit
    'Lab': {'Aula': 1},                           # dari Lab ke Aula 1 menit
    'Aula': {}                                    # Aula tujuan akhir
} 

def dijkstra(graph, start): 
    # nyiapin jarak awal (semua dianggap jauh dulu)
    distances = {node: float('inf') for node in graph} 
    
    # jarak dari start ke dirinya sendiri = 0
    distances[start] = 0 
    
    # priority queue (jarak, node)
    priority_queue = [(0, start)] 

    # selama masih ada yang diproses
    while priority_queue: 
        
        # ambil node dengan jarak paling kecil
        current_distance, current_node = heapq.heappop(priority_queue) 

        # kalau ternyata jaraknya udah bukan yang terbaik, skip
        if current_distance > distances[current_node]: 
            continue 

        # cek semua tetangga
        for neighbor, weight in graph[current_node].items():
            
            # hitung jarak baru
            distance = current_distance + weight 
            
            # kalau lebih kecil, update
            if distance < distances[neighbor]: 
                distances[neighbor] = distance 
                
                # masukin ke queue lagi
                heapq.heappush(priority_queue, (distance, neighbor)) 

    # balikin hasil akhir
    return distances 

# mulai dari Gerbang
hasil = dijkstra(graph, 'Gerbang') 

# nampilin hasil
print("Jarak terpendek dari Gerbang Kampus:") 
for lokasi, jarak in hasil.items(): 
    print(lokasi, "=", jarak, "menit")


# ==========================================================
# Jawaban Analisis
# ==========================================================

# 1. Lokasi mana yang paling dekat dari Gerbang?
# Lokasi yang paling dekat dari Gerbang adalah Kantin dengan waktu 2 menit,
# karena itu jalur dengan bobot paling kecil dari titik awal.

# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
# Waktu tercepat dari Gerbang ke Aula adalah 7 menit,
# yaitu lewat jalur Gerbang -> Kantin -> Lab -> Aula (2 + 4 + 1).

# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
# Tidak selalu. Contohnya dari Gerbang ke Aula, kalau langsung lewat Kantin ke Aula
# itu 2 + 7 = 9 menit, tapi kalau lewat Lab jadi 2 + 4 + 1 = 7 menit.
# Jadi jalur yang lebih panjang bisa aja lebih cepat kalau bobotnya lebih kecil.

# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
# Karena semua bobotnya positif (waktu tempuh ga mungkin negatif),
# jadi Dijkstra bisa bekerja dengan optimal dan cepat untuk cari jalur tercepat.