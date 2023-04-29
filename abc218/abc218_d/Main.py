from collections import defaultdict
N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

s = set()
for i, j in xy:
    s.add((i, j))

count = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        else:
            a = xy[i][0]
            b = xy[i][1]
            c = xy[j][0]
            d = xy[j][1]
            if a == c or b == d:
                continue
            if (a, d) in s and (c, b) in s:
                count += 1

print(count//4)    