N = int(input())

nlist = [True] * (N+1)
nlist[0] = False
nlist[1] = False

flag = N ** (1/2)
for i in range(2, N+1):
    if nlist[i] == False:
        continue
    for j in range(i * 2, N+1, i):
        nlist[j] = False
    
result = []
for i in range(N+1):
    if nlist[i]:
        result.append(i)
print(*result)