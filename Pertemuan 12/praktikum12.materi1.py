#===================================================================================
# Nama : Najwa Hanifa Sholiha Asy Syifa SM
# NIM : J0403251113
# Kelas : B2
#===================================================================================
#===================================================================================
# Materi 1 
#===================================================================================

import heapq  # buat priority queue (biar yang jaraknya paling kecil diproses dulu)

graph = { 
    'A': {'B': 4, 'C': 2},  # dari A ke B = 4, ke C = 2
    'B': {'D': 5},          # dari B ke D = 5
    'C': {'D': 1},          # dari C ke D = 1
    'D': {}                 # D ga punya tetangga lagi
}

def dijkstra(graph, start): 
    # nyiapin dictionary buat nyimpen jarak terpendek dari start ke semua node
    distances = {node: float('inf') for node in graph} 
    
    # set jarak node awal jadi 0 (karena mulai dari situ)
    distances[start] = 0 
    
    # priority queue, isinya (jarak, node)
    pq = [(0, start)] 
    
    # selama masih ada yang bisa diproses di queue
    while pq: 
        # ambil node dengan jarak paling kecil
        current_distance, current_node = heapq.heappop(pq) 
        
        # cek semua tetangga dari node sekarang
        for neighbor, weight in graph[current_node].items(): 
            
            # hitung jarak baru ke tetangga
            distance = current_distance + weight 
            
            # kalau jarak baru lebih kecil dari yang sebelumnya
            if distance < distances[neighbor]: 
                
                # update jarak yang lebih kecil itu
                distances[neighbor] = distance 
                
                # masukin ke queue biar nanti diproses lagi
                heapq.heappush(pq, (distance, neighbor)) 
    
    # balikin hasil semua jarak terpendek
    return distances 

# manggil fungsi dari node A
hasil = dijkstra(graph, 'A') 

# nampilin hasilnya
print(hasil)
