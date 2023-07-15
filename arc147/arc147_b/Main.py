N = int(input())
P = list(map(int, input().split()))

ans = []

for j in range(N):
    for i in range(N - 1):
        if P[i] % 2 != (i + 1) % 2 and P[i + 1] % 2 != i % 2:
            P[i], P[i + 1] = P[i + 1], P[i]
            ans.append(("A", i + 1))
        elif i + 2 < N and P[i] % 2 != (i + 1) % 2 and P[i + 2] % 2 == (i + 1) % 2:
            P[i], P[i + 2] = P[i + 2], P[i]
            ans.append(("B", i + 1))

for i in range(1, N + 1):
    j = P.index(i)
    if i == j:
        continue
    while i < j + 1:
        P[j], P[j - 2] = P[j - 2], P[j]
        ans.append(("B", j - 1))
        j -= 2
#print(P)
print(len(ans))
for i in range(len(ans)):
    print(*ans[i])
