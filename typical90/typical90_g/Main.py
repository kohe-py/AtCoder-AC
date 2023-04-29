N = int(input())
A = list(map(int, input().split()))
Q = int(input())
A.sort()
import bisect
for _ in range(Q):
    B = int(input())
    x = bisect.bisect_left(A, B)
    if x == 0:
        print(abs(A[0] - B))
    elif x == N:
        print(abs(A[-1] - B))
    else:
        print(min(abs(A[x] - B), abs(A[x-1] - B)))