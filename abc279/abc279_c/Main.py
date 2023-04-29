H, W = map(int, input().split())
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]

i = 0
while i < H:
    s = 0
    t = 0
    for j in range(W):
        if S[i][j] == ".":
            s += 1
        if T[i][j] == ".":
            t += 1
    if s != t:
        print("No")
        break
    else:
        i += 1

if i == H:
    print("Yes")