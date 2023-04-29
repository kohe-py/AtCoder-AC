import bisect
N, Q = map(int, input().split())
A = list(map(int, input().split()))

#ソート→累積和→二分探索？
A.sort()
B = [0]
for i in range(1, N+1):
    B.append(B[i-1]+A[i-1])
    
for _ in range(Q):
    x = int(input())
    i = bisect.bisect_left(A, x)
    ans = 0
    if i == 0 or i == N:
        print(abs(abs(B[-1] - abs(x*N))))
    else:
        ans += (x*i - B[i])
        ans += (B[-1] - B[i] - x*(N-i))
        print(ans)