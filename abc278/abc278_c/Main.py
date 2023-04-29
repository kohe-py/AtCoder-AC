N, Q = map(int, input().split())
TAB = [list(map(int, input().split())) for _ in range(Q)]

f = set()

for i in range(Q):
    if TAB[i][0] == 1:
        f.add((TAB[i][1],TAB[i][2]))
    elif TAB[i][0] == 2:
        f.discard((TAB[i][1],TAB[i][2]))
    else:
        if (TAB[i][1],TAB[i][2]) in f and (TAB[i][2],TAB[i][1]) in f:
            print("Yes")
        else:
            print("No")