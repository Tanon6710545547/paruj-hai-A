# NAME: Tanon Likhittaphong
# Student ID: 6710545547

text = input("Enter a string: ").lower()
text = text.replace(" ", "")

if text == "":
    print("Empty input")
else:
    count = {}
    for ch in text:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    for ch, num in count.items():
        print(f"{ch}: {num}")