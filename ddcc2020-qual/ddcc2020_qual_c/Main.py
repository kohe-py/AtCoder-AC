H, W, K = map(int, input().split())

s = [list(input()) for _ in range(H)]
from collections import defaultdict, deque
ans = [[0] * W for _ in range(H)]

now = 1
itigo = deque()
for i in range(H):
    for j in range(W):
        if s[i][j] == "#":
            ans[i][j] = now
            now += 1

def main(starth, endh, dh, startw, endw, dw, num):
    for i in range(starth, endh, dh):
        for j  in range(startw, endw, dw):
            if num == 1 and 0 <= j - 1 and ans[i][j] == 0:
                ans[i][j] = ans[i][j - 1]
            elif num == 2 and j + 1 < W and ans[i][j] == 0:
                ans[i][j] = ans[i][j + 1]
            elif num == 3 and 0 <= i - 1 and ans[i][j] == 0:
                ans[i][j] = ans[i - 1][j]
            elif num == 4 and i + 1 < H and ans[i][j] == 0:
                ans[i][j] = ans[i + 1][j]

main(0, H, 1, 0, W, 1, 1)
main(0, H, 1, W - 1, -1, -1, 2)
main(0, H, 1, 0, W, 1, 3)
main(H - 1, -1, -1, 0, W, 1, 4)

for i in range(H):
    print(*ans[i])