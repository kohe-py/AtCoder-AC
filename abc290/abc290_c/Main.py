from collections import defaultdict
N, K = map(int, input().split())
A = list(map(int,input().split()))

a = defaultdict(int)
for i in range(N):
    a[A[i]] += 1
for j in range(K):
    if a[j] == 0:
        print(j)
        exit()
print(K)