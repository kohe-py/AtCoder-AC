N, x, y = map(int, input().split())
A = list(map(int, input().split()))

X = {A[0]}
Y = {0}
for i in range(2, N, 2):
    xx = set()
    for j in X:
        xx.add(j+A[i])
        xx.add(j-A[i])
    #print(xx)
    X = xx

for i in range(1, N, 2):
    yy = set()
    for j in Y:
        yy.add(j+A[i])
        yy.add(j-A[i])
    #print(yy)
    Y = yy
    
if x in X and y in Y:
    print("Yes")
else:
    print("No")