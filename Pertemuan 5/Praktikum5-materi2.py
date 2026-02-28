#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
#Materi Rekursif 2 : Tracing Masuk/ keluar 
#=============================================

def hitung(n):
    #Base Case
    if n == 0:
        print("Selesai")
        return
    
    print("Masuk:",n)   #Fase Stacking
    hitung(n-1)         #Pemanggilan rekursif
    print("Keluar:",n)  #Fase unwinding

hitung(3)