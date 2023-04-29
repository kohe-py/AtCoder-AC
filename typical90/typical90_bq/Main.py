N, K = map(int, input().split())

mod = 10**9 + 7

if N >= 3 and K <= 2:
    print(0)
    exit()
if N == 1:
    print(K)
    exit()
if N == 2:
    print((K * (K - 1)) % mod )
    exit()

ans = 1
ans *= ((K * (K - 1) % mod) * (K - 2)) % mod
ans *= pow(K - 2, N - 3, mod)
print(ans % mod)