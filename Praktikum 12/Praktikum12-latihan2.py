#===========================================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=========================================================

# ==========================================================
# Latihan 2: Implementasi Dijkstra
# ==========================================================
import heapq

# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0
    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
        # maka proses dilewati
        if current_distance > distances[current_node]:
            continue
            
        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

# Menjalankan fungsi
hasil = dijkstra(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(f"{node} = {distance}")

# ==========================================================
# Jawaban Analisis:
# ==========================================================
# 1. Berapa jarak terpendek dari A ke B?
#    Jawaban: 4 (Jalur langsung A -> B).
#
# 2. Berapa jarak terpendek dari A ke C?
#    Jawaban: 2 (Jalur langsung A -> C).
#
# 3. Berapa jarak terpendek dari A ke D?
#    Jawaban: 3 (Melalui jalur A -> C -> D).
#
# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
#    Jawaban: Karena algoritma Dijkstra menghitung total akumulasi bobot.
#    Total bobot jalur A -> C -> D adalah 3 (2 + 1), sedangkan total bobot 
#    jalur A -> B -> D adalah 9 (4 + 5). 3 lebih kecil dari 9.
#
# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
#    Jawaban: Priority queue berfungsi untuk selalu memilih dan memproses 
#    node dengan jarak akumulasi paling kecil/terpendek  terlebih dahulu.
#    Hal ini memastikan efisiensi algoritma, sehingga
#    rute optimal ditemukan lebih cepat tanpa harus mengeksplorasi 
#    jalur-jalur panjang yang tidak perlu.
#
# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
#    Jawaban: Algoritma Dijkstra memiliki asumsi dasar bahwa:
#    "Menambahkan sebuah edge ke dalam sebuah jalur pasti akan 
#    menambah total jaraknya, atau setidaknya tetap."
#    Oleh karena itu, ketika sebuah node dikeluarkan dari priority queue, 
#    Dijkstra menganggap jarak terpendek ke node tersebut sudah 'final' dan 
#    tidak akan pernah mengevaluasinya lagi. Jika ada bobot negatif, jalur
#    yang tadinya dianggap sudah final bisa jadi memiliki jarak yang lebih 
#    kecil lagi di masa depan, membuat hasil akhir Dijkstra menjadi tidak akurat.
# ==========================================================