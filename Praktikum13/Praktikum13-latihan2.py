#===========================================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#============================================================

# ==========================================================
# Latihan 2 : Implementasi Sederhana Algoritma Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0

connected = set()

for weight, u, v in edges:
    
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        
        mst.append((u, v, weight))
        total_weight += weight
        
        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total_weight)

# Jawaban Analisis:
# 1. Edge mana yang dipilih pertama kali?
#    Jawab: Edge ('C', 'D') dengan bobot 1.

# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#    Jawab: Karena prinsip utama algoritma Kruskal adalah algoritma "greedy" yang 
#    selalu mencoba mengambil jalur termurah (bobot terkecil) terlebih dahulu 
#    untuk meminimalkan total bobot keseluruhan pohon (MST).

# 3. Berapa total bobot MST yang dihasilkan?
#    Jawab: Total bobotnya adalah 6 (didapat dari edge 1 + 2 + 3).

# 4. Mengapa edge tertentu tidak dipilih?
#    Jawab: Karena penambahan edge tersebut akan membentuk "cycle" (siklus). 
#    Dalam MST, semua node harus terhubung tanpa ada jalur tertutup agar 
#    koneksi tetap efisien dan sesuai definisi pohon (tree).