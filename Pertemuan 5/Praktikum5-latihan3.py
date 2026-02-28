#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
#Latihan 3: Mencari Nilai Maksimum
#=============================================

def cari_maks(data,index = 0):

    #Base Case
    #Base case terjadi ketika index sudah mencapai akhir list
    #Ini akan menghentikan recursive call dan mereturn nilai index terakhir tsb
    if index == len(data) - 1:
        return data[index]
    #Recursive Case
    #Recursive call akan memanggil list sampai akhir index
    maks_sisa = cari_maks(data,index+1)

    #Pengecekan dilakukan saat proses kembali (unwinding)
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa
    
angka = [3,7,2,9,5]
print("Nilai Maksimum : ", cari_maks(angka))
#Fungsi akan berakhir mengembalikan nilai maksimum dari list