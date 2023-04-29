from collections import defaultdict
H, W, N = map(int, input().split())

hw = set()
ab = []
for i in range(N):
    a, b = map(int, input().split())
    hw.add((a, b))
    ab.append([a, b, i])

ab = sorted(ab, key = lambda x: x[0])
j = 1
for i in range(N):
    if i+1 <= N-1 and ab[i+1][0] == ab[i][0]:
        ab[i][0] = j
    else:
        ab[i][0] = j
        j += 1

ab = sorted(ab, key = lambda x: x[1])
j = 1
for i in range(N):
    if i+1 <= N-1 and ab[i+1][1] == ab[i][1]:
        ab[i][1] = j
    else:
        ab[i][1] = j
        j += 1

ab = sorted(ab, key = lambda x: x[2])
for i in range(N):
    print(ab[i][0], ab[i][1])