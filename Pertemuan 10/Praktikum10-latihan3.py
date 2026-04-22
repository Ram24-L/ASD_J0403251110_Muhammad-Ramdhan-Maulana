#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
# Latihan : Rotasi Kiri pada BST tidak Seimbang
#=============================================

#Membuat node dasar untuk tree
class Node:
    def __init__(self,data):
        self.data = data # Menyimpan nilai ke dalam node
        self.left = None # Pointer ke child kiri
        self.right = None # Pointer ke child kanan


#Fungsi preorder untuk melihat bentuk tree
def preorder(root):
    #Preorder adalah metode traversal tree yang berasal dari root
    # root -> left -> right
    if root is not None:
        print(root.data,end = " ")
        preorder(root.left)
        preorder(root.right)

#Fungsi sederhana untuk menampilkan struktur Tree
def tampil_struktur(root,level = 0, posisi = "Root"):
    if root is not None:
        print("    " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

# Fungsi Rotate Left
def rotate_left(x):
    #x adalah root lama
    y = x.right # y adalah child kanan x
    T2 = y.left # subtree kiri milik y disimpan sementara

    # Proses rotasi
    y.left = x  # x menjadi child kiri dari y
    x.right = T2 # child kanan x diganti dengan T2

    # y menjadi root baru 
    return y


# -----------------------------
# Program utama
# -----------------------------
# Membuat tree yang tidak seimbang:
# 10 -> 20 -> 30
root = Node(10)
root.right = Node(20)
root.right.right = Node(30)

#Mengecek tree sebelum melakukan rotasi
print("Preorder sebelum rotasi kiri:")
preorder(root)
print("\n\nStruktur sebelum rotasi kiri:")
tampil_struktur(root)

# Melakukan rotasi kiri pada root
root = rotate_left(root)

#Mengecek hasil sesudah rotasi kiri dilakukan
print("\nPreorder sesudah rotasi kiri:")
preorder(root)
print("\n\nStruktur sesudah rotasi kiri:")
tampil_struktur(root)