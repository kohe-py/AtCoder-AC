N, K = map(int, input().split())
A = list(map(int, input().split()))

# 最初の転倒数
count = [0] * N
tentou = [0] * N
for i in range(N):
    for j in range(i + 1, N):
        if A[i] > A[j]:
            tentou[i] += 1

for i in range(N):
    for j in range(N):
        if A[i] > A[j]:
            count[i] += 1


result = sum(tentou)
ans = 0
for i in range(N):
    ans += (count[i] * (K - 1) * K // 2)

ans += result * (K)
print(ans % (10 ** 9 + 7))