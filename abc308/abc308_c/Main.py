N = int(input())

from decimal import *
vec = []
INF = 2*10**(9) + 2
for i in range(N):
    A, B = map(int, input().split())
    vec.append((i, A * 10 ** (20) // (A + B)))

#print(vec)

vec = sorted(vec, key = lambda x:(-x[1], x[0]))
ans = []
for i in range(N):
    ans.append(vec[i][0] + 1)

print(*ans)