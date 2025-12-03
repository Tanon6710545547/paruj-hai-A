# NAME: Tanon Likhittaphong
# Student ID: 6710545547

def count(x):
    vowel = "aeiou"
    count = 0
    for i in x.lower():
        if i in vowel:
            count += 1
    return count

while True:
    x = input("Enter a sentence (or 'exit' to quit): ")
    if x.lower() == "exit":
        print("Goodbye!")
        break
    else:
        y = count(x)
        print(f"Vowels: {y}")

