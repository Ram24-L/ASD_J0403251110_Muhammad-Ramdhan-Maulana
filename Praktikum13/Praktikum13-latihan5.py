#===========================================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#============================================================

# ==========================================================
# Latihan 5 : Studi kasus : Jaringan Jalan Antar Kota
# ==========================================================

# 1. Representasi weighted graph (Jarak antar kota)
# Format: (bobot/jarak, kota1, kota2)
edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

# 2. Implementasi Kruskal
# Mengurutkan semua edge berdasarkan jarak terpendek
edges.sort()

mst = []
total_bobot = 0
connected_cities = set()

# Iterasi untuk membangun Minimum Spanning Tree
for weight, u, v in edges:
    # Memilih edge yang tidak membentuk cycle sederhana
    # (Logika set sederhana sesuai materi Sekolah Vokasi IPB)
    if u not in connected_cities or v not in connected_cities:
        mst.append((u, v, weight))
        total_bobot += weight
        
        # Tambahkan kota ke set yang sudah terhubung
        connected_cities.add(u)
        connected_cities.add(v)

# 3. Output MST
print("Minimum Spanning Tree (Jaringan Jalan Efisien):")
for u, v, weight in mst:
    print(f"{u} - {v} dengan bobot: {weight}")

# 4. Output total bobot minimum
print(f"\nTotal bobot MST (Total Jarak) = {total_bobot}")

# 5. Jawaban Analisis:
# # 1. Kasus apa yang dipilih?
# #    Jawab: Kasus 1 (Jaringan Jalan Antar Kota).
# # 2. Algoritma apa yang digunakan?
# #    Jawab: Algoritma Kruskal.
# # 3. Edge mana saja yang dipilih dalam MST?
# #    Jawab: 
# #    - Bogor - Depok (2)
# #    - Depok - Jakarta (3)
# #    - Depok - Bandung (4)
# # 4. Berapa total bobot MST?
# #    Jawab: 9.
# # 5. Mengapa edge tertentu tidak dipilih?
# #    Jawab: Edge seperti Bogor-Jakarta (5) dan Jakarta-Bandung (6) tidak dipilih 
# #    karena kota-kota tersebut sudah terhubung melalui jalur lain yang lebih efisien. 
# #    Jika ditambahkan, edge tersebut hanya akan membentuk siklus (cycle) dan menambah total bobot.