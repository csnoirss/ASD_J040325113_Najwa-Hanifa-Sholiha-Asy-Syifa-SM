#===================================================================================
#Nama : Najwa Hanifa Sholiha Asy Syifa SM
#NIM : J0403251113
#Kelas : B2
#===================================================================================

#===================================================================================
# Latihan 1: Rekursi Pangkat
#===================================================================================

def pangkat(a, n):
    # Base case:
    # Jika pangkat sudah 0, kembalikan 1 (karena a^0 = 1)
    if n == 0:
        return 1

    # Recursive case:
    # Mengalikan a dengan hasil pangkat(a, n-1)
    # sehingga a^n = a * a^(n-1)
    return a * pangkat(a, n - 1)

# Memanggil fungsi untuk menghitung 2^4
print(pangkat(2, 4))   # Output: 16