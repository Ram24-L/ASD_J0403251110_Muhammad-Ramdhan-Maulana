#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
# Traversal Pre-Order
#=============================================


#Membuat  node yang akan menjadi dasar dari tree
class Node:
    def __init__(self,data):
        self.data = data # Menyimpan data pada node
        self.left = None # Menyimpan child kiri dari node
        self.right = None # Menyimpan child kanan dari node

# Membuat fungsi pre-order : Root -> left -> right
def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

#Membuat tree
#Membuat root awal
root = Node("A")

#Membuat child level 1
root.left = Node("B")
root.right = Node("C")

#Membuat child level 2
root.left.left = Node("D")
root.left.right = Node ("E")
root.right.left = Node("F")

print("Hasil cetak traversal pre order : ")
preorder(root)

#Pembahasan : 
# di materi 3, setelah cara membuat struktur tree dipelajari,
# pembahasan masuk ke metode-metode pengaksesan dari struktur tree (dalam kasus ini print)
# Terdapat 3 metode traversal :
# 1. Pre-order
# 2. In-Order
# 3. Post-Order
# di materi 3, pre order dipelajari terlebih dahulu
# traversal preorder merupakan traversal yang dimulai dari:
# root -> left -> right
# traversal2 ini dibuat dengan memanfaatkan fungsi rekursif
# yang nanti pada hasil akhirnya, struktur tree ini akan menghasilkan : 
# A B D E C F
# yang mana child dari B tercetak semua terlebih dahulu, 
# baru menelusuri ke node c dan child nya