# NAME: Tanon Likhittaphong
# Student ID: 6710545547

n = int(input('Enter an odd number for the size: '))
if n <= 0 or n % 2 == 0:
    print('Error: Please enter a positive odd number.')
else:
    t = input('Enter the character to use: ').strip()[:1]
    x = n // 2
    for i in range(n):
        for j in range(n):
            if i == x or abs(i - x) + abs(j - x) == x:
                print(t, end='')
            else:
                print(' ', end='')
        print()




