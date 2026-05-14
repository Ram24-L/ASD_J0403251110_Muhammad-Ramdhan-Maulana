#===========================================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#============================================================

# ==========================================================
# Latihan 4 : Studi kasus : Jaringan Kabel Antar Gedung
# ==========================================================

# 1. Representasi Weighted Graph (Daftar hubungan gedung dan biayanya)
# Format: (biaya, gedung1, gedung2)
connections = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]

# 2. Implementasi Kruskal
# Mengurutkan koneksi berdasarkan biaya terendah
connections.sort()

mst_edges = []
total_min_cost = 0
connected_buildings = set()

# Iterasi melalui setiap koneksi yang sudah diurutkan
for cost, u, v in connections:
    # Cek apakah koneksi membentuk cycle sederhana
    # (Menggunakan logika set sederhana sesuai modul Sekolah Vokasi)
    if u not in connected_buildings or v not in connected_buildings:
        mst_edges.append((u, v, cost))
        total_min_cost += cost
        
        # Tambahkan gedung ke set yang sudah terhubung
        connected_buildings.add(u)
        connected_buildings.add(v)

# 3. Output Edge yang dipilih
print("Jaringan Kabel yang Dipilih (MST):")
for u, v, cost in mst_edges:
    print(f"{u} - {v} dengan biaya: {cost}")

# 4. Output Total Biaya Minimum
print(f"\nTotal Biaya Minimum: {total_min_cost}")

# Jawaban Analisis:
# 1. Algoritma apa yang digunakan?
#    Jawab: Algoritma Kruskal (karena efisien untuk mengolah daftar edge/kabel secara langsung).

# 2. Edge mana saja yang dipilih?
#    Jawab: 
#    - GedungC - GedungD (Biaya: 1)
#    - GedungA - GedungC (Biaya: 2)
#    - GedungB - GedungD (Biaya: 3)

# 3. Berapa total biaya minimum?
#    Jawab: 1 + 2 + 3 = 6.

# 4. Mengapa MST cocok digunakan pada kasus ini?
#    Jawab: Karena tujuan utama kasus ini adalah menghubungkan seluruh gedung agar 
#    saling terintegrasi dalam satu jaringan dengan total biaya pemasangan yang 
#    paling rendah (minimum), tanpa perlu adanya jalur ganda atau siklus.