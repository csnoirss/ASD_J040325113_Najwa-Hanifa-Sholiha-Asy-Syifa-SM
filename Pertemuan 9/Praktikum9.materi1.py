#===================================================================================
# Nama : Najwa Hanifa Sholiha Asy Syifa SM
# NIM : J0403251113
# Kelas B2
#===================================================================================
# Latihan 1 : Membuat Node
#===================================================================================

#class node digunakan untuk dasar seperti tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #c kanan

#membuat root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#menampilkan isi node
print("data pada root", root.data)
print("data child kiri root", root.left)
print("data child kanan root", root.right)

#===================================================================================
#Penjelasan :
#Kode ini menunjukkan cara membuat struktur tree sederhana dengan class Node, 
# di mana setiap node punya data serta child kiri dan kanan. Saya membuat root dengan 
# nilai "A", lalu menambahkan "B" sebagai child kiri dan "C" sebagai child kanan. 
# Di akhir, saya menampilkan data pada root, sementara child yang ditampilkan masih 
# berupa objek karena belum diakses nilai .data-nya.         
#===================================================================================