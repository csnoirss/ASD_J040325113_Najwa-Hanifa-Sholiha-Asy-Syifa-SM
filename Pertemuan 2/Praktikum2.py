#==================================================
# Praktikum 2 : Konsep ADT dan File Handling
# Latihan 1 : Membuat fungsi load data
#==================================================

nama_file = "data_mahasiswa.txt"

def baca_data_mahasiswa(nama_file):
    data_dict = {}  # inisialisasi dictionary kosong

    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()  # hilangkan newline
            parts = baris.split(",")

            # pastikan datanya benar (harus ada 3 bagian)
            if len(parts) != 3:
                continue  # skip baris yang tidak valid

            nim, nama, nilai_str = parts

            # simpan ke dictionary
            data_dict[nim] = {
                "nama": nama,
                "nilai": int(nilai_str)
            }

    return data_dict


# panggil fungsi
#buka_data = baca_data_mahasiswa(nama_file)
#print("Jumlah data terbaca:", len(buka_data))

#==================================================
#Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 2 : Membuat fungsi menampilkan data
#==================================================

def tampilkan_data_mahasiswa(data_dict):

    if len(data_dict) == 0:
        print("Data mahasiswa kosong.")
        return
    #membuayt header tabel
    print("\n===Data Mahasiswa===")
    print(f"{'NIM' : <10} | {'Nama' : <12} | {'Nilai' : >5}")
    print("-" * 32) #membuat garis header

    """
    untuk tampilan yang rapi, atur f-string formating 
        {'NIM' : <10} artinya:
        tampilkan nim <= rata kiri dengan 10 karaketer
        {'Nama' : <12} artinya:
        tampilkan nama <= rata kiri dengan 12 karaketer
        {'Nilai' : >5} artinya: 
        tampilkan nilai >= rata kanan dengan 5 karaketer
    """
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim : <10} | {nama : <12} | {nilai : >5}")

#memanggil fungsi menampilkan data
#tampilkan_data_mahasiswa(buka_data)
        

#==================================================
# Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 3 : Membuat fungsi mencari data
#==================================================

def cari_data(data_dict):
    # mencari data mahasiswa berdasarkan NIM
    nim_cari = input("\nMasukkan NIM yang ingin dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("\n==== Data Mahasiswa Ditemukan ====")
        print(f"NIM   : {nim_cari}")
        print(f"Nama  : {nama}")
        print(f"Nilai : {nilai}")
    else:
        print("\nData tidak ditemukan.")

# Memanggil fungsi cari data
#cari_data(buka_data)


#==================================================
# Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 4 : Membuat fungsi update nilai
#==================================================

def update_nilai(data_dict):
    
    # mengupdate nilai mahasiswa berdasarkan NIM
    nim = input("Masukkan NIM mahasiswa yang akan diupdate nilainya: ").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan. updat edibatalkan")
        return
    try:
        nilai_baru = int(input("Masukkan nilai baru: ").strip())
    except ValueError:
        print("Nilai harus berupa angka.")
        return
    
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0 hingga 100. Update dibatalkan.")
        return
    
    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update Berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}.")

#update_nilai(buka_data)

#==================================================
# Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 5 : Membuat fungsi menyimpan perubahan data ke file
#==================================================

def simpan_data_mahasiswa(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            baris = f"{nim},{nama},{nilai}\n"
            file.write(baris)

#simpan_data_mahasiswa(nama_file,buka_data)
#print("Data berhasil di simpan ke file.")


#==================================================
# Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 6 : Membuat Menu Program
#==================================================

def main():

    #menjalankan fungsi 1 load data
    buka_data = baca_data_mahasiswa(nama_file)

    while True:
        print("\n=== MENU DATA MAHASISWA ===")
        print("1. Tampilkan Data Mahasiswa") #fungsi no.2
        print("2. Cari Data Mahasiswa") #fungsi no.3
        print("3. Update Nilai Mahasiswa") #fungsi no.4
        print("4. Simpan Data Mahasiswa") #fungsi no.5
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == "1":
            tampilkan_data_mahasiswa(buka_data)

        elif pilihan == "2":
            cari_data(buka_data)

        elif pilihan == "3":
            update_nilai(buka_data)

        elif pilihan == "4":
            simpan_data_mahasiswa(nama_file, buka_data)
            print("Data berhasil disimpan.")

        elif pilihan == "5":
            print("Terima kasih telah menggunakan program ini.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()