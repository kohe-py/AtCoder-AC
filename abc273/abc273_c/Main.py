N = int(input())
A = list(map(int, input().split()))

B = set(A)
leng = len(B)
B = list(B)
B.sort()
import bisect

ans = [0] * N
for i in range(N):
    ind = bisect.bisect_left(B, A[i])
    result = leng - ind - 1
    ans[result] += 1

for i in range(N):
    print(ans[i])