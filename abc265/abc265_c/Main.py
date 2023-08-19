H, W = map(int, input().split())
G = [input() for _ in range(H)]

visit = {(0, 0)}
now = [0, 0]
dyx = {"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1)}
while True:
    i, j = now
    y, x = dyx[G[i][j]]
    if 0 <= i + y <= H - 1 and 0 <= j + x <= W - 1:
        if (i + y, j + x) not in visit:
            visit.add((i + y, j + x))
            now = (i + y, j + x)
        else:
            print(-1)
            exit()
    else:
        ansy, ansx = i + 1, j + 1
        print(ansy, ansx)
        exit()
