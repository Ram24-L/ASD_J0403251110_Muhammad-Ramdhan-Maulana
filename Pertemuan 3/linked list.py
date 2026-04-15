class Node:
    def __init__(self,data):
        #initiallize node
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        new_node = Node(data)
        if not self in data:
            self.head = new_node
            return
        
        temp = self.head
        while(temp):
            temp = temp.next

    def display(self,data):
        if not self in data:
            print("Empty Linked List")
            return
        temp = self.head 
        while(temp):
            print(temp)
            temp = temp.next

while(True):
    var = input("Masukkan elemen linked list : ")


