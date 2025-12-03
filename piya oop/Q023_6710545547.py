# NAME: Tanon Likhittaphong
# Student ID: 6710545547

from pathlib import Path

while True:
    entry = input("Enter journal entry (or 'DONE' to exit): ")
    
    if entry == "DONE":
        break
    
    file = open('journal.log', 'a')
    file.write(entry + "\n")
    file.close()
    
    print("Entry saved.")

print("Journal closed.")