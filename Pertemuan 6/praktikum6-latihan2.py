#===================================================================================
#Nama : Najwa Hanifa Sholiha Asy Syifa SM
#NIM : J0403251113
#Kelas : B2
#===================================================================================

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        # kondisi ascending → selama data sebelumnya lebih besar dari key
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        # menempatkan key di posisi yang benar
        data[j + 1] = key

    return data

'''
versi descending

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        # kondisi descending → selama data sebelumnya lebih kecil dari key
        while j >= 0 and data[j] < key:
            data[j + 1] = data[j]
            j -= 1

        # menempatkan key di posisi yang benar
        data[j + 1] = key

    return data
'''