# NAME: Tanon Likhittaphong
# Student ID: 6710545547

x = list(map(float, input("Enter base and height: ").split()))
a = x[0]*x[1]/2
if x[0] < 0 or x[1] < 0:
    print("Input incorrect")
else:
    print(f"Area: {a:.2f}")