#===================================================================================
# Nama : Najwa Hanifa Sholiha Asy Syifa SM
# NIM : J0403251113
# Kelas : B2
#===================================================================================

#===================================================================================
# implementasi BFS (Breadth First Search)
#===================================================================================
#struktur data untuk membuat antrian, kita gunakan dari library collections bawaan python
from collections import deque

#representasi graph menggunakan dictionary
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],        
    'G': []
}

def bfs(graph,start):
    #fungsi untuk melakukan Breadth First Search pada graph
    #graph : dictionary yang merepresentasikan graph
    #start : node awal untuk memulai pencarian

    #variable yang digunakan untuk menyimpan node yang sudah dikunjungi dan antrian untuk node yang akan dikunjungi
    visited = set() #set untuk menyimpan node yang sudah dikunjungi

    #queue digunakan untuk menyimpan node yang akan dikunjungi, kita mulai dengan menambahkan node awal ke dalam antrian
    queue = deque([start]) #antrian untuk menyimpan node yang akan dikunjungi

    #masukan node awal ke dalam antrian
    queue.append(start) #tambahkan node awal ke dalam antrian

    #tandai node awal sebagai sudah dikunjungi
    visited.add(start) 

    while queue:
        #mengambil node dari antrian dan memeriksa apakah sudah dikunjungi atau belum
        node = queue.popleft() #mengambil node dari antrian

        print(node,end="") #menampilkan node yang sedang dikunjungi

        for neighbor in graph[node]: #periksa tetangga dari node yang sedang dikunjungi
            if neighbor not in visited: #jika tetangga belum dikunjungi

                visited.add(neighbor) #tandai tetangga sebagai sudah dikunjungi

                queue.append(neighbor) #tambahkan tetangga ke dalam antrian

#menjalankan fungsi bfs dengan node awal 'A'
bfs(graph, 'A')