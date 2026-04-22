#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
# Latihan 4 : Memahami Kode program (Merge Sort)
#=============================================

'''
Soal:
1. Apa yang dimaksud dengan base case?
2. Mengapa fungsi memanggil dirinya sendiri?
3. Apa tujuan fungsi merge()?
'''


def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)

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
Jawaban
1. Base case merupakan akhir dari rekursif, pada kasus ini, ketika setiap data 
    telah dibagi menjadi 1 individual
2. Pemanggilan diri sendiri diperlukan agar data dapat dipecah hingga
    menjadi 1 individual
3. Fungsi merge berfungsi untuk menyatukan list yang telah dipecah sambil
    mengurutkan individunya
'''