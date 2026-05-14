#===========================================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#============================================================

# ==========================================================
# Latihan 1 : Memahami Konsep Spanning Tree
# ==========================================================

# Contoh Struktur Program

# Daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# Jawaban Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
#    Jawab: Graph awal berisi seluruh jalur (edges) yang mungkin menghubungkan semua node, 
#    termasuk jalur yang membentuk siklus. Sedangkan spanning tree adalah sub-graph yang 
#    menghubungkan semua node dalam graph tersebut tanpa adanya siklus (cycle).

# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    Jawab: Secara definisi, 'tree' (pohon) adalah struktur data yang tidak memiliki siklus. 
#    Jika terdapat cycle, maka struktur tersebut bukan lagi sebuah pohon melainkan graph biasa. 
#    Tujuan spanning tree adalah mencari efisiensi koneksi minimum untuk menghubungkan semua node.

# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    Jawab: Karena spanning tree hanya menggunakan jumlah jalur minimum untuk menghubungkan 
#    n buah node. Secara matematis, jika sebuah graph memiliki n node, maka spanning tree-nya 
#    akan selalu memiliki tepat n-1 edge. Segala tambahan edge di luar itu pasti akan membentuk cycle.