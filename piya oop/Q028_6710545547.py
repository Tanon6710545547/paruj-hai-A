# NAME: Tanon Likhittaphong
# Student ID: 6710545547

import csv

sales_data = {}

file = open('sales.tsv', 'r')
reader = csv.reader(file, delimiter='\t')

header = next(reader)

for row in reader:
    if len(row) >= 3:
        region = row[0]
        sales_amount = float(row[2])
        
        if region in sales_data:
            sales_data[region] += sales_amount
        else:
            sales_data[region] = sales_amount

file.close()

print("--- Regional Sales Summary ---")
for region in sales_data:
    total_sales = sales_data[region]
    print(f"{region}: ${total_sales:.2f}")