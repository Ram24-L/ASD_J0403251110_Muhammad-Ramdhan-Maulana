#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
#Materi Rekursif 3 : Menjumlahkan elemen list 
#=============================================

def jumlah_list(data,index = 0):
    #Base Case: jika index sudah mencapai panjang list
    if index == len(data):
        return 0

    #Recursive case: elemen sekarang + jumlah elemen setelahnya
    return data[index] + jumlah_list(data,index+1)

print(jumlah_list([2,4,6,8])) #Output: 20

