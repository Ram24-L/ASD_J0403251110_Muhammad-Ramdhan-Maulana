# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Muhammad Ramdhan Maulana
# NIM     : J0403251110
# Kelas   : TPL-B2
# ==============================================================================

# 1. FILE HANDLING & DICTIONARY (Sub-CPMK 1) [cite: 31]
def muat_data_buku(nama_file):
    """
    Fungsi untuk membaca 'buku.txt' dan menyimpannya ke Dictionary.
    Format file: kode_buku,judul,harga
    """
    database_buku = {}
    try:
        with open("buku.txt","r", encoding="utf-8") as files:
            for lines in files:
                data = lines.strip()
                kode_buku,judul_buku,harga_buku = data.split(",")
                database_buku[kode_buku] = {
                    "judul_buku":judul_buku,
                    "harga_buku":harga_buku
                }
                
    except FileNotFoundError:
        with open("buku.txt","w", encoding="utf-8") as files:
            return {}
    
    # TODO: Implementasikan kode pembacaan file di sini
    return database_buku

#membuat fungsi untuk memvisualisasikan data buku
def tampilkan_data_buku(data_buku = {}):


    # Membuat tabel otomatis tanpa mentok dari data buku
    data = [["Kode Buku", "Judul Buku", "Harga Buku"]] + [[kode, info["judul_buku"], info["harga_buku"]] for kode, info in data_buku.items()]
    # Hitung lebar kolom
    col_widths = [max(len(str(row[i])) for row in data) for i in range(len(data[0]))]

    # Mencetak iterasi tabel dengan kalkulasi panjang kolom secara otomatis
    for row in data:
        print(" | ".join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row)))
        if row == data[0]:
            print("=" * (sum(col_widths) + 3 * (len(col_widths) - 1)))

            

# 2. LINKED LIST - MANAJEMEN PROMOSI (Sub-CPMK 2) [cite: 32]
class Node:
    def __init__(self, judul):
        #Data dasar awal
        self.judul = judul
        self.next = None

class LinkedListPromosi:
    def __init__(self):
         self.head = None

    def tambah_buku_promosi(self, judul):
        """Menambahkan buku ke daftar promosi (Linked List)"""
        # Penambahan node ke linked list
        #Membuat node baru dengan judul
        new_node = Node(judul)
            #Membuat kondisi jika head masih kosong, maka node baru menjadi head
        if self.head is None:
            self.head = new_node    
        else:
            #Jika tidak kosong maka node baru akan ditambahkan di akhir linked list
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node 
              

    def tampilkan_promosi(self):
        """Menampilkan semua buku dalam daftar promosi"""
        # TODO: Implementasikan traversal linked list
        # Buat variabel sementara untuk menyimpan node saat ini, mulai dari head
        current = self.head
        print("\nDaftar Promosi Buku:")
        # Jika masih terdapat judul buku yang ada, maka akan terus 
        # menampilkan judul buku tersebut hingga tidak ada lagi
        while current:
            print(current.judul,end=" -> ")
            current = current.next
        print("None")

# 3. QUEUE - ANTIREAN KASIR (Sub-CPMK 3) [cite: 33]
class AntreanKasir:
    def __init__(self):
        self.antrean = []

    def tambah_antrean(self, nama_pelanggan):
        """Menambah antrean (Enqueue)"""
        # TODO: Implementasikan prinsip FIFO
        self.antrean.append(nama_pelanggan)

    def layani_pelanggan(self):
        """Menghapus antrean (Dequeue)"""
        # TODO: Implementasikan prinsip FIFO
        if self.antrean:
            return self.antrean.pop(0)
        else:
            return None
    #Layani prioritas (Inisiatif)
    def layani_prioritas(self,nama_pelanggan):
        """Menghapus antrean berdasarkan nama"""
        if self.antrean:
            return self.antrean.remove(nama_pelanggan)
        else:
            return self.antrean
    
    #Membuat fungsi untuk menampilkan antrian (Inisiatif)
    def tampilkan_antrian(self):
        length = len(self.antrean)
        print("Daftar Antrian : ")
        for i in range(length):
            print(self.antrean[i],end=" <- ")
        print("None")

