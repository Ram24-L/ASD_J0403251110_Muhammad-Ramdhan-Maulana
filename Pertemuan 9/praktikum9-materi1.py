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
#Mendaftarkan node B menjadi left child dari A
root.left = node("B")
#Mendaftarkan node C menjadi right child dari A
root.right = node("C")
print("Data dari root: ",root.data)
print("Left child root : ",root.left.data)
print("Right child root : ",root.right.data)
#Mendaftarkan node D menjadi left child dari node B yang merupakan child left dari A
root.left.left= node("D")
#Mendaftarkan node E menjadi right child dari node B
root.left.right = node("E")

#Mendaftarkan Node F Menjadi left child dari node C yang merupakan right child dari C
root.right.left = node("F")