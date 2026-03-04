#===================================================================================
#Nama : Najwa Hanifa Sholiha Asy Syifa SM
#NIM : J0403251113
#Kelas : B2
#===================================================================================
'''
Buat program dengan menggunakan algoritma insertion sort
Tracing dengan data = [5, 2, 4, 6, 1, 3]
'''
data = [5, 2, 4, 6, 1, 3]

def insertion_sort(data):
    print("Data awal:", data)

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        print(f"\nIterasi i = {i} | key = {key}")

        # geser
        while j >= 0 and data[j] > key:
            print(f"  data[{j}] = {data[j]} lebih besar dari key → geser ke kanan")
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key
        print("  Hasil sementara:", data)

    print("\nData akhir (sudah urut):", data)

# jalankan
insertion_sort(data)

'''
1.Isi list setelah iterasi i = 1:
Hasil: [2, 5, 4, 6, 1, 3]

2.Isi list setelah iterasi i = 3:
Hasil: [2, 4, 5, 6, 1, 3]

3.Berapa kali pergeseran pada iterasi i = 4?
Terjadi 4 kali pergeseran
'''