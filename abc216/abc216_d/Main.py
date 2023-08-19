N, M = map(int, input().split())
A = []
K = []
from collections import deque, defaultdict
for _ in range(M):
    k = int(input())
    a = list(map(int, input().split()))
    K.append(k)
    A.append(a[::-1])

same = []
top = [[] for _ in range(N)]
rest = defaultdict(int)
for i in range(M):
    color = A[i].pop()
    top[color - 1].append(i)
    rest[i] = K[i] - 1

for i in range(N):
    if len(top[i]) == 2:
        same.append(i)

flag = 0
while same:
    color = same.pop()
    flag += 1
    i, j = top[color]
    if rest[i] >= 1:
        rest[i] -= 1
        ci = A[i].pop()
        top[ci - 1].append(i)
        if len(top[ci - 1]) == 2:
            same.append(ci - 1)
    if rest[j] >= 1:
        rest[j] -= 1
        cj = A[j].pop()
        top[cj - 1].append(j)
        if len(top[cj - 1]) == 2:
            same.append(cj - 1)
if flag == N:
    print("Yes")
    exit()
print("No")