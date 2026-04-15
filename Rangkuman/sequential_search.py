def seq_search(data,key):
    found = False
    len_data = len(data)
    for i in range(len_data):
        if data[i] == key:
            found = True
            return found
    else:
        return found
    
data = [1,2,3,4,5]
print(seq_search(data,0))