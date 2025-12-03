# NAME: Tanon Likhittaphong
# Student ID: 6710545547

print("Enter coefficients for f(x) = ax^2 + bx + c")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

print("")
print("Enter coefficients for g(x) = dx^2 + ex + f")
d = float(input("d: "))
e = float(input("e: "))
f = float(input("f: "))

print("")
start_int = float(input("Enter the start of the interval (a): "))
end_int = float(input("Enter the end of the interval (b): "))
num_trap = int(input("Enter the number of trapezoids (n): "))

if start_int >= end_int:
    print("Error: The start of the interval must be less than the end.")
elif num_trap <= 0:
    print("Error: The number of trapezoids must be a positive integer")
else:
    dx = (end_int - start_int) / num_trap

    def f1(x):
        return (a * x * x) + (b * x) + c

    def f2(x):
        return (d * x * x) + (e * x) + f

    area = 0.0
    for i in range(num_trap):
        x_i = start_int + i * dx
        x_next = x_i + dx
        y1 = abs(f1(x_i) - f2(x_i))
        y2 = abs(f1(x_next) - f2(x_next))
        area += (y1 + y2) * dx / 2

    print(" ")
    print(f"Approximate area: {area:.6f}")
