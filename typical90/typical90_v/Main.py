A, B, C = map(int, input().split())

import math
gcd = math.gcd(A, B)
gcd = math.gcd(gcd, C)
ans = 0
if gcd not in {A, B, C}:
    ans = (A + B + C) // gcd - 3
else:
    for i in [A, B, C]:
        if i != gcd:
            ans += (i // gcd - 1)
print(ans)