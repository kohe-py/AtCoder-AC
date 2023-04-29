N,K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

ab = []
for i in range(N):
    for j in range(N):
        ab.append(A[i]+B[j])
cd = set()
for i in range(N):
    for j in range(N):
        cd.add(C[i]+D[j])
a= len(ab)
for i in range(a):
    X = K - ab[i]
    if X in cd:
        print("Yes")
        exit()
            
print("No")