N, Q = map(int, input().split())
A = list(map(int, input().split()))

diff = [0] * (N - 1)
first = 0
for i in range(N-1):
    d = A[i] - A[i + 1]
    first += abs(d)
    diff[i] = d 
#print(first)
for _ in range(Q):
    L, R, V = map(int, input().split())
    if L == 1 and R == N:
        print(first)
    elif L == 1:
        # |R - R+1| の変動を記録
        pre = abs(diff[R - 1])
        diff[R-1] += V
        first += (abs(diff[R-1]) - pre)
        print(first)
    elif R == N:
        # |L-1 - L| の変動を記録
        pre = abs(diff[L - 2])
        diff[L - 2] -= V
        first -= (pre - abs(diff[L - 2]))
        print(first)
    else:
        pre = abs(diff[R - 1])
        diff[R-1] += V
        first += (abs(diff[R-1]) - pre)
        pre = abs(diff[L - 2])
        diff[L - 2] -= V
        first -= (pre - abs(diff[L - 2]))
        print(first)
