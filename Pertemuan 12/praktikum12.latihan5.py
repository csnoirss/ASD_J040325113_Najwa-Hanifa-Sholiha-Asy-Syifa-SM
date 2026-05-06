#===========================================================
# Nama : Najwa Hanifa Sholiha Asy Syifa SM
# NIM : J0403251113
# Kelas : B2
# Praktikum 12:  - Graph II: Shortest Path
# ==========================================================
# Studi Kasus: Jalur Terpendek Antar Kota
# Algoritma: Dijkstra
# ==========================================================

import heapq  # buat priority queue (biar ambil jarak paling kecil dulu)

# representasi graph berbobot (kayak peta antar kota)
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},   # Bogor ke Jakarta = 5, ke Depok = 2
    'Depok': {'Jakarta': 2, 'Bandung': 6}, # Depok ke Jakarta = 2, ke Bandung = 6
    'Jakarta': {'Bandung': 7},             # Jakarta ke Bandung = 7
    'Bandung': {}                          # Bandung tujuan akhir
}

def dijkstra(graph, start):
    # nyiapin jarak awal (semua dianggap jauh banget)
    distances = {node: float('inf') for node in graph}
    
    # jarak dari start ke dirinya sendiri = 0
    distances[start] = 0
    
    # priority queue (jarak, node)
    priority_queue = [(0, start)]

    # selama masih ada yang diproses
    while priority_queue:
        
        # ambil node dengan jarak paling kecil
        current_distance, current_node = heapq.heappop(priority_queue)

        # kalau jaraknya udah bukan yang terbaik, skip
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

    # balikin hasil
    return distances

# node awal (sesuai soal: dari Bogor)
start_node = 'Bogor'

# jalankan algoritma
hasil = dijkstra(graph, start_node)

# nampilin hasil
print("Jarak terpendek dari Bogor:")
for kota, jarak in hasil.items():
    print("Bogor ->", kota, "=", jarak)


# ==========================================================
# Jawaban Analisis
# ==========================================================

# 1. Node awal yang digunakan apa?
# Node awal yang digunakan adalah Bogor, karena dari soal diminta mencari
# jarak terpendek dari Bogor ke kota lainnya.

# 2. Node mana yang memiliki jarak paling kecil dari node awal?
# Node dengan jarak paling kecil adalah Depok dengan jarak 2,
# karena langsung dari Bogor ke Depok.

# 3. Node mana yang memiliki jarak paling besar dari node awal?
# Node dengan jarak paling besar adalah Bandung dengan jarak 8,
# karena harus melalui beberapa jalur sebelum sampai ke sana.

# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
# Algoritma Dijkstra bekerja dengan cara memilih node dengan jarak paling kecil
# terlebih dahulu, lalu mengecek semua tetangganya untuk mencari kemungkinan
# jalur yang lebih pendek. Pada kasus ini, dari Bogor akan dicek ke Depok dan Jakarta,
# lalu dari Depok ditemukan jalur lebih cepat ke Jakarta dan Bandung. Proses ini
# terus dilakukan sampai semua node mendapatkan jarak terpendeknya.