N, M, H, K = map(int, input().split())
S = input()
xy = set()
for _ in range(M):
    x, y = map(int, input().split())
    xy.add((x, y))

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
now = [0, 0]
if H >= N:
    print("Yes")
    exit()

for i in range(N):
    if H == 0:
        print("No")
        exit()

    if S[i] == "R":
        dy, dx = dxy[0]
    elif S[i] == "L":
        dy, dx = dxy[1]
    elif S[i] == "U":
        dy, dx = dxy[2]
    elif S[i] == "D":
        dy, dx = dxy[3]

    now[0] += dy
    now[1] += dx
    H -= 1
    check = (now[0], now[1])
    if check in xy and H < K:
        #print("check")
        H = K
        xy.discard(check)
    #print(now, H)

print("Yes")
