# NAME: Tanon Likhittaphong
# Student ID: 6710545547

def table(x):
    if x <= 0:
        print("Invalid input")
        return
    
    for i in range(1, x + 1):
        for j in range(1, x + 1):
            print(f"{i * j:4}", end="")
        print()


x = int(input("Enter table size: "))
table(x)