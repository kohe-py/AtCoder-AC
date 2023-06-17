N = int(input())
A = list(map(int, input().split()))
from collections import defaultdict
count = defaultdict(int)
ans = [[i + 1, 0] for i in range(N)]
#print(ans)
for i in range(3 * N):
    count[A[i] - 1] += 1
    if count[A[i] - 1] == 2:
        ans[A[i] - 1][1] = i + 1

ans = sorted(ans, key=lambda x: x[1])
ans1 = []
for i in range(N):
    ans1.append(ans[i][0])

print(*ans1)