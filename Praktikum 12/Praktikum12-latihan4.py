#===========================================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=========================================================

# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================
import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
            
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(f"{lokasi} = {jarak} menit")


# ==========================================================
# Jawaban Analisis:
# ==========================================================
# 1. Lokasi mana yang paling dekat dari Gerbang?
#    Jawaban: Kantin (dengan waktu tempuh 2 menit).
#
# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
#    Jawaban: 7 menit. 
#    (Rutenya adalah Gerbang -> Kantin -> Lab -> Aula, yaitu 2 + 4 + 1 = 7).
#
# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
#    Jawaban: Tidak selalu. Sebagai contoh pada kasus di atas, jika kita ingin
#    pergi dari Kantin ke Aula, ada jalur langsung (Kantin -> Aula) yang 
#    membutuhkan waktu 7 menit. Namun, jika kita menggunakan jalur memutar 
#    melewati Lab (Kantin -> Lab -> Aula), total waktunya justru lebih singkat, 
#    yaitu 4 + 1 = 5 menit. Algoritma mencari bobot total terkecil, bukan 
#    sekadar edge paling sedikit atau rute langsung.
#
# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
#    Jawaban: Karena dalam kasus lokasi kampus, bobotnya merepresentasikan 
#    "waktu tempuh". Waktu tempuh selalu bernilai positif (tidak mungkin ada 
#    waktu minus saat berpindah tempat). Algoritma Dijkstra dirancang khusus 
#    dan bekerja dengan sangat efisien pada graf yang hanya memiliki bobot positif.
# ==========================================================