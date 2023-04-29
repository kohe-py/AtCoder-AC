import bisect
from collections import deque
N, Q = map(int, input().split())
A = list(map(int ,input().split()))

# Aの要素の間の数を格納したリスト
nlist = [A[0] - 1]
for i in range(1, N):
    nlist.append(A[i] - A[i-1] - 1)


# nlistの累積和
B = [0]
B = deque(B)
for i in range(1, N+1):
    B.append(B[i-1] + nlist[i-1])
B.popleft()


for _ in range(Q):
    K = int(input())
    left = bisect.bisect_left(B, K)
    if A[-1] < K:
        print(A[-1] + K - B[-1])
    else:
        if left == 0:
            print(K)
        else:
            if left == N:
                print(A[-1] + K - B[-1])
            else:
                print(K - B[left - 1] + A[left - 1])