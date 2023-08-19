N, M = map(int, input().split())
S = input()
C = list(map(int, input().split()))

from collections import defaultdict
ind = defaultdict(list)
change = [""] * N
for i in range(N):
    ind[C[i]].append(i)

for i in range(M):
    for j in range(len(ind[i + 1])):
        if j == 0:
            change[ind[i + 1][j]] = S[ind[i + 1][-1-j]]
        else:
            change[ind[i + 1][j]] = S[ind[i + 1][j - 1]]
    
print("".join(change))