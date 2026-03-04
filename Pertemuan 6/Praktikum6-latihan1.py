#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
# Latihan 1 : Memahami kode Program (insertion sort)
#=============================================
'''
Soal:
1. Mengapa perulangan dimulai dari indeks 1?
2. Apa fungsi variabel key?
3. Mengapa digunakan while, bukan for?
4. Operasi apa yang terjadi di dalam while?'''
# Soal :
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data

''' 
Jawaban
1.  Karena index 1 akan dijadikan sebagai acuan (key), yang merupakan pemisah
    antara data yang telah terurut dan belum terurut. Dimana, pada awalnya key (index 1)
    akan dibandingkan dengan index sebelumnya (0), jika loop dimulai dari 0 konsep
    ini tidak akan dapat tereksekusi
2.  Key merupakan acuan nilai yang ingin diurutkan pada iterasi tsb, key akan dibandingkan 
    dengan elemen sebelumnya, jika key lebih kecil dari pembanding (indeks j), maka akan dimasukkan ke j-1
    dan key bergeser ke elemen selanjutnya
3.  While digunakan disini karena akhir dari loop belum diketahui, dan berupa syarat yang dinamis
    sseperti j >= 0 dan data[j] > key
4.  pada while, key akan membandingkan dirinya dengan elemen elemen sebelumnya (j), jika j lebih besar
    dari key, maka data index j akan digeser ke kanan lalu disisipkan data pada index key, iterasi akan
    diulang hingga j < 0 (indeks awal habis)

'''