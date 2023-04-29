N, M = map(int, input().split())
A = list(map(int, input().split()))

from collections import defaultdict, deque, Counter
A.sort()

C = [A[0]]
for i in range(N - 1):
    if A[i + 1] - A[i] <= 1:
        C[-1] += A[i + 1]
    else:
        C.append(A[i + 1])

if len(C) >= 2 and N >= 2 and (A[0] == A[-1] or (A[-1] == (M - 1)and A[0] == 0)):
    C[0] += C[-1]

print(sum(A) - max(C))