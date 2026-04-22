#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
# Latihan 2 : Melengkapi Potongan Kode
#=============================================

#Soal
'''
Soal:
1. Lengkapi kondisi agar menjadi sorting ascending.
2. Ubah agar menjadi descending.

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

    while j >= 0 and ______________________:
        data[j + 1] = data[j]
        j -= 1

    ______________________

    return data
'''

#Jawaban No 1
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

    while j >= 0 and data[j] > key:
        data[j + 1] = data[j]
        j -= 1

    data[j+1] = key 

    return data

#Jawaban No 2 (Ubah Descending)
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

    while j >= 0 and data[j] < key:
        data[j + 1] = data[j]
        j -= 1

    data[j+1] = key 

    return data