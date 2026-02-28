
#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

# ==========================================================
# Tugas Hands-On: Sistem Antrian Bengkel Motor
# Menggunakan Queue berbasis Linked List
# ==========================================================

# ==========================================================
# Class Node
# Merepresentasikan satu pelanggan dalam antrian
# ==========================================================
class Node:
    def __init__(self, no, nama, servis):
        self.no = no            # Nomor antrian pelanggan
        self.nama = nama        # Nama pelanggan
        self.servis = servis    # Jenis servis
        self.next = None        # Pointer ke node berikutnya


# ==========================================================
# Class QueueBengkel
# Mengelola antrian menggunakan konsep FIFO
# ==========================================================
class QueueBengkel:
    def __init__(self):
        self.front = None   # Pointer ke pelanggan terdepan
        self.rear = None    # Pointer ke pelanggan terakhir

    # ======================================================
    # Method enqueue()
    # Menambahkan pelanggan ke belakang antrian
    # ======================================================
    def enqueue(self, no, nama, servis):
        new_node = Node(no, nama, servis)  # Membuat node baru

        # Jika antrian kosong
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            # Sambungkan node terakhir ke node baru
            self.rear.next = new_node
            # Geser pointer rear ke node baru
            self.rear = new_node

        print(">> Pelanggan berhasil ditambahkan ke antrian.")

    # ======================================================
    # Method dequeue()
    # Melayani pelanggan terdepan (FIFO)
    # ======================================================
    def dequeue(self):
        # Jika antrian kosong
        if self.front is None:
            print(">> Antrian kosong, tidak ada pelanggan.")
            return

        # Simpan data pelanggan terdepan
        print("\n>> Melayani Pelanggan:")
        print("No Antrian :", self.front.no)
        print("Nama       :", self.front.nama)
        print("Servis     :", self.front.servis)

        # Geser pointer front ke node berikutnya
        self.front = self.front.next

        # Jika setelah dequeue antrian menjadi kosong
        if self.front is None:
            self.rear = None

    # ======================================================
    # Method tampilkan()
    # Menampilkan seluruh data antrian (Traversal)
    # ======================================================
    def tampilkan(self):
        # Jika antrian kosong
        if self.front is None:
            print(">> Antrian masih kosong.")
            return

        print("\n===== Daftar Antrian Bengkel =====")

        current = self.front  # Mulai dari depan
        while current is not None:  # Traversal sampai akhir
            print("---------------------------------")
            print("No Antrian :", current.no)
            print("Nama       :", current.nama)
            print("Servis     :", current.servis)
            current = current.next  # Pindah ke node berikutnya

        print("---------------------------------")


# ==========================================================
# Program Utama (Menu Interaktif)
# ==========================================================
def main():
    q = QueueBengkel()  # Membuat objek Queue

    while True:
        print("\n=== Sistem Antrian Bengkel ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            no = input("No Antrian : ")
            nama = input("Nama       : ")
            servis = input("Servis     : ")
            q.enqueue(no, nama, servis)

        elif pilih == "2":
            q.dequeue()

        elif pilih == "3":
            q.tampilkan()

        elif pilih == "4":
            print(">> Program selesai. Terima kasih.")
            break

        else:
            print(">> Pilihan tidak valid.")


# ==========================================================
# Menjalankan Program
# ==========================================================
if __name__ == "__main__":
    main()