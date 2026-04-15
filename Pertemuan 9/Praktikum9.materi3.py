#===================================================================================
# Nama : Najwa Hanifa Sholiha Asy Syifa SM
# NIM : J0403251113
# Kelas B2
#===================================================================================
# Latihan 3 : Membuat Traversal Preorder
#===================================================================================

#class node digunakan untuk dasar seperti tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#fungsi preorder : root ==> left ==> right
def preorder(node):
    if node is not None:
        print(node.data, end=" ") 
        preorder(node.left) 
        preorder(node.right)

#membuat tree
#membuat root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#menjalankan traversal preorder
print("Traversal Preorder:")
preorder(root)

#===================================================================================
#Penjelasan :
#Kode ini membuat struktur tree dengan root "A", lalu menambahkan "B" dan "C" sebagai child, 
#serta "D" dan "E" sebagai child dari "B". Selain itu, terdapat fungsi preorder untuk 
#menelusuri tree dengan urutan root, kiri, kanan, dan di akhir fungsi tersebut dipanggil 
#untuk menampilkan hasil traversal.
#===================================================================================