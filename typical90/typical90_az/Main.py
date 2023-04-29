N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

ans = 1
for i in range(N):
    ans *= sum(A[i])
    ans %= (10**9 + 7)

print(ans)