N = int(input())
A = list(map(int, input().split()))

from collections import defaultdict
ans = []
for i in range(N - 1):
    ans.append(A[i])
    if abs(A[i] - A[i + 1]) == 1:
        pass
    else:
        if A[i + 1] > A[i]:
            for j in range(A[i] + 1, A[i + 1]):
                ans.append(j)
        else:
            for j in reversed(range(A[i + 1] + 1, A[i])):
                ans.append(j)
ans.append(A[-1])
print(*ans)