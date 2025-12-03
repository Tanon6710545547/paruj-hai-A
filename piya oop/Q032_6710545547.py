# NAME: Tanon Likhittaphong
# Student ID: 6710545547

import math
while True:
    try:
        num = input("Enter a non-negative number: ")
        number = float(num)
        
        if number < 0:
            print("Error: Cannot calculate the square root of a negative number.")
            continue

        sq = math.sqrt(number)
        print(f"The square root of {number} is {sq}.")
        break

    except ValueError:
        print("Error: Invalid input. Please enter a number.")