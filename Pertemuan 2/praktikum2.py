#===========================================
# Praktikum 2 : Konsep ADT dan file Handling 
# Latihan 1  : Membuat Fungsi Load Data
#===========================================

nama_file = "data.txt"

def baca_file(file):
    data_dict = {}
    try:
        with open(file,"r",encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip("\n")
                nim,nama,nilai = baris.split(",")
                data_dict[nim] = {
                    "nama" : nama,
                    "nilai" : nilai
                }
    except(FileNotFoundError):
        print("File TIidak ada")
    return data_dict


#========================================================
# Praktikum 2 : Konsep ADT dan File Handling (Stuedi Kasus)
# Latihan 2 : Membuat Fungsi Menampilkan data
#========================================================

def tampilkan_data(data):
    #Membuat Header Tabel
    if len(data) == 0:
        print("Data Tidak Ada")
        return
    
    print("\n=========== Daftar Mahasiswa ===========")
    print(f"{'NIM':10} | {'Nama':<12} | {'Nilai':>5}")
    print("-"*40)

    for nim in sorted(data):
        nama = data[nim]["nama"]
        nilai = data[nim]["nilai"]
        print(f"{nim:10} | {nama:<12} | {nilai:>5}")

def cari_data(data):
    if len(data) == 0:
        print("Data Tidak Ada")
        return
    search = input("Masukkan NIM yang ingin dicari : ").strip().upper()

    if search in data:
        nim = search
        nama = data[search]["nama"]
        nilai = data[search]["nilai"]

        print("========= Data Mahasiswa ========")
        print("Data Ditemukan")
        print("NIM : ", nim)
        print("Nama : ",nama)
        print("Nilai",nilai)
        return
    else:
        print("Data Tidak Ditemukan")


def update_nilai(data):
    nim = input("Masukkan NIM yang ingin diupdate datanya : ").strip().upper()
    if nim in data:
        nama = data[nim]["nama"]
        nilai = data[nim]["nilai"]
        print("====== Data Ditemukan =======")
        print("NIM : ", nim)
        print("Nama : ",nama)
        print("Nilai",nilai)
        print("========= Update Data ========")
        try:
            nilai_baru = int(input("Masukkan Nilai Baru (0-100) : "))
        except ValueError:
            print("Nilai Harus Berupa Angka")

        if (nilai_baru < 0 or nilai_baru > 100):
            print("Nilai Harus antara 0 sampai 100, Update Dibatalkan")
            return
        
        data[nim]["nilai"] = nilai_baru
        print(f"Update Berhasil. Nilai {nim} berubah dari {nilai} menjadi {nilai_baru}")
    else:
        print("Data Tidak ditemukan")
        return

def simpan_data(path,data):
    try:
        with open(path,"w",encoding = "utf-8") as file:
            for nim in sorted(data.keys()):
                nama = data[nim]["nama"]
                nilai = data[nim]["nilai"]
                file.write(f"{nim},{nama},{nilai}\n")
            print("Data Tersimpan")
    except FileNotFoundError:
        print("Data Tidak ada")


def main():

    #Menjalankan fungsi 1 load data : 
    data = baca_file(nama_file)
    while True:
        print("====== Program Mahasiswa =====")
        print("[1] Tampilkan Data")
        print("[2] Cari Data")
        print("[3] Update Data")
        print("[4] Simpan Data yang telah diubah")
        print("[0] Keluar Program")
        valid_opt = (1,2,3,4,0)
        try:
            pilihan = int(input("Input Perintah : ").strip())
            if pilihan in valid_opt:
                if pilihan == 1:
                    tampilkan_data(data)
                elif pilihan == 2:
                    cari_data(data)
                elif pilihan == 3:
                    update_nilai(data)
                elif pilihan == 4 :
                    simpan_data(nama_file,data)
                elif pilihan == 0:
                    exit()
            else:
                print("Input Tidak valid")
                continue
        except ValueError:
            print("Pilihan Tidak Valid")


if __name__ == "__main__":
    main() 
