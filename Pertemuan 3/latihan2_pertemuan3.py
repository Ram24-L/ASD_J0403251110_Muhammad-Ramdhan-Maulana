#==============================================
#Latihan No 2
# Buat Kode implementasikan pencarian pada node tertentu
# pada single circular linked list
#==============================================
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList : 
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        
        #cari node terakhir
        temp = self.head
        while(temp.next != self.head):
            temp = temp.next
        
        temp.next = new_node
        new_node.next = self.head

    def display(self):
        if not self.head:
            print("List is empty")
            return
        
        print("Circular Linked List Traversal: ")
        temp = self.head
        print(temp.data, end=" -> ")
        temp = temp.next

        while temp != self.head:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("(kembali ke head)")

    def search(self,key):
        if not self.head:
            return False
        
        temp = self.head
        while True:
            if temp.data == key:
                return True

            temp = temp.next

            if temp == self.head:
                break
        return False


circlinkedlist = CircularSinglyLinkedList()
while True:
    try:
        x = input("Masukkan elemen ke dalam circular linked list: ").strip()
        if x == '':
            x = []
        else:
            x = [int(num.strip()) for num in x.split(",")]
        for i in x:
            circlinkedlist.insert_at_end(i)
        break
    except ValueError:
        print("Masukkan dengan format yang sesuai")
while True:
    try:
        search_key = input("Masukkan elemen yang ingin dicari : ").strip()
        search_key = int(search_key)
        break
    except ValueError:
        print("Masukkan satu angka saja")

result = circlinkedlist.search(search_key)
if(circlinkedlist.head == None):
    print("Circular Linked List Kosong. Tidak ada elemen yang bisa dicari")
elif result:
    print(f"Elemen {search_key} ditemukan dalam circular linked list")
else:
    print(f"Elemen {search_key} tidak ditemukan dalam circular linked list")



