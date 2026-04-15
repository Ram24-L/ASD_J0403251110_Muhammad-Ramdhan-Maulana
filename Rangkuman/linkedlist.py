class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    #Saat baru diinisialisasi, head = none
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        if not self.head:
            print("Empty Linkedlist")
            return
        
        temp = self.head
        while temp.next:
            print(f"{temp.data}",end="->")
            temp = temp.next
        print(f"{temp.data}",end="->")

ll = linkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)

ll.display()