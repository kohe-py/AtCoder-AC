K, S = map(int, input().split())
count = 0

for x in range(K+1):
    for y in range(K+1):
        Z = S - x - y
        if 0 <= Z <= K:
            count += 1

print(count)