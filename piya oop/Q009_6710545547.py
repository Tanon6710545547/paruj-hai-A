# NAME: Tanon Likhittaphong
# Student ID: 6710545547

n = int(input("How many items in inventory? "))
items = []
same = [] 

for i in range(1, n+1):
    print()
    print(f"Item {i}")

    while True:
        name = input("Enter name: ").strip()
        if name.lower() in same:
            print("Invalid name, enter a different name")
        else:
            same.append(name.lower())
            break

    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    item = {"name": name,"price": price,"quantity": quantity}
    items.append(item)

print()
print("Inventory Details:")
total = 0

for item in items:
    sub = item["price"] * item["quantity"]
    total += sub
    print(f"{item['name']} - Price: {item['price']:.2f}, Quantity: {item['quantity']}, Subtotal: {sub:.2f}")

print()
print(f"Total inventory value: {total:.2f}")

