#==============================================
# Fungsi untuk membaca dataset dari file txt
#==============================================
def read_data(path):
    data_dict = {}  # dictionary kosong untuk menampung data barang

    try:
        # buka file dalam mode read
        with open(path,"r",encoding="utf-8") as file:
            # baca file baris demi baris
            for baris in file:

                # hilangkan newline di akhir baris
                baris = baris.strip("\n")

                # pecah berdasarkan koma 
                kode_brg, nama_brg, stok_brg = baris.split(",")

                # ubah stok dari string menjadi integer
                stok_brg = int(stok_brg)

                # simpan ke dictionary dengan kode sebagai key
                data_dict[kode_brg] = {
                    "nama_brg":nama_brg,
                    "stok_brg":stok_brg
                }

            # kembalikan dictionary hasil baca file
            return data_dict

    # jika file belum ada, buat dataset kosong
    except FileNotFoundError:
        print("File tidak ditemukan, memuat dataset baru")
        return {}



#==============================================
# Fungsi untuk menampilkan dataset ke tabel
#==============================================
def print_data(data):

    # cek apakah dataset kosong
    if (len(data) == 0):
        print("Dataset masih kosong")
        return

    # header tabel
    print("\n============= DAFTAR BARANG =============")
    print(f"{'KODE':10} | {'NAMA':<12} | {'STOK':>5}")
    print("-"*40)

    # tampilkan data terurut berdasarkan kode
    for kode in sorted(data):

        # ambil nilai dari dictionary bertingkat
        nama = data[kode]["nama_brg"]
        stok = data[kode]["stok_brg"]

        # format kolom rapi
        print(f"{kode:10} | {nama:<12} | {stok:>5}")



#==============================================
# Fungsi untuk mencari data berdasarkan kode
#==============================================
def search_data(data):

    # guard clause jika dataset kosong
    if (len(data) == 0):
        print("Dataset masih kosong")
        return

    # loop interaktif agar bisa cari berulang
    while(True):

        choice = input("Cari Data ?[Y/N] : ").upper().strip()

        if choice == "N":
            break

        elif choice == "Y":

            # input kode yang ingin dicari
            searched_code = input("Masukkan Kode barang yang ingin dicari : ")

            # cek apakah kode ada di dictionary
            if searched_code in data:

                print("Data Ditemukan ")

                # ambil isi data
                nama = data[searched_code]["nama_brg"]
                stok = data[searched_code]["stok_brg"]

                # tampilkan tabel satu baris
                print("\n============= DAFTAR BARANG =============")
                print(f"{'KODE':10} | {'NAMA':<12} | {'STOK':>5}")
                print("-"*40)
                print(f"{searched_code:10} | {nama:<12} | {stok:>5}\n")

            else:
                # FIX: sebelumnya tidak tercetak
                print("Data tidak ditemukan")

        else:
            print("Input Sesuai Format")
            continue



#==============================================
# Fungsi untuk menambah barang ke dataset
#==============================================
def add_data(data):

    # tampilkan data agar user tahu kondisi awal
    print_data(data)

    while(True):

        choice = input("Tambahkan Barang Baru? [Y/N] : ").upper().strip()

        if choice == "N":
            break

        elif choice == "Y":

            # ===== input kode barang =====
            while(True):
                kode_baru = input("Input kode barang : ")

                # validasi unik
                if kode_baru in data:
                    print("Kode Sudah Tersedia, Input Kode Lain")
                    continue

                # tidak boleh kosong
                elif not kode_baru:
                    print("Kode Tidak Boleh Kosong")
                    continue

                # validasi prefix
                elif kode_baru[:3] != "BRG":
                    print("Kode Harus memiliki Prefix BRG")
                    continue

                else:
                    break

            # ===== input nama barang =====
            while(True):
                nama_baru = input("Input nama barang : ").strip()

                if not nama_baru:
                    print("Nama Tidak Boleh Kosong")
                    continue
                else:
                    break

            # ===== input stok =====
            while(True):
                try:
                    stok_baru = int(input("Input stok barang : ").strip())

                    # stok tidak boleh negatif
                    if stok_baru < 0:
                        print("Stok Tidak Boleh minus")
                        continue

                except ValueError:
                    print("Input Harus Berupa Angka")
                    continue

                break

            # simpan ke dictionary utama
            data[kode_baru] = {
                "nama_brg":nama_baru,
                "stok_brg":stok_baru
            }

            print(f"Barang {nama_baru} dengan kode {kode_baru} ditambahkan \n")

        else:
            print('Input Sesuai Format')
            continue



# ==============================================
# Fungsi Update Stok barang
# ==============================================
def update_stok(data):

    # guard jika kosong
    if (len(data) == 0):
        print("Dataset masih kosong")
        return

    # tampilkan data dulu
    print_data(data)

    while(True):

        choice = input("Update Data ? [Y/N] : ").upper().strip()

        if choice == "N":
            break

        elif choice =="Y":

            while(True):

                updated_code = input("Input Kode barang untuk update stok : ").strip()

                if not updated_code:
                    print("Tidak boleh kosong")
                    continue

                elif updated_code not in data:
                    print("Data Tidak Ditemukan, Masukkan Kode yang valid")
                    continue

                # jika kode valid
                print("Stok saat ini : ",data[updated_code]["stok_brg"])

                try:
                    while(True):

                        updated_stok = int(input("Masukkan Stok Baru : ").strip())

                        if updated_stok < 0:
                            print("Stok Harus >= 0")
                            continue

                        break

                except ValueError:
                    print("Nilai stok harus berupa angka")
                    continue

                # tampilkan perubahan sebelum overwrite
                print(
                    f"Berhasil merubah stok "
                    f"{data[updated_code]['nama_brg']} "
                    f"dari {data[updated_code]['stok_brg']} "
                    f"menjadi {updated_stok}"
                )

                # update nilai di dictionary (mutable, langsung berubah)
                data[updated_code]["stok_brg"] = updated_stok
                break

        else:
            print("Masukkan Input Sesuai Format")
            continue



# ==============================================
# Fungsi Save Data ke file
# ==============================================
def save_data(path,data):

    # buka file mode write  menimpa isi lama
    with open(path,"w",encoding="utf-8") as file:

        # loop seluruh data
        for kode in data:

            nama_brg = data[kode]["nama_brg"]
            stok_brg = data[kode]["stok_brg"]

            # tulis format CSV
            file.write(f"{kode},{nama_brg},{stok_brg}\n")

    print("File Tersimpan")



# ==============================================
# Program Utama : Menu Interaktif
# ==============================================
def main():

    # path file dataset
    file_path = "stok_barang.txt"

    # baca dataset saat program mulai
    data_brg = read_data(file_path)

    # daftar menu valid
    menu = ("1","2","3","4","5","0")

    # loop menu utama
    while(True):

        print("\n===== Manajemen Gudang ======")
        print("[1] Tampilkan Semua Barang")
        print("[2] Cari Barang")
        print("[3] Tambah Barang Baru")
        print("[4] Update Stok Barang")
        print("[5] Simpan File")
        print("[0] Keluar")

        choice = input("Pilih Menu : ").strip()

        # validasi input menu
        if choice not in menu:
            print("Input Sesuai Format")
            continue

        elif choice == "1":
            print_data(data_brg)

        elif choice == "2":
            search_data(data_brg)

        elif choice == "3":
            add_data(data_brg)

        elif choice == "4":
            update_stok(data_brg)

        elif choice == "5":
            save_data(file_path,data_brg)

        elif choice =="0":
            print("Exit")
            break   # FIX: agar benar-benar keluar


# titik masuk program
if __name__ == "__main__":
    main()
