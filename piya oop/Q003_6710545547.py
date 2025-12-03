# NAME: Tanon Likhittaphong
# Student ID: 6710545547

import math
x = int(input("Enter a non-negative integer: "))
total = 0
if x <= 0:
    print("Factorial Sum is: 0")
else:
    for i in range(1,x+1):
        num = 1
        for j in range(1,i+1):
            num = num * j
        total += num
    print("Factorial Sum is:",total)