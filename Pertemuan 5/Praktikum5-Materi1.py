#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
#Materi 1, Fungsi Rekursif : Faktorial
#=============================================

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

while(True):    
    x = int(input("Penghitung Bilangan Factorial : "))
    print(f"{x} Faktorial adalah : ",factorial(x))
    lagi = input("Hitung lagi? [Y/N] : ").upper().strip()
    if lagi =="Y":
        continue
    else:
        break