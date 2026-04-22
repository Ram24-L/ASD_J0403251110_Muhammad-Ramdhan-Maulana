#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#============================================
#Implementasi Dasar : Node Pada Linked List
#============================================

#Membuat class node, yang merupakann calon anggota dari linked list
class Node:
    def __init__(self,data): #Membuat constructor pada linked list
        self.data = data # Menyimpan data ke dalam node
        self.next = None # Membuat Pointer 
        

#1) Membuat node satu per satu
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2) Menghubungkan Node
# Menghubungkan Node A -> B -> C
nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = None

#3) Menentukan Node Pertama
head = nodeA

#4) Traversal : Menyelusuri data pada linked list dari awal hingga akhir
current = head #Mulai dari head
while current is not None: #Selama masih ada node yang dapat diakses
    print(current.data) #cetak data saat ini
    current = current.next #beralih ke data selanjutna

#========================================================
#   Implementasi Dasar : Linked List + Insert awal
#========================================================

class LinkedList:
    def __init__(self):
        self.head = None #Awalnya Kosong

    def insert_awal(self,data): #Konsep Push pada stack
        #Daftarkan data baru sebagai node
        nodebaru = Node(data)
        #Buat node baru menunjuk ke head data yang ada
        nodebaru.next = self.head
        #Ganti head dengan data yang baru saja disambungkan ke head lama
        self.head = nodebaru

    def hapus_awal(self): #Pop dalam stack
        data_terhapus = self.head.data #Peek dalam stack
        #Menggeser head ke node selanjutnya
        self.head = self.head.next
        print("Node yang telah terhapus : ", data_terhapus)
        
    def tampilkan(self): #Implementasi traversal
        current = self.head
        while(current is not None):
            print(current.data)
            current = current.next

ll = LinkedList()
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan()