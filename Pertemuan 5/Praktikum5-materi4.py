#===============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#===============================================

#===============================================
#Materi Rekursif 4 : Backtraking kombinasi biner
#===============================================

def biner(n,hasil = ""):
    #Base case: jika panjang string sudah n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return
    
    #Choose + explore: tambah '0'
    biner(n,hasil+"0")

    #Choose + explore: tambah '1'
    biner(n, hasil+"1")

biner(3)