#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
# Traversal Post-Order
#=============================================

class Node:
    def __init__(self,data):
        self.data = data # Menyimpan data pada node
        self.left = None # Menyimpan child kiri dari node
        self.right = None # Menyimpan child kanan dari node

# Membuat fungsi Traversal Post-Order : left -> right -> root
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")

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
postorder(root)
