N = int(input())
P = list(map(int, input().split()))

maxp= 0
for i in range(1, N):
    maxp = max(maxp, P[i])

if maxp < P[0]:
    print(0)
else:
    print(maxp - P[0] + 1)