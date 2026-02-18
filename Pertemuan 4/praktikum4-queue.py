#================================================
#Nama    : Najwa Hanifa Sholiha Asy Syifa SM
#NIM     : J0403251113
#Kelas   : TPL B
#================================================

#================================================
#Implementasi Dasar : ???
#================================================

#Membuat class NOde (merupakan unit dasar linked list)
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai/data
        self.next = None #pointer ke note berikutnya (awal=none) 

#Queue dengan 2 pointer : front dan rear
class QueueLL:
    def __init__(self):
        self.front = None #pointer ke depan (awal)
        self.rear = None  #pointer ke belakang (akhir)

    def is_empty(self):
        return self.front is None
    
    def enqueue(self, data):
        #menambah data ke belakang (rear)
        nodeBaru = Node(data)

    
        #Jika queue kosong, front dan rear menunjuk ke node baru
        if self.rear is None:
            self.front = nodeBaru
            self.rear = nodeBaru
        else:
            #Jika queue tidak kosong, rear.next menunjuk ke node baru
            self.rear.next = nodeBaru
            #Pindah rear ke node baru
            self.rear = nodeBaru

    def dequeue(self):
        #menghapus data dari depan (front)


        #1)lihat data yang paling depan
        data_terhapus = self.front.data
        
        #2)geser front ke node berikutnya
        self.front = self.front.next

        #3) JIka setelah dihapus queue menjadi kosong, rear juga harus di set ke none
        if self.front is None: #jika setelah dihapus queue menjadi kosong
            self.rear = None #rear juga harus di set ke none

        return data_terhapus

    def tampilkan(self):
        #menampilkan isi queue dari front ke rear
        current = self.front
        print("Front -> ", end="")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("Rear")

#instantiasi objek class QueueLL
q = QueueLL()

q.enqueue("A")
q.enqueue("B")
q.enqueue("c")
q.tampilkan()

q.dequeue()
q.tampilkan()