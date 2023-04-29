import bisect
N=int(input())
A=list(map(int,input().split()))
Q=int(input())
A.sort()
for _ in range(Q):
    X=int(input())
    print(bisect.bisect_left(A,X))