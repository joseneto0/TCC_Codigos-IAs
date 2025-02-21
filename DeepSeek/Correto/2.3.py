n = int(input())
names = []
seen = set()

for _ in range(n):
    name = input().strip()
    if name not in seen:
        seen.add(name)
        names.append(name)

for name in names:
    print(name)