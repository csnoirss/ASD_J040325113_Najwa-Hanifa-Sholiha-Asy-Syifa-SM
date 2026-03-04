#===================================================================================
#Nama : Najwa Hanifa Sholiha Asy Syifa SM
#NIM : J0403251113
#Kelas : B2
#===================================================================================

from heapq import merge


def merge_sort(data):
    # jika datanya cuma 0 atau 1 elemen, langsung balikan (sudah pasti urut)
    if len(data) <= 1:
        return data

    # cari titik tengah untuk membagi list jadi dua bagian
    mid = len(data) // 2

    # bagian kiri
    left = data[:mid]
    # bagian kanan
    right = data[mid:]

    # rekursif: urutkan bagian kiri
    left_sorted = merge_sort(left)
    # rekursif: urutkan bagian kanan
    right_sorted = merge_sort(right)

    # gabungkan dua bagian yang sudah terurut
    return merge(left_sorted, right_sorted)

'''
1.Apa yang dimaksud dengan base case?
Base case adalah kondisi berhenti saat rekursi.
Di merge sort, base case-nya adalah ketika list berisi 0 atau 1 elemen, karena itu sudah pasti urut.

2.Mengapa fungsi memanggil dirinya sendiri?
Karena merge sort memakai rekursi untuk memecah list jadi bagian kecil.
List dibagi terus sampai ketemu base case.

3.Apa tujuan fungsi merge()?
Fungsi merge() dipakai buat menggabungkan dua list yang sudah terurut menjadi satu list yang terurut.
'''