#============================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 1A : Membaca seluruh isi file
#============================================

#membuka file dengan "read"
#Fungsi Baca File
path = "data.txt"

#!!Ini Inisiatif saat itu!!
#Fungsi Read file
def read_file(data):
    #Error Handling
    try:
        #Membuka File dalam kesatuan String
        with open(data,"r",encoding="utf-8") as file:
            return file.read()
    except(FileNotFoundError):
        print("File Tidak Ada")

#!!Ini Inisiatif saat itu!!
#Fungsi Save File
def save_file(data,saved_data):
    #Error Handling
    try:
        with open(data,"w") as file:
            file.write(saved_data)
            print('Data Tersimpan')
    except(FileNotFoundError):
        print("File Tidak ada")


data_mahasiswa = read_file(path)
print("======= Hasil Read ========")
print("Tipe Data : ",type(data_mahasiswa))
print("Jumlah Karakter : ",len(data_mahasiswa))
print("Jumlah Baris", data_mahasiswa.count("\n")+1)

#============================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 2A : Membaca file bper baris
#============================================
print("Membaca File Per Baris")
jumlah_baris = 0
with open("data.txt","r",encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris+1
        baris = baris.strip("\n")
        print("Baris ke-",jumlah_baris)
        print("Isinya : ",baris )
        
with open("data.txt","r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim,nama,nilai = baris.split(",") #Parsing data berdasarkan Koma jika 
        print(f"NIM : {nim} | Nama : {nama} | Nilai : {nilai}")

#============================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 3A : Menyimpan data ke dalam list
#============================================

data_list = [] #List untuk menampung data mahasiswa

with open("data.txt","r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        baris = baris.split(",")
        baris[2] = int(baris[2])
        #simpan Data Mahasiswa sebagai list
        data_list.append(baris)

#Data Mahasiswa dalam list
print("======= Data Mahasiswa =======")
print(data_mahasiswa)
#Jumlah Mahasiswa Dalam List
print("======= Jumlah Mahasiswsa =======")
print(len(data_mahasiswa))
#Menampilkan Data Record Tertentu
print("======== Mahasiswa Pertama ======= " )
print(data_list[0])

#============================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 4A : Menyimpan data ke dalam list
#============================================

data_dict = {}
with open("data.txt","r",encoding="utf-8") as file :
    for baris in file : 
        baris = baris.strip()

        nim,nama,nilai = baris.split(",")
        data_dict[nim] = {
            "Nama" : nama,
            "Nilai": int(nilai)
        }