#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
#Latihan 2: Tracking Rekursi
#=============================================

def countdown(n):
    #Base case
  if n == 0:
    print("Selesai")
    return
  #printing log masuk
  print("Masuk:",n)
  #Pemanggilan rekursi
  countdown(n-1)
  #Printing log saat keluar
  print("Keluar:",n)

countdown(3)
# Menurut pengamatan saya Output keluar dikeluarkan secara terbalik
# dikarenakan alur pemanggilan akan menjalankan dari fungsi yang terakhir dipanggil
# Pada kasus ini, countdown(1) lah yang terakhir dipanggil dan masuk ke dalam base case
# jadi countdown 1 yang terlebih dahulu menjalankan print keluar dibanding countdown yang lebih besar

