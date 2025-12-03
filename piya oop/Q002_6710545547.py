# NAME: Tanon Likhittaphong
# Student ID: 6710545547

x = list(map(int, input("Enter three integers: ").split()))
sum_x = sum(x)
if sum_x == 0:
    sum_x = "Zero"
elif sum_x % 2 == 0:
    sum_x = "Even"
else:
    sum_x = "Odd"
max_x = max(x)
min_x = min(x)

print("Sum:",sum_x)
print("Max:",max_x)
print("Min:",min_x)
