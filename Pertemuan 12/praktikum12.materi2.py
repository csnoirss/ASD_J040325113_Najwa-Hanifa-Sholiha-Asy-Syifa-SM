#===================================================================================
# Nama : Najwa Hanifa Sholiha Asy Syifa SM
# NIM : J0403251113
# Kelas : B2
#===================================================================================

#===================================================================================
# Materi 2 
#===================================================================================

def bellman_ford(graph, start): 
    
    # nyiapin tempat buat nyimpen jarak awal (semua dianggap jauh banget dulu)
    distances = {node: float('inf') for node in graph} 
    
    # node awal jaraknya 0 karena kita mulai dari sini
    distances[start] = 0 
    
    # relaksasi dilakukan sebanyak (jumlah node - 1)
    # kenapa? karena maksimal edge terpanjang itu segitu
    for _ in range(len(graph) - 1): 
        
        # looping tiap node di graph
        for node in graph: 
            
            # cek semua tetangga dari node tersebut
            for neighbor, weight in graph[node].items(): 
                
                # kalau jarak lewat node ini lebih pendek
                if distances[node] + weight < distances[neighbor]: 
                    
                    # update jarak jadi yang lebih kecil
                    distances[neighbor] = distances[node] + weight 
    
    # balikin hasil jarak terpendek
    return distances