from collections import deque
Q = int(input())
S = 1
s = deque([1])
keta = 0
mod = 998244353
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        S *= 10
        S += q[1]
        s.append(q[1])
        S %= mod
        keta += 1

    elif q[0] == 2:
        v = int(s.popleft())
        S -= v * pow(10, keta, mod)
        keta -= 1
    else:
        print(S % mod)