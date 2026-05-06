#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
# Materi : Algoritma djikstra pada weighted graph
#=============================================



import heapq

# Representasi graf menggunakan dictionary bersarang.
# Key utama adalah node asal, valuenya adalah dictionary berisi node tetangga beserta bobot jaraknya.
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {} # D tidak memiliki tetangga tujuan
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari rute atau jarak terpendek dari node awal (start) 
    ke semua node lain di dalam graf.
    """
    # 1. INISIALISASI
    # Atur jarak awal ke semua node menjadi tak terhingga (infinity).
    # Ini karena kita belum mengetahui jarak pastinya.
    distances = {node: float('inf') for node in graph}
    
    # Jarak dari node awal ke dirinya sendiri tentu saja 0.
    distances[start] = 0
    
    # 2. SETUP PRIORITY QUEUE (Antrean Prioritas)
    # Menyimpan antrean node yang akan diproses dalam format: (jarak_akumulasi, nama_node).
    # Kita mulai dengan memasukkan node awal.
    pq = [(0, start)]
    
    # 3. PROSES UTAMA (Looping selama antrean tidak kosong)
    while pq:
        # Ambil node dengan jarak paling kecil (prioritas tertinggi) dari antrean
        current_distance, current_node = heapq.heappop(pq)
        
        # Optimalisasi keamanan: Jika jarak yang sedang diproses ternyata lebih besar
        # dari jarak minimum yang sudah tersimpan, lewati saja (mencegah komputasi berulang).
        if current_distance > distances[current_node]:
            continue
            
        # 4. PERIKSA SEMUA TETANGGA
        # Looping untuk melihat setiap tetangga dari node yang sedang kita pijak saat ini
        for neighbor, weight in graph[current_node].items():
            
            # Hitung total jarak tempuh dari titik awal (start) hingga ke tetangga ini
            distance = current_distance + weight
            
            # 5. UPDATE JARAK (Relaksasi)
            # Jika rute baru yang ditemukan jaraknya LEBIH KECIL (lebih cepat) 
            # daripada jalur yang pernah dicatat sebelumnya...
            if distance < distances[neighbor]:
                distances[neighbor] = distance             # Perbarui catatan jarak minimum
                heapq.heappush(pq, (distance, neighbor))   # Masukkan tetangga ke antrean untuk diproses nanti

    return distances

# --- EKSEKUSI PROGRAM ---
# Mencari jarak terpendek dari titik 'A'
hasil = dijkstra(graph, 'A')

# Menampilkan hasil dengan format yang lebih rapi
print("Jarak minimum dari Node 'A':")
for node, jarak in hasil.items():
    print(f"Ke Node {node} : {jarak}")