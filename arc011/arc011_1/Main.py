m, n, N = map(int, input().split())
result = N // m
mod = N % m
ans = N

while True:
    ans += (N // m) * n
    N = (N // m) * n + (N % m)
    if N < m:
        break

print(ans)