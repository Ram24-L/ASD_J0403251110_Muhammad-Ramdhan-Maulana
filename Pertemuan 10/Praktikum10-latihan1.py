#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
# Latihan : Binary Search Tree
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

#Mengisi data BST
root = None
data_list = [50,30,70,20,40,50,80]

for data in data_list:
    root = insert(root,data)


#=======================================
# Latihan 2: Traversal InOrder
# ======================================

# Membuat traversal in order untuk menampilkan setiap node dalam tree
def inorder(root):
    # Fungsi inorder menelusuri node paling kiri terlebih dahulu
    # Left -> parent -> Right
    # Berulang ulang menggunakan rekursif hingga seluruh tree terselusuri
    if root is not None:
        inorder(root.left) 
        print(root.data,end=" ") 
        inorder(root.right)

#Cetak hasil inorder
print("Hasil Inorder : ")
inorder(root)

#=======================================
#Latihan 3 :  Search di BST
#=======================================

#Membuat fungsi search di BST
def search(root,key):
    #Handling jika root kosong, langsung return False
    if root is None:
        return False

    #Jika data dari root sama dengan key yang dicari
    if root.data == key:
        #maka, return True (elemen ditemukan)
        return True
    #Jika data yang dicari lebih kecil dari parent nya
    elif key < root.data:
        #maka, telusuri child kiri dari parent tsb
        return search(root.left,key)
    #Jika data yang dicari lebih besar dari parent nya
    elif key > root.data:
        #maka, telusuri child kanan dari parent tsb
        return search(root.right,key)

#Mencoba fungsi search pada tree yang sudah ada
key = 40
if search(root,key):
    print("Data ditemukan")
else:
    print("Data tidak ditemukan")
# Hasil : Data Ditemukan karena key (40) berada dalam tree