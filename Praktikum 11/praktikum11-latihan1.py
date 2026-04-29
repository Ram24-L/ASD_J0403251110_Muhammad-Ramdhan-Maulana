#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
# Latihan : Studi Kasus BFS
#=============================================

# Inisialisasi graph
graph = {
 'Rumah': ['Sekolah', 'Toko'],
 'Sekolah': ['Perpustakaan'],
 'Toko': ['Pasar'],
 'Perpustakaan': [],
 'Pasar': []
}

#Mengimport fungsi deque dari collections
from collections import deque

# Membuat fungsi penelusuran BFS
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

#Mencetak hasil BFS
print("BFS dari Rumah : ")
bfs(graph,"Rumah")

'''
Pertanyaan Analisis
1. Node mana yang dikunjungi pertama?
2. Mengapa BFS cocok untuk mencari jalur terdekat?
3. Apa perbedaan urutan BFS jika struktur graph diubah?
'''

# Jawaban Pertanyaan Analisis
# 1. Jika graph tersebut menggambarkan jalur dari rumah ke lokasi lain, tempat / node yang pertama kali dikunjungi 
#    adalah Rumah itu sendiri, setelah itu sekolah lalu ke toko
# 2. BFS menggunakan konsep level per level (melebar)
#    dengan kata lain BFS menelusuri node yang paling dekat terlebih dahulu
# 3. Perbedaan urutan BFS akan berubah jika struktur graph diubah, jika terdapat perbedaan 
#    baik dalam hal urutan, atau bahkan jumlah neighbor, maka struktur graph akan berubah
#    namun prinsip BFS tetap sama