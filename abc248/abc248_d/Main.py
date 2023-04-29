from collections import deque, defaultdict, Counter
import bisect

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
#整数 L,R,X が与えられてL～Rの区間でXの個数を求める
#要素ごとに出てくる場所を格納する
s = [[] for i in range(N+1)]
for i, x in enumerate(A):
    s[x].append(i)
#print(s)
for _ in range(Q):
    L, R, X = map(int, input().split())
    l = bisect.bisect_left(s[X], L-1)
    r = bisect.bisect_right(s[X], R-1)
    print(r - l)