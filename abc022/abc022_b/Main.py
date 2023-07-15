N = int(input())
A = [int(input()) for _ in range(N)]

from collections import defaultdict
cnt = defaultdict(lambda: False)
ans = 0
for i in range(N):
    if cnt[A[i] - 1] == False:
        cnt[A[i] - 1] = True
    else:
        ans += 1
print(ans)