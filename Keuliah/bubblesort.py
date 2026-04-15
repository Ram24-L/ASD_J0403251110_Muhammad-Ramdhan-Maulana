def bubble_sort(data):
    n = len(data)

    for i in range(n):
        for j in range(0,n-i-1):
            if data[j] > data[j+1]:
                #Menukar Posisi
                data[j],data[j+1] = data[j+1],data[j]

    return data
# Average case O(N^2)



data = [64,45,25,12,22,11]
hasil = bubble_sort(data)
print(hasil)
