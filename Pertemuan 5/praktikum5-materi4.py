#===================================================================================
#Nama : Najwa Hanifa Sholiha Asy Syifa SM
#NIM : J0403251113
#Kelas : B2
#===================================================================================

#===================================================================================
#Materi Rekursif :  Backtracking kombinasi biner
#===================================================================================

def biner(n, hasil=""):
    # Base case: jika panjang string sudah n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return
    
    # Choose + Explore: tambah '0'
    biner(n, hasil + "0")
    
    # Choose + Explore: tambah '1'
    biner(n, hasil + "1")

biner(3)