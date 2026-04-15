#===================================================================================
# Nama : Najwa Hanifa Sholiha Asy Syifa SM
# NIM : J0403251113
# Kelas B2
#===================================================================================
# Latihan 2 : Membuat Binary Search Sederhana
#===================================================================================

#class node digunakan untuk dasar seperti tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #c kanan
def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

#membuat root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#menampilkan isi node
print("data pada root", root.data)
print("data child kiri root", root.left)
print("data child kanan root", root.right)
print("data child kiri child kiri root", root.left.left.data)
print("data child kanan child kiri root", root.left.right.data)

#===================================================================================
#Penjelasan :
#Kode ini membuat struktur tree dengan root "A", lalu menambahkan child "B" dan "C", 
#serta "D" dan "E" sebagai child dari "B". Terdapat juga fungsi preorder untuk 
#menelusuri tree, tetapi belum digunakan, dan di akhir hanya menampilkan beberapa data node.    
#===================================================================================