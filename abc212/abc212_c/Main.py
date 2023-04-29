import bisect
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
C = set(B)
for i in range(N):
    if A[i] in C:
        print(0)
        exit()
ans = 10**9 + 3
for i in range(N):
    x = bisect.bisect_left(B, A[i])
    if x == M:
        x -= 1
    #print(A[i], B[x], x)
    q = min(abs(A[i] - B[x]), abs(A[i] - B[x-1]))
    ans = min(ans, q)
print(ans)