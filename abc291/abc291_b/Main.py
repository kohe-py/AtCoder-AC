N = int(input())
X = list(map(int, input().split()))
count = 0
X.sort()
for i in range(N, 4*N):
    count += X[i]
    #print(i)
print(count/(3*N))