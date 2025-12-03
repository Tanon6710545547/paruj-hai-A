# NAME: Tanon Likhittaphong
# Student ID: 6710545547

x = int(input("Enter number of rows: "))
y = int(input("Enter number of columns: "))

matrix = []
for i in range(x):
    row = list(map(int, input(f"Enter row {i+1}: ").split()))
    matrix.append(row)

print()
print("Transposed Matrix:")

for j in range(y):
    for i in range(x):
        print(matrix[i][j], end=" ")
    print()