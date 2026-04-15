with open("D:\IPB\Akademik\Semester 2\Algoritma dan Data Struktur\Rangkuman\data.txt","r",encoding="utf-8") as file:
    new_dict = {}
    for baris in file:
        data = baris.strip()
        nama,nilai = data.split(",")
        new_dict[nama] = nilai

print(new_dict)
