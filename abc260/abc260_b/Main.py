N, X, Y, Z = map(int,input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

AB = []
ans = []
for i in range(N):
    AB.append([A[i], B[i], A[i] + B[i],i+1])

AB = sorted(AB, key = lambda x:(-x[0], x[3]))
for j in range(X):
    ans.append(AB[j][3])

AB=AB[X:]

AB = sorted(AB, key = lambda x:(-x[1], x[3]))
for k in range(Y):
    ans.append(AB[k][3])
    
AB=AB[Y:]

AB = sorted(AB, key = lambda x:(-x[1]-x[0], x[3]))
for l in range(Z):
    ans.append(AB[l][3])
    

ans.sort()
for m in range(X+Y+Z):
    print(ans[m])