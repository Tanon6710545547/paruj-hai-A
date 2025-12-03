# NAME: Tanon Likhittaphong
# Student ID: 6710545547

from pathlib import Path

name = input("Enter your name: ")

file = open('greeting.txt', 'w')
file.write(f"Hello, {name}! Welcome to file handling.")
file.close()

print("Greeting saved to greeting.txt")

# Hard

# # 1. ขอชื่อจากผู้ใช้
# name = input("Enter your name: ")

# # 2. สร้างข้อความที่จะเขียนลงไฟล์
# greeting_line = f"Hello, {name}! Welcome to file handling."

# # 3. เปิดไฟล์ greeting.txt ในโหมดเขียน (write mode)
# #    encoding='utf-8' เพื่อรองรับชื่อที่ไม่ใช่ภาษาอังกฤษ เช่น "นัท"
# with open("greeting.txt", "w", encoding="utf-8") as f:
#     f.write(greeting_line)

# # 4. แจ้งผู้ใช้ว่าเสร็จแล้ว
# print("Greeting saved to greeting.txt")
