try:
    with open("data.txt","r", encoding="utf-8") as r:
        print(r)
except FileNotFoundError:
     with open("data.txt","w", encoding="utf-8") as r:
         print(r)
        # Create a simple table without libraries

data = [
    ["Nama", "Nilai", "Grade"],
    ["Ali", "85", "B"],
    ["Budi", "92", "A"],
    ["Citra", "78", "C"]
]

# Calculate column widths
col_widths = [max(len(str(row[i])) for row in data) for i in range(len(data[0]))]

# Print table
for row in data:
    print(" | ".join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row)))
    if row == data[0]:
        print("-" * (sum(col_widths) + 3 * (len(col_widths) - 1)))


p = [1,2,3,4]
print(p.index(4))
p.pop(2)
print(p)