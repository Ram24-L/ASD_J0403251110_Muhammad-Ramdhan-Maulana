#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
# Latihan Membuat Node tree
#=============================================

#Membuat  node yang akan menjadi dasar dari tree
class Node:
    def __init__(self,data):
        self.data = data # Menyimpan data pada node
        self.left = None # Menyimpan child kiri dari node
        self.right = None # Menyimpan child kanan dari node

#Membuat root awal
root = Node("A")

#Membuat child level 1
root.left = Node("B")
root.right = Node("C")

#Membuat child level 2
root.left.left = Node("D")
root.left.right = Node ("E")
root.right.left = Node("F")

#Menampilkan isi node
print("Data pada root : ",root.data)
#Menampilkan child level 1
print("Child left root : ",root.left.data)
print("Child right root : ",root.right.data)
#Menampilkan child level 2
print("Child left dari B : ",root.left.left.data)
print("Child right dari B : ",root.left.right.data)
print("Child left dari C : ",root.right.left.data)