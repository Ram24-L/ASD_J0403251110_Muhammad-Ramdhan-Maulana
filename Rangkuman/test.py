list1 = [10, 20, 30]
list2 = [30, 40, 50]

# Using the extend() method
list1.extend(list2)
print(list1)
# Output: [10, 20, 30, 40, 50, 60]

with open("data.txt","r",encoding="utf-8") as file:
    for lines in file:
        print(lines)