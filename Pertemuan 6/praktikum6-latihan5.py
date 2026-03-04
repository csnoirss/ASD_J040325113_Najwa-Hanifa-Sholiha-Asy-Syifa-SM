#===================================================================================
#Nama : Najwa Hanifa Sholiha Asy Syifa SM
#NIM : J0403251113
#Kelas : B2
#===================================================================================

def merge(left, right):
    result = []
    i = 0
    j = 0

    # selama masih ada elemen di kedua list
    while i < len(left) and j < len(right):
        # kondisi ascending → ambil nilai yang lebih kecil dulu
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # tambahkan sisa elemen yang belum masuk
    result.extend(left[i:])
    result.extend(right[j:])

    return result
'''
2.Jelaskan fungsi result.extend().
result.extend() digunakan untuk menambahkan semua elemen dari list lain 
ke dalam list result secara langsung tanpa perlu memasukkan satu per satu.
'''