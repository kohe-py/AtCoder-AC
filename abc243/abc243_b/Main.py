N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

count = 0
for i in range(N):
    if A[i] == B[i]:
        count += 1
c = 0
for i in range(N):
    for j in range(N):
        if i != j:
            if A[i] == B[j]:
                c += 1
print(count)
print(c)