def insertion_sort(data):
    data_len =len(data)
    for i in range(1,data_len):
        j = i-1
        key = i
        while(j >= 0 and data[j] > key):
            data[j+1] = data[j]
            j-=1
        data[j+1] = key
    return data

x = [4,3,2,1]
x = insertion_sort(x)
print(x)
