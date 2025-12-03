# NAME: Tanon Likhittaphong
# Student ID: 6710545547

x = int(input("Enter size of triangle: "))
y = input("Enter pattern string: ")

if x <= 0 or y == "":
    print("Invalid input")
else:
    k = 0
    q = len(y)
    for i in range(1, x+1):
        for j in range(i):
            print(y[k], end="")
            k += 1
            if k == q:
                k = 0
        print()