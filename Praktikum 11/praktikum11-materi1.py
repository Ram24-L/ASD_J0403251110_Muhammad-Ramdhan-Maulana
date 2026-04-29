#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#====================================
# Implementasi dasar Graph
#====================================

# Graph dibuat dengan struktur Dictionary
# dengan keys sebagai node, dan value sebagai neighbour
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D',],
    'C': ['A', 'D'],
    'D': ['B', 'C'],
}

# cetak graph
for node in graph:
    print(node, "->", graph[node])