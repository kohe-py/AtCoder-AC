N,M,T = map(int, input().split())
A = list(map(int, input().split()))
xy={}
for i in range(N):
    xy[i] = 0
    
for i in range(M):
    X, Y = map(int, input().split())
    xy[X-1] = Y
#print(xy)
for i in range(N-1):
    T -= A[i]
    if T <= 0:
        print("No")
        exit()

    T += xy[i+1]

print("Yes")