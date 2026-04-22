#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
# Latihan : Rotasi Kanan pada BST tidak Seimbang
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
def rotate_right(x):
    #x adalah root lama
    y = x.left # y adalah child kiri x
    T2 = y.right # subtree kanan milik y disimpan sementara

    # Proses rotasi
    y.right = x  # x menjadi child kanan dari y
    x.left = T2 # child kiri x diganti dengan T2

    # y menjadi root baru 
    return y


# -----------------------------
# Program utama
# -----------------------------
# Membuat tree yang tidak seimbang:
# 30 -> 20 -> 10
root = Node(30)
root.left = Node(20)
root.left.left = Node(10)

#Mengecek tree sebelum melakukan rotasi
print("Preorder sebelum rotasi kanan:")
preorder(root)
print("\n\nStruktur sebelum rotasi kanan:")
tampil_struktur(root)

# Melakukan rotasi kanan pada root
root = rotate_right(root)

#Mengecek hasil sesudah rotasi kanan dilakukan
print("\nPreorder sesudah rotasi kanan:")
preorder(root)
print("\n\nStruktur sesudah rotasi kanan:")
tampil_struktur(root)