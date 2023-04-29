from collections import deque
N, Q = map(int, input().split())
A = list(map(int, input().split()))
A = deque(A)
for _ in range(Q):
    T, x, y = map(int, input().split())
    if T == 1:
        A[x-1], A[y-1] = A[y-1], A[x-1]
    elif T == 2:
        A.appendleft(A.pop())
    else:
        print(A[x-1])