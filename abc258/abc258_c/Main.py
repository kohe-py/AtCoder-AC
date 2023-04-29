from collections import defaultdict, deque

N,Q = map(int, input().split())
q = input()

P = 0
for i in range(Q):
    x, y = map(int, input().split())
    if x == 1:
        P += y
    else:
        print(q[(y-1 - P)%N])