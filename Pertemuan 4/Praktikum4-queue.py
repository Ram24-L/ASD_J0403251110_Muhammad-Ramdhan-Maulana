#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=================================================
# Implementasi Dasar : Queue berbasis linked list
#=================================================

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
#Queue dengan 2 pointer : front and rear
class QueueLL:
    def __init__(self):
        self.front = None
        self.rear = None
    #buat fungsi entry queue (enqueue)
    def is_empty(self):
        if self.front == None and self.rear == None:
            return True
        else:
            return False
    def enqueue(self,data):
        #Menamnbah data di belakang (rear)
        new_node = Node(data)
        
        #Jika queue kosong, front dan rear menunjuk ke node yang sama
        if (self.is_empty()):
            self.front = new_node
            self.rear = new_node
            return
        #Menambah node baru di belakang
        self.rear.next = new_node
        self.rear = new_node


    def dequeue(self):
        #Menghapus data dari 
        # 1) lihat data yang paling depan
        data_terhapus = self.front.data

        # 2) geser front ke node berikutnya
        self.front = self.front.next
        
        # 3) jika queue kosong
        if (self.front is None):
            #maka rear juga None
            self.rear = None
        
        return data_terhapus


    def tampilkan(self):
        current = self.front
        print("Front -> ", end="")
        while current is not None:
            print(current.data,end=" -> ")
            current = current.next
        print("None - Rear di node")

#instantiasi
qll = QueueLL()

qll.enqueue(1)
qll.enqueue(2)
qll.enqueue(3)
qll.dequeue()
qll.tampilkan()