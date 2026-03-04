#=============================================
#Nama   : Muhammad Ramdhan Maulana
#NIM    : J0403251110
#Kelas  : TPL B2
#=============================================

#=============================================
# Insertion Sort
#=============================================

def insertion_sort(data):
    panjang_data = len(data)
            #Melihat data awal
    print("Data Awal:",data)
    print("-"*50)
    #Loop mulai dari data ke 2 (Index Array ke-1)
    for i in range(1,panjang_data):


        key = data[i] #Simpan nilai yang disisipkan
        j = i-1 #Index elemen 

        print("Iterasi ke- ",i)
        print("Nilai Key = ",key)
        print("Bagian Kiri (Terurut) : ",data[:i])
        print("Bagian Kanan (Belum terurut:)",data[i:])
        print("-"*50)
        #Geser data jika tidak memenuhi inc/decrement
        while j>= 0 and data[j] > key:
            #Jika kunci lebih kecil, maka tukar data dengan kunci
            data[j+1] = data[j]
            #Geser j ke kiri hingga mencapai 0
            j -=1
        #Geser kunci
        data[j+1] = key

    return data

angka = [7,8,5,2,4,6]
print("Hasil Sorting : ",insertion_sort(angka))