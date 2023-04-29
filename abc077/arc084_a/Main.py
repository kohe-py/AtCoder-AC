import bisect
   
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

s = 0
for i in range(N):
    a_key = bisect.bisect_left(A,B[i])
    c_key = bisect.bisect_right(C,B[i])
    s += a_key*(N-c_key)

print(s)