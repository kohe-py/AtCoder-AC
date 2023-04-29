N, X = map(int, input().split())
A = list(map(int, input().split()))
B = set(A)

for i in range(N):
    x = A[i] - X
    if x in B:
        print("Yes")
        exit()

print("No")