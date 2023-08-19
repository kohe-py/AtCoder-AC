H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]

x = set(range(W))
y = set(range(H))
h = [[0] * 26 for _ in range(H)]
w = [[0] * 26 for _ in range(W)]

for i in range(H):
    for j in range(W):
        h[i][ord(C[i][j]) - ord("a")] += 1
        w[j][ord(C[i][j]) - ord("a")] += 1

def main(h, w):
    global x, y
    # 消した行, 列を管理する配列
    g, r = [], []
    # まず各行を見る
    for i in y:
        if h[i].count(0) <= 24:
            continue
        for j in range(26):
            if h[i][j] >= 2:
                h[i][j] = 0
                g.append(i)
                break
    # 各列を見る
    for j in x:
        if w[j].count(0) <= 24:
            continue
        for i in range(26):
            if w[j][i] >= 2:
                r.append(j)
                w[j][i] = 0
                break
    if g == [] and r == []:
        return False, h, w
    # 印をつけたものを除外する
    for i in g:
        y.discard(i)
    for j in r:
        x.discard(j)
    for i in g:
        for j in range(W):
            w[j][ord(C[i][j]) - ord("a")] -= 1
    for j in r:
        for i in range(H):
            h[i][ord(C[i][j]) - ord("a")] -= 1
    return True, h, w
    
while True:
    flag, h, w = main(h, w)
    if flag == False:
        break

print(len(y) * len(x))