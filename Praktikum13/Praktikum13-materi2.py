#===========================================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#============================================================

# ==========================================================
# Materi 2 : Algoritma Prim
# ==========================================================

import heapq

# Definisi graf dalam bentuk adjacency list (dictionary)
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    # Set untuk melacak simpul yang sudah dikunjungi
    visited = set([start])
    
    # Priority queue untuk menyimpan edge (bobot, simpul_asal, simpul_tujuan)
    edges = []
    
    # Masukkan semua tetangga dari simpul awal ke dalam heap
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
        
    mst = []
    total_weight = 0
    
    while edges:
        # Ambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges)
        
        # Jika simpul tujuan belum dikunjungi, tambahkan ke MST
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            
            # Periksa tetangga dari simpul yang baru ditambahkan
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
                    
    return mst, total_weight

# Eksekusi fungsi
mst, total = prim(graph, 'A')

# Output hasil
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total)