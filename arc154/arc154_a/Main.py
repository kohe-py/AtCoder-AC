N = int(input())
A = int(input())
B = int(input())
a = str(A)
b = str(B)

newA = ""
newB = ""
for i in range(N):
    if int(a[i]) >= int(b[i]):
        newA += a[i]
        newB += b[i]
    else:
        newA += b[i]
        newB += a[i]
print((int(newA)*(int(newB)))%998244353)