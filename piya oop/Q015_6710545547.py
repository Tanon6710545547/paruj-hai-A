# NAME: Tanon Likhittaphong
# Student ID: 6710545547

import math

groups = {} 

while True:
    line = input("Enter group name and coordinates (x y z) or 'done' to finish: ").strip()
    if line == "done":
        break
    parts = line.split()
    name, x, y, z = parts[0], float(parts[1]), float(parts[2]), float(parts[3])
    groups[name] = (x, y, z)

pairs = []
names = list(groups.keys())

for i in range(len(names)):
    for j in range(i + 1, len(names)):
        a, b = names[i], names[j]
        (x1, y1, z1), (x2, y2, z2) = groups[a], groups[b]
        d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
        a2, b2 = sorted([a, b])
        pairs.append((d, f"{a2} to {b2}"))

pairs.sort(key=lambda t: (t[0], t[1]))
print()
print("Top minimum distance pairs (show only top-5):")
limit = min(5, len(pairs))

for idx in range(limit):
    d, label = pairs[idx]
    print(f"{idx+1}. {label}: {d:.2f}")
