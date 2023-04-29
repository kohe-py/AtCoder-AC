N = int(input())

import math

def prime(n):
    is_prime = [True] * (int(math.sqrt(n)) + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(2 * i, int(math.sqrt(n)) + 1, i):
                is_prime[j] = False
    return is_prime

x = prime(N)
p = []
count = 0
for i in range(len(x)):
    if x[i]:
        p.append(i)
        count += 1

p2 = []
for i in range(count):
    p2.append(p[i] ** 2)
    
ans = 0
#print(p)
import bisect
for i in range(count):
    result = p[i] ** 2
    for j in range(i+1, count - 1):
        result *= p[j]
        if result > N:
            break
        else:
            t = N // result + 1
            ind = bisect.bisect_left(p2, t)
            if p[j] < p[ind]:
                #print(ind, j)
                ans += (ind - j - 1)
        result //= p[j]

print(ans)