#===========================================================
# Nama : Najwa Hanifa Sholiha Asy Syifa SM
# NIM : J0403251113
# Kelas : B2
# Praktikum 12:  - Graph II: Shortest Path
#===========================================================
# Latihan 2: Implementasi Dijkstra 
#========================================================== 

import heapq  # buat priority queue (biar ambil jarak paling kecil dulu)
from tracemalloc import start  # ini sebenernya ga kepake, tapi ya udah gapapa 😆

# weighted graph (semua bobotnya positif)
graph = { 
    'A': {'B': 4, 'C': 2},   # A ke B = 4, A ke C = 2
    'B': {'D': 5},           # B ke D = 5
    'C': {'D': 1},           # C ke D = 1
    'D': {}                  # D tujuan akhir
} 

def dijkstra(graph, start): 
    """ 
    untuk mencari jarak terpendek dari node start 
    ke seluruh node lain pakai algoritma Dijkstra
    """ 
    
    # semua jarak awal dianggap jauh banget (tak hingga)
    distances = {node: float('inf') for node in graph} 
    
    # jarak dari start ke dirinya sendiri = 0
    distances[start] = 0 
    
    # priority queue isinya (jarak, node)
    priority_queue = [(0, start)]

    # selama masih ada yang diproses
    while priority_queue: 
        
        # ambil node dengan jarak paling kecil
        current_distance, current_node = heapq.heappop(priority_queue) 
 
        # kalau jaraknya lebih besar dari yang udah disimpan, skip aja
        if current_distance > distances[current_node]: 
            continue 
 
        # cek semua tetangga dari node sekarang
        for neighbor, weight in graph[current_node].items(): 
            
            # hitung jarak baru
            distance = current_distance + weight 
 
            # kalau lebih kecil, update
            if distance < distances[neighbor]: 
                distances[neighbor] = distance 
                
                # masukin ke queue lagi biar diproses
                heapq.heappush(priority_queue, (distance, neighbor)) 
 
    # balikin semua jarak terpendek
    return distances 
 
# manggil fungsi dari node A
hasil = dijkstra(graph, 'A') 

# nampilin hasil
print("Jarak terpendek dari node A:") 
for node, distance in hasil.items(): 
    print(node, "=", distance)


#===========================================================
# Jawaban Analisis
#===========================================================

# 1. Berapa jarak terpendek dari A ke B?
# Jarak terpendek dari A ke B adalah 4, karena langsung dari A ke B tanpa jalur lain.

# 2. Berapa jarak terpendek dari A ke C?
# Jarak terpendek dari A ke C adalah 2, karena langsung dari A ke C.

# 3. Berapa jarak terpendek dari A ke D?
# Jarak terpendek dari A ke D adalah 3, yaitu lewat jalur A -> C -> D (2 + 1).

# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
# Karena kalau lewat B totalnya jadi 4 + 5 = 9, sedangkan lewat C cuma 2 + 1 = 3.
# Jadi walaupun sama-sama sampai D, jalur lewat C lebih kecil bobotnya.

# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
# Priority queue dipakai buat milih node dengan jarak paling kecil dulu.
# Jadi algoritma ini selalu fokus ke jalur yang paling cepat dulu, bukan asal jalan.

# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
# Karena Dijkstra menganggap jarak yang sudah kecil itu final.
# Kalau ada bobot negatif, bisa aja nanti ada jalur yang lebih pendek lagi,
# jadi hasilnya bisa salah atau ga akurat.