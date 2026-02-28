#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
#Latihan 5: Generator PIN TANPA angka yang sama 
#=============================================


def buat_pin(panjang, hasil=""):

    # Base case: jika panjang sudah terpenuhi
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return

    # Recursive case
    for angka in ["0", "1", "2"]:
        # Cegah angka yang sudah dipakai sebelumnya
        if angka not in hasil:   
            buat_pin(panjang, hasil + angka)

#Generate pin dengan panjang 3 tanpa duplikasi
buat_pin(3)