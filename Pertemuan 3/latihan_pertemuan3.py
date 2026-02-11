#===================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#===================================

##===================================
# Single Linked List + Delete Node
#===================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # tambah di akhir
    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # tampilkan isi list
    def display(self):
        if not self.head:
            print("kosong")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    # delete berdasarkan nilai
    def delete_node(self, key):
        temp = self.head

        # jika head yang dihapus
        if temp and temp.data == key:
            self.head = temp.next
            return True

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if not temp:
            return False

        prev.next = temp.next
        return True


#========================
# INPUT LINKED LIST
#========================

ll = SinglyLinkedList()

while True:
    try:
        x = input("Masukkan elemen linked list (pisah koma): ").strip()
        if x == "":
            break

        nums = [int(n.strip()) for n in x.split(",")]
        for n in nums:
            ll.insert_at_end(n)
        break

    except ValueError:
        print("Format salah. Contoh: 3,5,7,9")


#========================
# TAMPIL SEBELUM HAPUS
#========================

print("\nLinked List sebelum hapus:")
ll.display()


#========================
# INPUT HAPUS
#========================

while True:
    try:
        key = int(input("\nMasukkan nilai yang ingin dihapus: "))
        break
    except ValueError:
        print("Masukkan satu angka saja")


#========================
# PROSES HAPUS
#========================

result = ll.delete_node(key)

#========================
# TAMPIL SESUDAH HAPUS
#========================

print("\nLinked List sesudah hapus:")
ll.display()

if result:
    print("Node berhasil dihapus")
else:
    print("Node tidak ditemukan")
