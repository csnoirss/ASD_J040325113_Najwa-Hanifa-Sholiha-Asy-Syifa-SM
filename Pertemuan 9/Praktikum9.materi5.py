#===================================================================================
# Nama : Najwa Hanifa Sholiha Asy Syifa SM
# NIM : J0403251113
# Kelas B2
#===================================================================================
# Latihan 5 : Membuat Traversal Postorder
#===================================================================================

#class node digunakan untuk dasar seperti tree
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat traversal postorder : left -> right -> root
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")

#membuat tree
#membuat root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#menjalankan traversal postorder
print("Hasil Traversal postorder:", end=" ")
postorder(root)

#===================================================================================
#Penjelasan :
#Kode ini membuat struktur tree dengan root "A", lalu menambahkan "B" dan "C" sebagai child, 
#serta "D" dan "E" sebagai child dari "B". Selain itu, terdapat fungsi postorder untuk 
#menelusuri tree dengan urutan kiri, kanan, lalu root, dan di akhir fungsi tersebut dipanggil 
#untuk menampilkan hasil traversal.
#===================================================================================