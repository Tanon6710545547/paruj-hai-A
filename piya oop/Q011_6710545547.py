# NAME: Tanon Likhittaphong
# Student ID: 6710545547

trans = {}

while True:
    name = input("Enter transaction description (or 'done' to finish): ")
    if name == 'done':
        break
    name = name.__add__(':')
    amount = float(input(f'Enter amount for {name} '))
    if amount != 0:
        trans[name] = amount

up = sum(v for v in trans.values() if v >= 0)
down = sum(v for v in trans.values() if v < 0)
net = up + down

print()
print('--- FINANCIAL REPORT ---')
print('Transactions:')

for key, value in trans.items():
    if value > 0:
        print(f'+ {key:<15}${value:8.2f}')
    else:
        print(f'- {key:<15}${value:8.2f}')

print('-'*24)
print(f'{'Total Income:':<17}${up:8.2f}')
print(f'{'Total Expenses:':<17}${down:8.2f}')
print(f'{'Net Balance:':<17}${net:8.2f}')
print('-'*24)



