#===================================================================================
# Nama : Najwa Hanifa Sholiha Asy Syifa SM
# NIM : J0403251113
# Kelas B/P2
#===================================================================================
# Latihan 6 : Struktur organisasi perusahaan
#===================================================================================

#class node digunakan untuk dasar seperti tree
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan
   
# Fungsi untuk traversal preorder
def preorder(node):
    if node is not None:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

#membuat tree struktur organisasi perusahaan
root = Node("Direktur")

#child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

#child level 2
root.left.left = Node("Staff1")
root.left.right = Node("Staff2")

root.right.right = Node("Staff3")

#menjalankan traversal preorder 
print("Struktur Organisasi (Preorder):")
preorder(root)

#===================================================================================
#Penjelasan :
#Kode ini membuat struktur tree untuk merepresentasikan organisasi perusahaan, 
#dengan "Direktur" sebagai root, lalu "Manajer A" dan "Manajer B" sebagai child, 
#serta beberapa staff di bawahnya. Selain itu, terdapat fungsi preorder untuk 
#menelusuri tree dengan urutan root, kiri, kanan, dan di akhir fungsi tersebut 
#dipanggil untuk menampilkan struktur organisasi.
#===================================================================================