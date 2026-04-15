#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
# Implementasi Node pada Tree
#=============================================

#Membuat  node yang akan menjadi dasar dari tree
class node:
    def __init__(self,data):
        self.data = data # Menyimpan data pada node
        self.left = None # Menyimpan child kiri dari node
        self.right = None # Menyimpan child kanan dari node

# Membuat Node Root
root = node("A")
print("Data dari root: ",root.data)
print("Left child root : ",root.left)
print("Right child root : ",root.right)

# Pembahasan : 
# Materi 1 mempelajari bagaimana kita dapat menginisialisasi node yang dapat diimplementasikan
# pada struktur data tree, dimana node memiliki 3 atribut, yang memiliki fungsi
# 1. data : tempat value disimpan
# 2. left : child sebelah kiri dari root
# 3. right : child sebelah kanan dari root
# setelah membuat class node yang berisi atribut tersebut
# Pembuatan tree dapat langsung dieksekusi dengan membuat root terlebih dahulu
# lalu mendaftarkan child dari root tsb
