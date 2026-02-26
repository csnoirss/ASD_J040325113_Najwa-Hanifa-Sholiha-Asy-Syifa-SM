#===================================================================================
#Nama : Najwa Hanifa Sholiha Asy Syifa SM
#NIM : J0403251113
#Kelas : B2
#===================================================================================

#===================================================================================
# Studi Kasus: Generator PIN (Backtracking)
#===================================================================================

def buat_pin(panjang, hasil=""):

    # Base case:
    # Jika panjang PIN sudah sesuai dengan yang diminta
    # maka PIN ditampilkan
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return

    # Dicetak saat fungsi mulai diproses (alur masuk)
    print("Masuk fungsi - PIN sementara:", hasil)

    # Pilihan angka yang bisa digunakan
    for angka in ["0", "1", "2"]:
        # Explore kemungkinan berikutnya
        buat_pin(panjang, hasil + angka)

    # Dicetak saat kembali (backtracking)
    print("Kembali (backtrack) dari:", hasil)


# Memulai pembuatan PIN dengan panjang 3 digit
buat_pin(3)