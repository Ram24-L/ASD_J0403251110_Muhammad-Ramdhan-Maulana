#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
#Studi kasus : sistem antrain layanan Academic
#Implementasi Queue ->
# Enqueue : Memindahkan pointer rear (Menambah data baru di belakang dan mendaftarkan data baru tsb menjadi paling belakang)
# Dequeue : Memindahkan Pointer front (Menghapus data paling depan dan mendaftarkan front baru)
# Front -> A -> B -> C
#=============================================

#Mendefinisikan node (satuan data)
class Node:
    #queue akademik membutuhkan nim dan nama
    #Pembuatan data yang diperlukan di constructor
    def __init__(self,nim,nama):
        self.nim = nim
        self.nama = nama
        self.next = None

#Mendefinisikan queue akademik
class QueueAkademik:
    #Menginisialisasi antrian
    def __init__(self):
        #Pada awalnya, rear dan front None saat belum ada data
        self.rear = None
        self.front = None
    #Membuat fungsi untuk mengecek apakah queue kosong
    def is_empty(self):
        return self.front is None
    
    def Enqueue(self,nim,nama):
        node_baru = Node(nim,nama)
        if self.is_empty() == True:
            self.rear = node_baru
            self.front = node_baru
            return
        self.rear.next = node_baru
        self.rear = node_baru

    def dequeue(self):
        if self.is_empty() == True :
            print("Antrian Kosong")
            return
        node_dilayani = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        
        return node_dilayani

    def tampilkan(self):
        if self.is_empty() == True:
            print("Antrian Kosong")
            return
        node_saat_ini = self.front
        i = 1
        while(node_saat_ini is not None):
            print("================================")
            print(f"Antrian Mahasiswa ke-{i}")
            print("NIM : ",node_saat_ini.nim)
            print("Nama : ",node_saat_ini.nama)
            node_saat_ini = node_saat_ini.next
            i+=1

akademikQueue = QueueAkademik()
akademikQueue.Enqueue("J0403251110","Snickers")
akademikQueue.Enqueue("J0403251111","Lmao")
akademikQueue.tampilkan()
A = Node("J0403251110","Snickers")
B = Node("J0403251110","Snickers")
        
#Program Utama

def main():
    #Instansiasi Queue
    q = QueueAkademik()

    while True:
        print("======== Sistem Antrian Akademik ========")
        print("[1] Tambah Mahasiswa")
        print("[2] Layani Mahasiswa")
        print("[3] Lihat Antrian")
        print("[4] Keluar")

        pilihan = input("Pilih Menu (1-4) : ").strip()

        if pilihan == "1":
            nim = input("Masukkan NIM : ").strip()
            nama = input("Masukkan Nama : ").strip()

            q.Enqueue(nim,nama)
            print("Mahasiswa Berhasil Ditambahkan")

        elif pilihan == "2":
            mhsw_dilayani = q.dequeue()
            print(f"Mahasiswa Dilayani : {mhsw_dilayani.nim} = {mhsw_dilayani.nama}")

        elif pilihan == '3':
            q.tampilkan()
            
        elif pilihan == "4":
            print("Program Selesai. Terimakasih")
            break
        else:
            print("Pilihan tidak valid. Silahkan coba lagi [1-4]")

if __name__ == "__main__":
    main()