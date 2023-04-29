L1, R1, L2, R2 = map(int, input().split())

N = max(L1, L2, R1, R2)
x = [0 for _ in range(N)]
for i in range(L1, R1):
    x[i] += 1
for j in range(L2, R2):
    x[j] += 1
c = 0
for i in range(N):
    if x[i] == 2:
        c += 1
print(c)   