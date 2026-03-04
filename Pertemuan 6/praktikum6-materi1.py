#===================================================================================
#Nama : Najwa Hanifa Sholiha Asy Syifa SM
#NIM : J0403251113
#Kelas : B2
#===================================================================================

#===================================================================================
#Intersection Sort (ascending)
#===================================================================================

def intersection_sort(data):
    #loop mulai dari data ke 2 (index array ke 1)
    for i in range(1, len(data)):

        key = data[i] #simpan nilai yang disisipkan
        j = i - 1 #index elemen terakhir di bagian kiri

        #geser
        while j >= 0 and data[j] > key:
            data[j+1] = data[j] #geser elemen ke kanan
            j -= 1 
        #sisipkan key ke posisi yang benar
        data[j+1] = key
    return data
angka = [7,8,5,2,4,6]
print("Hasil Sorting: ", intersection_sort(angka))

