#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
# Latihan 5 : Melengkapi Fungsi Merge
#=============================================

'''
1. Lengkapi kondisi agar menjadi ascending.
2. Jelaskan fungsi result.extend().

'''

'''
Soal
def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
    if __________________________:
        result.append(left[i])
        i += 1
    else:
        result.append(right[j])
        j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    '''
#Versi dilengkapi 
#Jawaban No 1
def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

'''
Jawaban No 2 : 
2. fungsi result.extend() 
    berfungsi untuk menggabungkan data yang tidak dibandingkan karena sudah terurut.
'''