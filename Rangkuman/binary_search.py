def binarySearch(data, value):
    first = 0
    last = len(data) -1
    found = False

    while not found and first <= last:
        midpoint = (first+last)//2
        if(data[midpoint] == value):
            found = True
            return midpoint
        elif(data[midpoint] < value):
            first = midpoint + 1
        else:
            last = midpoint - 1
    return -1

data = [1,2,3,4,5]
print(binarySearch(data,4))
print(binarySearch(data,0))