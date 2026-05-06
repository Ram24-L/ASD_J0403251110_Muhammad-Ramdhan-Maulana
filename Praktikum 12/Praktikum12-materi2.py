#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
# Materi : Algoritma djikstra pada weighted graph
#=============================================


# Nama File: praktikum12.materi2.py

def bellman_ford(graph, start):
    """
    Fungsi untuk menghitung jarak terpendek dari satu titik ke semua titik lainnya.
    Mendukung graf dengan bobot tepi (edge) negatif.
    """
    
    # 1. INISIALISASI
    # Atur semua jarak ke node lain sebagai tak terhingga (infinity)
    distances = {node: float('inf') for node in graph}
    # Jarak ke node awal adalah 0
    distances[start] = 0

    # 2. PROSES RELAKSASI (Sebanyak V - 1 kali)
    # V adalah jumlah simpul (node) dalam graf.
    # Kita melakukan pengulangan sebanyak (jumlah_node - 1) karena jalur 
    # terpendek yang mungkin tanpa siklus maksimal memiliki V-1 tepi.
    for i in range(len(graph) - 1):
        # Periksa setiap node dan tetangganya
        for node in graph:
            for neighbor, weight in graph[node].items():
                # Jika ditemukan jalur yang lebih pendek, perbarui nilainya
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
        
        # Penjelasan: Pada setiap iterasi i, kita menjamin telah menemukan 
        # semua jalur terpendek dengan panjang maksimal i+1 tepi.

    # 3. DETEKSI SIKLUS NEGATIF (Langkah Tambahan)
    # Lakukan relaksasi sekali lagi untuk mengecek apakah masih ada nilai yang mengecil.
    # Jika masih ada, berarti graf tersebut memiliki "Negative Cycle".
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                print("Peringatan: Graf mengandung siklus negatif (Negative Cycle)!")
                return None

    return distances

# --- CONTOH PENGGUNAAN ---

# Representasi Graf dengan dictionary (mendukung bobot negatif)
graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}

start_node = 'A'
hasil = bellman_ford(graph, start_node)

if hasil:
    print(f"Jarak terpendek dari Node {start_node}:")
    for node, jarak in hasil.items():
        print(f"Ke Node {node} : {jarak}")