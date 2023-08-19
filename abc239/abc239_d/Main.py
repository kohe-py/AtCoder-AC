A, B, C, D = map(int, input().split())

import math
prime = [True] * 201
prime[0] = False
prime[1] = False

for i in range(2, int(math.sqrt(200)) + 1):
    if prime[i]:
        for j in range(2 * i, 201, i):
            prime[j] = False
s = set()
for i in range(A, B + 1):
    flag = True
    for j in range(C, D + 1):
        if prime[i + j]:
            flag = False
    s.add(flag)
if True in s:
    print("Takahashi")
else:
    print("Aoki")