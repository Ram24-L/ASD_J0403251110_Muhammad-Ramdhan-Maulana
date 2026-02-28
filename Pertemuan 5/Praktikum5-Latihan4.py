#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
# Latihan 4: Kombinasi Huruf
#=============================================


def kombinasi(n, hasil=""):    
    # n = panjang kombinasi  (digit max kombinasi)
    # hasil = string sementara (default kosong)                 
    # BASE CASE:
     # Jika panjang string sudah sama dengan n
    if len(hasil) == n:          
        # Cetak kombinasi yang sudah jadi              
        print(hasil)             
        return
         # Hentikan rekursi (tidak lanjut bercabang)                  

    # RECURSIVE CASE:
    # Jika belum mencapai panjang n,
    # maka buat percabangan dengan menambah "A" dan "B"

    # Cabang 1 → tambahkan "A"
    kombinasi(n, hasil + "A")   
     # Cabang 2 → tambahkan "B" 
    kombinasi(n, hasil + "B")   


kombinasi(2)  # Meminta semua kombinasi panjang 2