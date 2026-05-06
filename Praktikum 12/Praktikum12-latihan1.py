#===========================================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#===========================================================

# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================

# Representasi weighted graph menggunakan dictionary bersarang.
# Key utama adalah node, value-nya adalah node tujuan beserta bobotnya.
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D'] # Rute: A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D'] # Rute: A -> C -> D

# Menampilkan hasil perhitungan masing-masing jalur
print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

# Menentukan dan menampilkan jalur terpendek
if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")


# ==========================================================
# Soal & Jawaban Analisis:
# ==========================================================
# 1. Berapa total bobot jalur A -> B -> D?
#    Jawaban: Total bobotnya adalah 9. 
#    (Didapat dari bobot A->B yaitu 4, ditambah bobot B->D yaitu 5).
#
# 2. Berapa total bobot jalur A -> C -> D?
#    Jawaban: Total bobotnya adalah 3. 
#    (Didapat dari bobot A->C yaitu 2, ditambah bobot C->D yaitu 1).
#
# 3. Jalur mana yang dipilih sebagai jalur terpendek?
#    Jawaban: Jalur yang dipilih adalah A -> C -> D, karena total 
#    bobotnya (3) lebih kecil dibandingkan jalur A -> B -> D (9).
#
# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah 
#    edge yang paling sedikit?
#    Jawaban: Karena dalam 'weighted graph' (graf berbobot), setiap 
#    edge memiliki nilainya sendiri yang bisa merepresentasikan jarak, 
#    biaya, atau waktu. Jalur dengan jumlah edge lebih banyak bisa jadi 
#    memiliki total bobot keseluruhan yang lebih kecil/ringan dibandingkan 
#    jalur dengan sedikit edge tetapi berbobot sangat besar. 
#    
# ==========================================================
