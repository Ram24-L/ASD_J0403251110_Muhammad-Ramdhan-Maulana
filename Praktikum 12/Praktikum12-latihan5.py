#===========================================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=========================================================

# ==========================================================
# Latihan 5: Studi Kasus Jalur Terpendek (Shortest Path)
# Kasus: Rute antar kota menggunakan algoritma Dijkstra
# ==========================================================
import heapq

# 1. Representasi graph berbobot menggunakan dictionary
# Key adalah kota asal, value adalah dictionary dari kota tujuan dan bobot (jarak/waktu).
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {} # Bandung tidak memiliki rute keluar dalam kasus ini
}

# 2. Fungsi Dijkstra
def dijkstra(graph, start):
    """
    Menghitung jarak terpendek dari node awal (start) ke seluruh node dalam graph.
    """
    # Inisialisasi jarak awal ke semua node sebagai tak terhingga (infinity)
    distances = {node: float('inf') for node in graph}
    # Jarak dari node awal ke dirinya sendiri selalu 0
    distances[start] = 0
    
    # Priority queue untuk menyimpan node yang akan dieksplorasi (jarak, node)
    priority_queue = [(0, start)]
    
    # Looping selama masih ada node yang perlu dievaluasi
    while priority_queue:
        # Ambil node dengan jarak terpendek saat ini dari antrean
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Jika jarak yang sedang diproses lebih besar dari yang tercatat, lewati (optimalisasi)
        if current_distance > distances[current_node]:
            continue
            
        # Periksa semua kota tetangga yang terhubung langsung
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight # Total jarak dari node awal
            
            # Jika rute baru yang dihitung lebih pendek, lakukan pembaruan
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Masukkan tetangga dengan jarak terbarunya ke antrean
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

# 3. Penentuan node awal
node_awal = 'Bogor'

# Menjalankan algoritma
hasil = dijkstra(graph, node_awal)

# 4. Output jarak terpendek dari node awal ke semua node sesuai format yang diharapkan
print(f"Jarak terpendek dari {node_awal}:")
for kota, jarak in hasil.items():
    print(f"{node_awal} -> {kota} = {jarak}")


# ==========================================================
# Jawaban Analisis:
# ==========================================================
# 1. Node awal yang digunakan apa?
#    Jawaban: Node awal yang digunakan adalah 'Bogor'.
#
# 2. Node mana yang memiliki jarak paling kecil dari node awal?
#    Jawaban: 'Depok' (dengan jarak 2), jika tidak menghitung node Bogor itu 
#    sendiri (yang jaraknya 0).
#
# 3. Node mana yang memiliki jarak paling besar dari node awal?
#    Jawaban: 'Bandung' (dengan jarak 8).
#
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat:
#    Jawaban: 
#    - Algoritma dimulai di 'Bogor' (jarak 0). Bogor mengevaluasi tetangganya:
#      'Depok' (jarak 0+2=2) dan 'Jakarta' (jarak 0+5=5).
#    - Karena jarak ke 'Depok' (2) lebih kecil dari 'Jakarta' (5), algoritma 
#      memilih untuk mengeksplorasi 'Depok' terlebih dahulu.
#    - Dari 'Depok', ia mengevaluasi tetangganya:
#      a. Ke 'Jakarta': total jarak menjadi 2 + 2 = 4. Jarak ini (4) lebih 
#         kecil daripada jarak awal langsung Bogor->Jakarta (5). Maka jarak 
#         menuju 'Jakarta' diperbarui/direlaksasi menjadi 4.
#      b. Ke 'Bandung': total jarak menjadi 2 + 6 = 8.
#    - Selanjutnya, algoritma mengeksplorasi 'Jakarta' (dengan jarak saat ini 4). 
#      Dari Jakarta ke Bandung jaraknya 7, sehingga total rute Bogor -> Depok -> 
#      Jakarta -> Bandung adalah 4 + 7 = 11. Karena 11 > 8, jarak ke Bandung 
#      tidak diperbarui dan tetap 8.
#    - Karena tidak ada lagi rute baru yang lebih singkat, proses selesai dengan
#      hasil akhir Bogor=0, Depok=2, Jakarta=4, dan Bandung=8.
# ==========================================================