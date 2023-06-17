N, M = map(int, input().split())
s = [list(input()) for _ in range(N)]

import itertools
x = [i for i in range(N)]

x_list = list(itertools.permutations(x))
#print(x_list)
for li in x_list:
    count = 0
    for j in range(N - 1):
        c = 0
        for k in range(M):
            if s[li[j]][k] != s[li[j + 1]][k]:
                c += 1
        if c != 1:
            break
        else:
            count += 1
    if count == N - 1:
        print("Yes")
        exit()
print("No")
exit()