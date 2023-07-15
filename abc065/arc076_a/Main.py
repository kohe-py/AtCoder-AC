N, M = map(int, input().split())

if abs(N - M) >= 2:
    exit(print(0))

mod = 10 ** 9 + 7
import math 
ans = 0
if M > N:
  	M, N = N, M
    
p = math.factorial(N)
q = math.factorial(M)
ans += ((p % mod) * (q % mod))
ans %= mod
if M >= N:
    ans *= 2
    ans %= mod
print(ans)