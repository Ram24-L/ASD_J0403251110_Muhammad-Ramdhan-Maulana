#===========================================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#============================================================

# ==========================================================
# Latihan 3 : Implementasi Algoritma Prim
# ==========================================================

import heapq

# Definisi graph
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    visited = set([start])
    edges = []
    
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
        
    mst = []
    total_weight = 0
    
    while edges:
        weight, u, v = heapq.heappop(edges)
        
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
                    
    return mst, total_weight

# Menjalankan program mulai dari node 'A'
mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total)

# Jawaban Analisis:
# 1. Node awal apa yang digunakan?
#    Jawab: Node awal yang digunakan dalam pemanggilan fungsi adalah 'A'.

# 2. Edge mana yang dipilih pertama kali?
#    Jawab: Edge ('A', 'C') dengan bobot 2, karena merupakan tetangga dengan bobot terkecil dari node 'A'.

# 3. Bagaimana Prim menentukan edge berikutnya?
#    Jawab: Prim menggunakan priority queue (heapq) untuk selalu memilih edge dengan bobot 
#    terkecil yang menghubungkan node yang sudah dikunjungi dengan node yang belum dikunjungi.

# 4. Berapa total bobot MST yang dihasilkan?
#    Jawab: Total bobot MST adalah 6 (didapat dari edge A-C: 2, C-D: 1, dan D-B: 3).

# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#    Jawab: Prim membangun MST secara bertahap mulai dari satu node akar dan "tumbuh" ke luar 
#    dengan menambahkan node terdekat. Sedangkan Kruskal bekerja dengan mengurutkan 
#    seluruh sisi (edges) di graf dan menambahkannya satu per satu selama tidak membentuk cycle.