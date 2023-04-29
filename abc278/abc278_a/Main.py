N,K = map(int, input().split())
A = list(map(int, input().split()))

for k in range(K):
    A.pop(0)
    A.append(0)

print(*A)