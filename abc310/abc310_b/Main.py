N, M = map(int, input().split())
from collections import defaultdict
F = defaultdict(list)
PC = []
for i in range(N):
    x = list(map(int, input().split()))
    F[i] = set(x[2:])
    PC.append(x[:2])

for i in range(N):
    for j in range(N):
        flag = True
        for a in F[i]:
            if a not in F[j]:
                flag = False
                break
        if flag == False:
            continue

        if flag:
            if PC[i][0] > PC[j][0]:
                print("Yes")
                exit()
            if PC[i][0] == PC[j][0] and PC[j][1] > PC[i][1]:
                print("Yes")
                exit()

print("No")