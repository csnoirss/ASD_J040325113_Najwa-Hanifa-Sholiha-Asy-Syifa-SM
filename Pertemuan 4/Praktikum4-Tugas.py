#===================================================================================
#Nama : Najwa Hanifa Sholiha Asy Syifa SM
#NIM : J0403251113
#Kelas : B2
#===================================================================================

#===================================================================================
# Studi Kasus : Sistem Antrian Bengkel Motor
# Implementasi Queue menggunakan Linked List
# FIFO (First In First Out)
#===================================================================================


# 1. Mendefinisikan Node (unit dasar Linked List)
class Node:
    def __init__(self, nomor_antrian, nama, jenis_servis):
        self.nomor_antrian = nomor_antrian   # Nomor antrian pelanggan
        self.nama = nama                     # Nama pelanggan
        self.jenis_servis = jenis_servis     # Jenis servis motor
        self.next = None                     # Pointer ke node berikutnya


# 2. Mendefinisikan Queue
class QueueBengkel:
    def __init__(self):
        self.front = None   # Menunjuk pelanggan terdepan
        self.rear = None    # Menunjuk pelanggan terakhir
        self.nomor = 1      # Penomoran antrian otomatis

    # Mengecek apakah antrian kosong
    def is_empty(self):
        return self.front is None

    # Menambahkan pelanggan ke antrian (Enqueue)
    def enqueue(self, nama, jenis_servis):
        nodeBaru = Node(self.nomor, nama, jenis_servis)

        # Jika antrian kosong
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
        else:
            # Jika antrian sudah ada
            self.rear.next = nodeBaru
            self.rear = nodeBaru

        print(f"Pelanggan {nama} masuk antrian nomor {self.nomor}")
        self.nomor += 1

    # Melayani pelanggan terdepan (Dequeue)
    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong, tidak ada pelanggan.")
            return None

        pelanggan_dilayani = self.front
        self.front = self.front.next

        # Jika setelah dilayani antrian kosong
        if self.front is None:
            self.rear = None

        return pelanggan_dilayani

    # Menampilkan seluruh antrian
    def tampilkan(self):
        if self.is_empty():
            print("Antrian masih kosong.")
            return

        print("\nDaftar Antrian Pelanggan (Front -> Rear):")
        current = self.front
        while current:
            print(f"No: {current.nomor_antrian} | Nama: {current.nama} | Servis: {current.jenis_servis}")
            current = current.next


#===================================================================================
# Program Utama
#===================================================================================

def main():
    q = QueueBengkel()

    while True:
        print("\n=== Sistem Antrian Bengkel ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilihan = input("Pilih Menu (1-4): ").strip()

        if pilihan == "1":
            nama = input("Masukkan Nama Pelanggan: ").strip()
            jenis_servis = input("Masukkan Jenis Servis: ").strip()
            q.enqueue(nama, jenis_servis)

        elif pilihan == "2":
            pelanggan = q.dequeue()
            if pelanggan:
                print(f"Pelanggan nomor {pelanggan.nomor_antrian} ({pelanggan.nama}) sedang dilayani untuk servis {pelanggan.jenis_servis}.")

        elif pilihan == "3":
            q.tampilkan()

        elif pilihan == "4":
            print("Program selesai. Terima kasih.")
            break

        else:
            print("Pilihan tidak valid.")


# Menjalankan program
if __name__ == "__main__":
    main()