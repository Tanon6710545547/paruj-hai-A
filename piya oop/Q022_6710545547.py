# NAME: Tanon Likhittaphong
# Student ID: 6710545547

from pathlib import Path

filename = input("Enter the filename to read: ")

if not Path(filename).exists():
    print(f"Error: The file '{filename}' was not found.")
else:
    file = open(filename, 'r')
    content = file.read()
    file.close()

    print("--- File Content ---")
    print(content)

    words = content.split()
    word_count = len(words)

    print("--- Word Count ---")
    print(f"Total words: {word_count}")

