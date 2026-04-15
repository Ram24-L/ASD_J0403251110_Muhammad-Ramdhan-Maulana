#Double Linked List

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Double_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self,data):
        #Mengubah format data yang diinsert menjadi node
        new_node = Node(data)
        #mengecek apakah linked list sudah ber kepala
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        #Sambungkan node terakhir dengan node baru
        #pointer dari akhir linked list ke node baru
        self.tail.next = new_node
        #pointer dari node baru ke akhir list sebelumnya
        new_node.prev = self.tail

        #update tail menjadi paling akhir
        self.tail = new_node

    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def display_backward(self):
        temp = self.tail
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev
        print("null")


# ==== contoh pakai ====
dll = Double_Linked_List()
dll.insert_at_end(3)
dll.insert_at_end(5)
dll.insert_at_end(9)

dll.display_forward()
dll.display_backward()