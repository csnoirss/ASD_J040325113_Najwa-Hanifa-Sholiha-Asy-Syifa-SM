#===================================================================================
#Nama : Najwa Hanifa Sholiha Asy Syifa SM
#NIM : J0403251113
#Kelas : B2
#===================================================================================

def insertion_sort(data):
    # mulai dari indeks 1 karena indeks 0 dianggap sudah benar posisinya
    for i in range(1, len(data)):
        
        # simpan nilai yang mau disisipkan
        key = data[i]

        # posisi elemen sebelumnya
        j = i - 1

        # selama nilai sebelumnya lebih besar dari key, geser ke kanan
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]  # geser elemen ke kanan
            j -= 1  # pindah cek ke elemen sebelumnya

        # simpan key di posisi yang pas
        data[j + 1] = key

    # kembalikan data yang sudah urut
    return data
'''
1.Mengapa perulangan dimulai dari indeks 1?
Karena elemen pertama dianggap sudah “beres”. Jadi kita mulai ngatur dari elemen kedua.

2.Apa fungsi variabel key?
Variabel key dipakai buat menyimpan nilai yang lagi mau ditempatkan di posisi yang benar.

3.Mengapa digunakan while, bukan for?
Karena jumlah pergeseran tidak tentu. Jadi pakai while agar bisa berhenti kapan pun kalau sudah berketemu posisi yang pas.

4.Operasi apa yang terjadi di dalam while?
Elemen-elemen yang lebih besar dari key digeser ke kanan sampai ketemu tempat yang pas untuk key.
'''
