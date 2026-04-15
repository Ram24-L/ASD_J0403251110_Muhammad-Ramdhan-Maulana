def mergesort(data):
    
    if len(data) <= 1:
        return data

    mid = len(data)//2 
    left = data[:mid]
    right = data[mid:]

    left_sorted = mergesort(left)
    right_sorted = mergesort(right)

    return merge(left_sorted,right_sorted)

def merge(left,right):
    result = []
    i = 0
    j = 0
    left_len = len(left)
    right_len = len(right)
    while(i < left_len and j < right_len):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    
    result.extend(left[i:])
    result.extend(right[j:])

    return result

list = [4,3,2,1,0]
list = mergesort(list)

print(list)