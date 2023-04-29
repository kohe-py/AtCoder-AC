import bisect
from collections import deque
N = int(input())
A = list(map(int, input().split()))

# 累積
B = [0]
for i in range(2*N):
    B.append(B[-1] + A[i % (N)])

if B[N] % 10 != 0:
    print("No")
    exit()

#print(B)
ans = B[N] // 10 
for i in range(1, 2*N+1):
    # iは左の選び方
    # 右は二分探索で選ぶ
    # ans = 
    result = -B[i - 1]
    x = ans - result
    ind = bisect.bisect_left(B, x)
    #print(x, B[ind])
    if B[ind] == x and ind - i < N:
        print("Yes")
        exit()
print("No")
