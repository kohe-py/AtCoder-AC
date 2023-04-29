N = int(input())

leng = len(str(N))
mod = 998244353
ans = 0

for i in range(1, leng+1):
    x = min(10**i - 1, N) - 10**(i-1) + 1
    ans = (ans + x*(x+1)//2) % mod
print(ans)