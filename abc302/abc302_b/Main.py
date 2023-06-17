H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

dxy = [(1,  0), (0, 1), (1, 1), (1, -1)]
def search(H, W, maze, string, i, j):
    #maze[i][j] == "s"
    for dy, dx in dxy:
        indy = i
        indx = j
        result = string[0]
        indxy = [[i, j]]
        for l in range(4):
            indy += dy
            indx += dx
            if indy > H - 1:
                indy = indy - H
            elif indy < 0:
                indy = H + indy
            if indx > W - 1:
                indx = indx - W
            elif indx < 0:
                indx = W + indx
            #print(indy, indx)
            result += maze[indy][indx]
            indxy.append([indy, indx])
        if result == string:
            count = 0
            for k in range(3):
                if string == "snuke":
                    if abs(indxy[k][0] - indxy[k + 1][0]) <= 1 and abs(indxy[k][1] - indxy[k + 1][1]) <= 1:
                        count += 1
                if string == "ekuns":
                    if abs(indxy[-k-1][0] - indxy[-k-2][0]) <= 1 and abs(indxy[-k-1][1] - indxy[-k-2][1]) <= 1:
                        count += 1
            if count == 3:
                return indxy
    return 

for i in range(H):
    for j in range(W):
        if S[i][j] == "s":
            result = search(H, W, S, "snuke", i, j)
            if result != None:
                for y, x in result:
                    print(y + 1, x + 1)
                exit()
        if S[i][j] == "e":
            result = search(H, W, S, "ekuns", i, j)
            if result != None:
                for k in range(5):
                    print(result[-k  - 1][0] + 1, result[-1-k][1] + 1)
                exit()
