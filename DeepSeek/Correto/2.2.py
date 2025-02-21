N = int(input())
count = 0
for _ in range(N):
    msg = input().strip()
    if 'fada' in msg.lower():
        count +=1
print(count)