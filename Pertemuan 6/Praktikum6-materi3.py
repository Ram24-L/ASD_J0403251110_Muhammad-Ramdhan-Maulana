#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
# Materi 3 : Merge Sort
#=============================================


def merge_sort(data,depth = 0):
    indent = " " * depth
    #Base Case
    if(len(data) <= 1):
        return data
    
    #Divde : Membagi data menjadi 2 bagian
    mid = len(data)//2
    left = data[:mid]   #Slicing Bagian Kiri
    right = data[mid:]  #Slicing Bagian Kanan


    #Recursive Call diperlukan agar data terbagi sampai menjadi 1
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted,right_sorted)

def merge(left,right):
    result = []
    i = 0
    j = 0

    #Membandingkan elemen kiri dan kanan
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    #Menambahkan sisa elemen jika ada
    result.extend(left[i:])
    result.extend(right[j:])
    return result

angka = [13,7,28,5,19,36,4]

print("Hasil Merge Sorting : ", merge_sort(angka))