# NAME: Tanon Likhittaphong
# Student ID: 6710545547

n = int(input("How many students? "))
names = []
grades = {}

for i in range(1, n+1):
    print()
    name = input(f"Enter name for student {i}: ").strip()
    scores = list(map(float, input(f"Enter scores for {name}: ").split()))
    names.append(name)
    grades[name] = scores

print()
print("Student Averages:")

for name in names:                  
    s = grades[name]
    avg = sum(s)/len(s)
    print(f"{name}: {avg:.2f}")

