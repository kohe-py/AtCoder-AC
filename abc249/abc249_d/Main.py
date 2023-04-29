import bisect
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
A_counter = defaultdict(int)
A.sort()
M = 2*10**5+1
for i in range(N):
    A_counter[A[i]] += 1
    
count = 0
for i in range(1, M):
    for j in range(1, M):
        k = i * j
        if A[-1] < k:
            break
        else:
            count += A_counter[i] * A_counter[k] * A_counter[j]
print(count)