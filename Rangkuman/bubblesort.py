#Bubblesort Ascending
def bubble_sort(data):
    data_len = len(data)
    for i in range(data_len-1):
        for j in range(data_len-i-1):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
    return data

data = [5,4,3,2,1]
data = bubble_sort(data)
print(data)