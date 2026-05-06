#===========================================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=========================================================

# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0
    
    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):
        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():
                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    
    return distances

# Eksekusi fungsi
hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(f"{node} = {distance}")

# ==========================================================
# Jawaban Analisis:
# ==========================================================
# 1. Berapa bobot langsung dari A ke B?
#    Jawaban: 5.
#
# 2. Berapa total bobot jalur A -> C -> B?
#    Jawaban: 2. (Bobot A->C adalah 4, ditambah bobot C->B yaitu -2. 
#    Sehingga 4 + (-2) = 2).
#
# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
#    Jawaban: Jalur A -> C -> B (dengan total bobot 2) menghasilkan jarak 
#    yang lebih kecil dibandingkan jalur langsung A -> B (dengan bobot 5).
#
# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
#    Jawaban: Karena Bellman-Ford tidak berasumsi bahwa jarak yang ditemukan 
#    pertama kali adalah jarak final yang mutlak (berbeda dengan pendekatan 
#    Greedy pada Dijkstra). Algoritma ini memastikan evaluasi secara menyeluruh 
#    dengan merelaksasi *semua* edge berulang kali sebanyak (Jumlah Node - 1) kali. 
#    Jika ada jalur memutar yang melewati bobot negatif dan membuat jarak 
#    total semakin kecil, Bellman-Ford pasti akan menemukannya di iterasi berikutnya.
#
# 5. Apa yang dimaksud dengan proses relaksasi edge?
#    Jawaban: Relaksasi edge adalah proses pengecekan dan pembaruan jarak. 
#    Sistem akan membandingkan jarak terpendek yang sudah tercatat saat ini 
#    menuju node tujuan, dengan "jalur alternatif" yang melewati node perantara. 
#    Jika jalur alternatif tersebut menghasilkan total jarak yang lebih kecil, 
#    maka catatan jarak akan diperbarui (di-relaksasi) menjadi nilai baru yang 
#    lebih optimal.
#
# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
#    Jawaban: 
#    - Dijkstra gagal jika ada bobot negatif, sedangkan 
#      Bellman-Ford didesain khusus untuk mampu menangani bobot negatif.
#    - Bellman-Ford dapat mendeteksi keberadaan "Negative Cycle" 
#      (siklus negatif yang membuat jarak terus mengecil tanpa batas), sedangkan 
#      Dijkstra tidak bisa.
#    - Performa : Dijkstra jauh lebih cepat dan efisien 
#      untuk graf yang besar (jika semua bobot positif) karena hanya memproses 
#      jalur prioritas. Bellman-Ford bekerja lebih lambat karena secara "brute force" 
#      harus memeriksa semua jalur berulang kali.
# ==========================================================