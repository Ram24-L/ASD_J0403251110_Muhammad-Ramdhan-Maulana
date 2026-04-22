#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
#Latihan 1 : Rekursi pangkat
#=============================================

#Buat fungsi pangkat rekursi dengan 2 parameter
#a = basis, n = pangkat
def pangkat(a,n):

    #Base Case (ketika rekursi berakhir)
    if n == 0:
        return 1
    
    # Recursive Case
    #Memanggil 1 pangkat dan mengalikannya dengan pangkat-1
    return a * pangkat(a,n-1)

#Menguji fungsi
print(pangkat(2,4)) #Output 16
# fungsi penghitung pangkat ini dapat berjalan dikarenakan terdapat base case dan recursive call
# Recursive call akan terjadi selama pangkat belum 0, artinya bilangan basis akan mengalikan
# dengan dirinya sendiri sebanyak pangkat itu sendiri (n)

