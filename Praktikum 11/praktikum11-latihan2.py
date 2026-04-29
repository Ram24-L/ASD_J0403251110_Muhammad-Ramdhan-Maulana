#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
# Latihan : Studi Kasus DFS
#=============================================

from collections import deque

# Implementasi DFS
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
#menggunakan dfs sebagai studi kasus
def dfs(graph, node, visited):
    #Fungsi untuk melakukan penelusuran graph menggunakan DFS
    #graph : dictionary yang menyimpan graph
    #node : menyimpan node yang sedang dikunjungi
    #visited : menyimpan node yang sudah dikunjungi

    #tandai node saat ini sebagai node yang sudah dikunjungi
    visited.add(node)

    #tampilkan node yang sedang dikunjungi
    print(node, end=" ")

    #periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:
        # jika tetangga belum pernah dikunjungi
        if neighbor not in visited:
            #Lakukan dfs secara rekursif ke tetangga tersebut
            dfs(graph,neighbor,visited)


visited = set()

#menjalankan dfs dari A
dfs(graph,"A",visited)

'''
Pertanyaan Analisis
1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
2. Apa yang terjadi jika urutan neighbor diubah?
3. Bandingkan hasil DFS dengan BFS pada graph yang sama.
'''

# Jawaban
# 1. Karena DFS menggunakan pendekatan rekursif atau yang selalu 
#  melanjutkan ke node berikutnya sebelum kembali (backtracking)
#  selama masih ada neighbour, maka penelusuran akan terus ke level yang terdalam
# 2. tentu urutan traversal DFS akan beubah juga, contoh jika 'A':["C","B"] (dibalik),
#  maka DFS akan mengunjungi C dulu baru baru B, jika tidak dibalik akan sebaliknya
# 3. DFS (Depth first search)
#    A → B → D → E → C → F
#    BFS (Breadth First Search)
#    A → B → C → D → E → F