#===================================================================================
#Nama : Najwa Hanifa Sholiha Asy Syifa SM
#NIM : J0403251113
#Kelas : B2
#===================================================================================

#===================================================================================
#Materi Rekursif : Call Stack
# Tracing bilangan (masuk-keluar)
# input 3
# 3-2-1 | 1-2-3  
#===================================================================================

def hitung(n):

    #base case
    if n == 0:
        print("Selesai")
        return 1
    
    print("Masuk : ", n) #menunjukkan nilai n saat masuk ke fungsi
    hitung(n-1) #recursive case
    print("Keluar", n)

print("========Program Tracing========")
hitung(3)
    