#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
# Latihamn 6 : Struktur organisasi persuahaan
#=============================================

class Node:
    def __init__(self,data):
        self.data = data # Menyimpan data pada node
        self.left = None # Menyimpan child kiri dari node
        self.right = None # Menyimpan child kanan dari node

def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)


#Membuat tree struktur organisasi
root = Node("Direktur")

#Membuat child level 1
root.left = Node("Manager A")
root.right = Node("Manager B")

#Membuat child level 2
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")
root.right.left = Node("Staff 3")

preorder(root)

#Pembahasan : 
# di materi ke-6, kita melakukan latihan dengan pengimplementasian praktik tree
# dari real world problem, yaitu struktur organisasi dari perusahaan
# yang terdiri dari 2 level hierarki
# pengimplementasian tidak jauh berbeda dari abstrak tree yang berupa abjad
# hanya berbeda dari isi data setiap node-nya
# kemudian pencetakan dilakukan dengan memakai pre order traversal


