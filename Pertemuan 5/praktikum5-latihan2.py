#===================================================================================
#Nama : Najwa Hanifa Sholiha Asy Syifa SM
#NIM : J0403251113
#Kelas : B2
#===================================================================================

#===================================================================================
# Latihan 2: Tracing Rekursi
#===================================================================================

def countdown(n):
    # Base case:
    # Jika n sudah 0, hentikan rekursi
    if n == 0:
        print("Selesai")
        return

    # Dicetak saat fungsi mulai diproses (alur masuk)
    print("Masuk:", n)

    # Panggil fungsi yang sama dengan n dikurangi 1
    countdown(n - 1)

    # Dicetak saat fungsi selesai diproses (alur keluar)
    print("Keluar:", n)


# Memulai countdown dari angka 3
countdown(3)