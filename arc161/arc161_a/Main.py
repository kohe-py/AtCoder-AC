N = int(input())
A = list(map(int, input().split()))

A.sort()

g = A[N - (N // 2):]
k = A[:N // 2 + 1]

#print(k)
#print(g)

result = []
for i in range(N):
    if i % 2 == 0:
        result.append(k[i // 2])
    else:
        result.append(g[i // 2])
#print(result)

for i in range(N - (N // 2) - 1):
    ind = (2 * i) + 1
    if (result[ind - 1] < result[ind]) and (result[ind] > result[ind + 1]):
        pass
    else:
        print("No")
        exit()
print("Yes")