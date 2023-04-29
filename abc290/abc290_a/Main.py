N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
b =set(B)
count = 0
for i in range(N):
    if i+1 in b:
        count += A[i]
print(count)