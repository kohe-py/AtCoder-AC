N = int(input())
A = list(map(int, input().split()))
Q = int(input())

B = []
win = 0
for i in range(N):
    win += A[i]
    B.append(win)

for i in range(Q):
    L, R = map(int, input().split())
    if L == 1:
        ans = B[R-1]
    elif L != 1:
        ans = B[R-1] - B[L-2]
    
    if 2*ans > R - L + 1:
        print("win")
    elif 2*ans == R - L + 1:
        print("draw")
    else:
        print("lose")