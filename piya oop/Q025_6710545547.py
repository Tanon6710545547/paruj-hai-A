# NAME: Tanon Likhittaphong
# Student ID: 6710545547

from pathlib import Path

input_filename = input("Enter the input filename: ")
word_to_find = input("Enter the word to find: ")
replacement_word = input("Enter the replacement word: ")
output_filename = input("Enter the output filename: ")

input_path = Path(input_filename)
if not input_path.exists():
    print(f"Error: Input file '{input_filename}' not found.")
else:
    with open(input_filename, 'r') as file:
        content = file.read()

    new_content = content.replace(word_to_find, replacement_word)

    with open(output_filename, 'w') as file:
        file.write(new_content)

    print(f"Replacement complete. Content saved to {output_filename}.")