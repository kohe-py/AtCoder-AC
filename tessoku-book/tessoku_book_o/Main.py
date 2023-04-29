N = int(input())
A = list(map(int, input().split()))
a = []
for i in range(N):
    a.append([A[i], i])
a = sorted(a, key = lambda x:x[0])
b = [[1, a[0][1]]]
for i in range(1,N):
    if a[i-1][0] == a[i][0]:
        b.append([b[i-1][0],a[i][1]])
    else:
        b.append([b[i-1][0]+1, a[i][1]])
a = sorted(b, key = lambda x:x[1])
B = []
for i in range(N):
    B.append(a[i][0])
print(*B)