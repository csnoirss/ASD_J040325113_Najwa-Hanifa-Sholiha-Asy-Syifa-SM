#===================================================================================
#Nama : Najwa Hanifa Sholiha Asy Syifa SM
#NIM : J0403251113
#Kelas : B2
#===================================================================================

#===================================================================================
# Latihan 3: Rekursi pada List (Mencari Nilai Maksimum)
#===================================================================================

def cari_maks(data, index=0):

    # Base case:
    # Jika sudah berada di elemen terakhir list,
    # maka langsung kembalikan nilai tersebut
    if index == len(data) - 1:
        print("Base case tercapai di index:", index, "nilai:", data[index])
        return data[index]

    # Dicetak saat fungsi mulai diproses (alur masuk)
    print("Masuk fungsi - index:", index, "nilai:", data[index])

    # Panggil fungsi rekursif untuk mengecek sisa elemen
    maks_sisa = cari_maks(data, index + 1)

    # Membandingkan nilai sekarang dengan hasil dari rekursi
    if data[index] > maks_sisa:
        hasil = data[index]
    else:
        hasil = maks_sisa

    # Dicetak saat fungsi selesai diproses (alur keluar)
    print("Keluar fungsi - index:", index, "maks sementara:", hasil)

    return hasil


# Data list angka
angka = [3, 7, 2, 9, 5]

# Memanggil fungsi
print("Nilai maksimum:", cari_maks(angka))