#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
# Materi : Penelusuran DFS pada Graph
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