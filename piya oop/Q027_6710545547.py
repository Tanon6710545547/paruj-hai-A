# NAME: Tanon Likhittaphong
# Student ID: 6710545547

import csv

category = input("Enter category to filter by: ")

file = open('inventory.csv', 'r')
reader = csv.reader(file)

header = next(reader)

found_items = False

for row in reader:
    if len(row) >= 4:
        item_category = row[2]
        if item_category.lower() == category.lower():
            if not found_items:
                print(f"Items in category '{category}':")
                found_items = True
            print(f"Item: {row[1]}, Stock: {row[3]}")

file.close()

if not found_items:
    print(f"No items found in category '{category}'.")