#Fungsi merge sort manual
def merge_sort(data):
    #Base case dari merge sort
    if len(data) <= 1:
        return data
    #Tentukan poin titik tengah
    tengah = len(data) // 2
    #Belah data menjadi kiri dan kanan secara recursive
    #Hingga base case tercapai
    kiri = merge_sort(data[:tengah])
    kanan = merge_sort(data[tengah:])
    return merge(kiri, kanan)

#Fungsi merge untuk menggabungkan kiri dan kanan
def merge(kiri, kanan):
    #Membuat data kosong untuk menyatukan kembali list yang telah terbagi
    merged = []
    i, j = 0, 0
    #Logika pengulangan sambil menyusun list kembali
    while i < len(kiri) and j < len(kanan):
        if kiri[i] < kanan[j]:
            merged.append(kiri[i])
            i += 1
        else:
            merged.append(kanan[j])
            j += 1
    #Memastikan semua data yang telah terurut ikut tergabung
    merged.extend(kiri[i:])
    merged.extend(kanan[j:])
    return merged

# 4. SORTING - LAPORAN TRANSAKSI (Sub-CPMK 4) [cite: 34]
def urutkan_transaksi(list_harga):
    """
    Mengurutkan list harga secara manual menggunakan 
    Insertion Sort atau Merge Sort.
    """ 
    # TODO: Implementasikan algoritma sorting secara manual
    # Fungsi manual nya ada di atas
    list_harga = merge_sort(list_harga)
    return list_harga

# ==============================================================================
# MAIN PROGRAM - MENU ANTARMUKA
# ==============================================================================
def main():
    # Inisialisasi Data
    file_db = "buku.txt"
    data_buku = muat_data_buku(file_db)
    list_promosi = LinkedListPromosi()
    antrean_toko = AntreanKasir()
    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]

    while True:
        print("\n--- SISTEM MANAJEMEN TOKO BUKU ---")
        print("1. Lihat Katalog Buku (Dictionary/File)")
        print("2. Kelola Daftar Promosi (Linked List)")
        print("3. Kelola Antrean Kasir (Queue)")
        print("4. Lihat Laporan Penjualan Terurut (Sorting)")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            tampilkan_data_buku(data_buku)
        
        elif pilihan == '2':
            judul_baru = input("Masukkan judul buku untuk promosi: ")
            list_promosi.tambah_buku_promosi(judul_baru)
            list_promosi.tampilkan_promosi()

        elif pilihan == '3':
            #Inisiatif menambah fitur sistem antrian
            #Fitur menampilkan antrian
            #Fitur melayani antrian
            while(True):
                #Menu
                print("========Kelola Antrian Pelanggan=======")
                print("[1] Tambah Antrian")
                print("[2] Layani Antrian")
                print("[3] Tampilkan Antrian")
                print("[4] Layani Prioritas ")
                print("[5] Kembali")
                pilihan2 = input("Pilih Menu [1-5] : ")
                #Menambah antrian
                if pilihan2 == "1":
                    nama = input("Nama Pelanggan: ")
                    antrean_toko.tambah_antrean(nama)
                    print(f"Antrian dengan nama {nama} ditambah")
                #Melayani antrian
                elif pilihan2 == "2":
                    pelanggan_dilayani = antrean_toko.layani_pelanggan()
                    if pelanggan_dilayani:
                        print(f"Pelanggan yang dilayani: {pelanggan_dilayani}")
                    else:
                        print("Tidak ada pelanggan dalam antrean.")
                #Menampilkan antrian
                elif pilihan2 == "3":
                    antrean_toko.tampilkan_antrian()
                #Melayani antrian prioritas
                elif pilihan2 == "4":
                    prioritas = input("Masukkan Nama Prioritas : ")
                    antrean_toko.layani_prioritas(prioritas)
                    print(f"Prioritas dengan nama : {prioritas}, sudah dilayani")
                elif pilihan2 =="5":
                    break
                
            

            # Tambahkan logika untuk melayani jika diperlukan
            
            

        elif pilihan == '4':
            print("Harga Sebelum Urut:", riwayat_transaksi)
            hasil_sort = urutkan_transaksi(riwayat_transaksi)
            print("Harga Sesudah Urut:", hasil_sort)

        elif pilihan == '5':
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()