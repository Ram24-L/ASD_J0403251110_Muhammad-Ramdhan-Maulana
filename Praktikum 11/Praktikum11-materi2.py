#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
# Materi : Penelusuran Graph dengan BFS
#=============================================

from collections import deque

#Representasi Graph
graph = {
    "A":["B","C"],
    "B":["D","E"],
    "C":["F","G"],
    "D":[],
    "E":[],
    "F":[],
    "G":[]
}

def bfs(graph,start):
    # Fungsi untuk melakukan penelusuran graph dengan BFS
    # Queue digunakan untuk menyimpan node yang akan diproses / dibaca
    queue = deque()
    
    # Variabel yang digunakan untuk menyimpan node yang sudah dikunjungi
    visited = set()

    # Masukkan node awal ke queue
    queue.append(start)

    # Tandai node awal sebagai node yang sudah dikunjungi
    visited.add(start)

    while queue:
        # Mengambil node paling depan dari queue
        node = queue.popleft()

        #Tampilkan node yang sedang dikunjungi
        print(node,end=" ")

        # periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]:
            #Jika tetangga belum dikunjungi
            if neighbor not in visited:
                #tandai sebagai sudah dikunjungi
                visited.add(neighbor)
                #Masukkan tetangga ke queue untuk diproses nanti
                queue.append(neighbor)

#Menjalankan BFS dari node A
bfs(graph,"A")
