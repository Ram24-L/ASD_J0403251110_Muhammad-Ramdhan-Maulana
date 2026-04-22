#==========================================
#Latihan 3 Pertemuan 3
#Penggabungan linked list
#==========================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        if not self.head:
            print("kosong")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")


def merge(list1, list2):
    merged = LinkedList()

    temp = list1.head
    while temp:
        merged.insert_at_end(temp.data)
        temp = temp.next

    temp = list2.head
    while temp:
        merged.insert_at_end(temp.data)
        temp = temp.next

    return merged


# ===== helper input =====

def input_list(prompt):
    ll = LinkedList()
    x = input(prompt).strip()

    if x == "":
        return ll

    nums = [int(n.strip()) for n in x.split(",")]
    for n in nums:
        ll.insert_at_end(n)

    return ll


# ===== program utama =====

list1 = input_list("Masukkan elemen untuk Linked List 1: ")
list2 = input_list("Masukkan elemen untuk Linked List 2: ")

print("Linked List 1:", end=" ")
list1.display()

print("Linked List 2:", end=" ")
list2.display()

merged = merge(list1, list2)

print("Linked List setelah digabungkan:", end=" ")
merged.display()
