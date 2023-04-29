N, M, T = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]
n = N
N -= ab[0][0]
if N <= 0:
    print("No")
    exit()
    
for i in range(M-1):
    N += (ab[i][1] - ab[i][0])
    if N > n:
        N = n
    N -= (ab[i+1][0] - ab[i][1])
    if N <= 0:
        print("No")
        exit()
N += (ab[-1][1] - ab[-1][0])
if N > n:
    N = n
N -= (T - ab[-1][1])
if N <= 0:
    print("No")
else:
    print("Yes")
