N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
import bisect
for _ in range(Q):
    print(N - bisect.bisect_left(A, int(input())))