A, B, C = map(int, input().split())
mod = 998244353

a = A*(A+1)//2
b = B*(B+1)//2
c = C*(C+1)//2

ans = 1
ans *= a
ans %= mod
ans *= b
ans %= mod
ans *= c
ans %= mod
print(ans)