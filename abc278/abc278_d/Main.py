from collections import deque, Counter, defaultdict
N = int(input())
A = [0] + list(map(int, input().split()))
Q = int(input())

log = -1
add = defaultdict(int)
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        log = q[1]
        add = defaultdict(int)
    elif q[0] == 2:
        add[q[1]] += q[2]
    else:
        if log == -1:
            print(A[q[1]] + add[q[1]])
        else:
            print(log + add[q[1]])