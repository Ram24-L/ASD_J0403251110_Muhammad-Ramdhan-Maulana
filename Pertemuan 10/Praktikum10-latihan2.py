#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
# Latihan : Membuat BST yang tidak seimbang
#=============================================

#Membuat node dasar untuk tree
class Node:
    def __init__(self,data):
        self.data = data # Menyimpan nilai ke dalam node
        self.left = None # Pointer ke child kiri
        self.right = None # Pointer ke child kanan

#Membuat fungsi untuk membuat Binary Search Tree
def insert(root,data):
    # Handling jika root yang dijadikan parameter ternyata kosong
    if root is None: 
        return Node(data)

    # Jika data lebih kecil dari parent
    if data < root.data:
        #data akan menjadi child left dari parent tsb
        root.left = insert(root.left,data)
    #Jika data lebih besar dari parent
    elif data > root.data:
        #Maka data akan menjadi child right dari parent tsb
        root.right = insert(root.right,data)
    
    #Mengembalikan tree yang telah diisi 
    return root

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

# -----------------------------
# Program utama
# -----------------------------
#Menginisialisasikan tree kosong
root = None
# Data dimasukkan berurutan naik
# yang akan menyebabkan BST tidak seimbang
data_list = [10, 20, 30]
#memasukkan elemen data_list satu persatu ke dalam BST
for data in data_list:
    root = insert(root, data)

print("Preorder BST:")
preorder(root)
print("\n\nStruktur BST:")
tampil_struktur(root)
