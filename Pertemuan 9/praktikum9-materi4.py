#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
# Traversal In-Order
#=============================================

class Node:
    def __init__(self,data):
        self.data = data # Menyimpan data pada node
        self.left = None # Menyimpan child kiri dari node
        self.right = None # Menyimpan child kanan dari node

# Membuat fungsi in order : left -> root -> right
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

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
inorder(root)

#Pembahasan : 
# di materi ke empat, kita mempelajari bagaimana traversal in order bekerja 
# dan mengimplementasikan nya
# traversal inorder menelusuri node dari : 
# left -> root -> right
# pengimplementasian mirip seperti preorder hanya berbeda urutan saja
# struktur ini akan menghasilkan : 
# D B E A F C
# dimana elemen yang dicetak mulai dari child left dengan level terbawah
# diikuti oleh root nya yang kemudian mencetak child right dari root tersebut, dan seterusnya