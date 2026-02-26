#===================================================================================
#Nama : Najwa Hanifa Sholiha Asy Syifa SM
#NIM : J0403251113
#Kelas : B2
#===================================================================================

#===================================================================================
# Latihan 4: Backtracking Dasar (Kombinasi Huruf A dan B)
#===================================================================================

def kombinasi(n, hasil=""):

    # Base case:
    # Jika panjang hasil sudah sama dengan n,
    # maka kombinasi sudah lengkap dan langsung ditampilkan
    if len(hasil) == n:
        print("Kombinasi ditemukan:", hasil)
        return

    # Dicetak saat fungsi mulai diproses (alur masuk)
    print("Masuk fungsi - hasil sementara:", hasil)

    # Choose & Explore huruf A
    kombinasi(n, hasil + "A")

    # Choose & Explore huruf B
    kombinasi(n, hasil + "B")

    # Dicetak saat fungsi selesai diproses (alur keluar / backtracking)
    print("Kembali (backtrack) dari:", hasil)


# Memulai kombinasi dengan panjang 2
kombinasi(2)