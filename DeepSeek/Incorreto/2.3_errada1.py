n = int(input())
names = [input().strip() for _ in range(n)]
unique_names = list(set(names))
print(' '.join(unique_names))