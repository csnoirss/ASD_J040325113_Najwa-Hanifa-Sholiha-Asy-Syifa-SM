# ==========================================================
# TUGAS HANDS-ON MODUL 1 
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)

# Nama  : Najwa Hanifa Sholiha Asy Syifa SM
# NIM   : J0403251113
# Kelas : B2
# ==========================================================
nama_file = "stok_barang.txt"

# ----------------------------------------------------------
# Fungsi: Membaca data stok dari file
# ----------------------------------------------------------
def baca_stok(nama_file): #Membaca data stok dari file dan mengembalikan sebagai dictionary.
    stok_dict = {}

    try:
        with open(nama_file, "r", encoding="utf-8") as f:
            for baris in f:
                baris = baris.strip()

                if baris == "":
                    continue

                parts = baris.split(",")
                if len(parts) != 3:
                    continue

                kode, nama, stok_str = parts

                try:
                    stok_int = int(stok_str)
                except ValueError:
                    continue

                stok_dict[kode] = {
                    "nama": nama,
                    "stok": stok_int
                }
    except FileNotFoundError: # Jika file tidak ada → stok kosong
        pass

    return stok_dict

# ----------------------------------------------------------
# Fungsi: Menyimpan data ke file
# ----------------------------------------------------------
def simpan_stok(nama_file, stok_dict): #Menyimpan ulang seluruh data stok ke file.
    with open(nama_file, "w", encoding="utf-8") as f:
        for kode in sorted(stok_dict.keys()):
            nama = stok_dict[kode]["nama"]
            stok = stok_dict[kode]["stok"]
            f.write(f"{kode},{nama},{stok}\n")

# ----------------------------------------------------------
# Fungsi: Menampilkan semua data
# ----------------------------------------------------------
def tampilkan_semua(stok_dict): #Menampilkan seluruh barang dalam format tabel rapi.
    if len(stok_dict) == 0:
        print("Stok barang kosong.")
        return

    print("\n=== DAFTAR STOK BARANG ===")
    print(f"{'Kode':<10} | {'Nama Barang':<15} | {'Stok':>5}")
    print("-" * 36)

    for kode in sorted(stok_dict.keys()):
        nama = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]
        print(f"{kode:<10} | {nama:<15} | {stok:>5}")

# ----------------------------------------------------------
# Fungsi: Cari barang berdasarkan kode
# ----------------------------------------------------------
def cari_barang(stok_dict):
    kode = input("Masukkan kode barang: ").strip()

    if kode in stok_dict:
        barang = stok_dict[kode]
        print("\n=== BARANG DITEMUKAN ===")
        print(f"Kode : {kode}")
        print(f"Nama : {barang['nama']}")
        print(f"Stok : {barang['stok']}")
    else:
        print("Barang tidak ditemukan.")

# ----------------------------------------------------------
# Fungsi: Tambah barang baru
# ----------------------------------------------------------
def tambah_barang(stok_dict):
    kode = input("Masukkan kode barang baru: ").strip()

    if kode in stok_dict:
        print("Kode sudah digunakan. Tambah dibatalkan.")
        return

    nama = input("Masukkan nama barang: ").strip()

    try:
        stok_awal = int(input("Masukkan stok awal: ").strip())
    except ValueError:
        print("Stok harus berupa angka.")
        return

    stok_dict[kode] = {"nama": nama, "stok": stok_awal}

    print(f"Barang '{nama}' berhasil ditambahkan.")

# ----------------------------------------------------------
# Fungsi: Update stok barang
# ----------------------------------------------------------
def update_stok(stok_dict):
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()

    if kode not in stok_dict:
        print("Kode barang tidak ditemukan.")
        return

    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")

    pilihan = input("Masukkan pilihan (1/2): ").strip()

    try:
        jumlah = int(input("Masukkan jumlah perubahan stok: ").strip())
    except ValueError:
        print("Jumlah harus berupa angka.")
        return

    if pilihan == "1":
        stok_dict[kode]["stok"] += jumlah
        print("Stok berhasil ditambah.")

    elif pilihan == "2":
        if stok_dict[kode]["stok"] - jumlah < 0:
            print("Stok tidak boleh negatif. Update dibatalkan.")
            return
        stok_dict[kode]["stok"] -= jumlah
        print("Stok berhasil dikurangi.")
    else:
        print("Pilihan tidak valid.")

# ----------------------------------------------------------
# Program Utama
# ----------------------------------------------------------
def main():
    # Load data dari file
    stok_barang = baca_stok(nama_file)

    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_semua(stok_barang)

        elif pilihan == "2":
            cari_barang(stok_barang)

        elif pilihan == "3":
            tambah_barang(stok_barang)

        elif pilihan == "4":
            update_stok(stok_barang)

        elif pilihan == "5":
            simpan_stok(nama_file, stok_barang)
            print("Data berhasil disimpan.")

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()