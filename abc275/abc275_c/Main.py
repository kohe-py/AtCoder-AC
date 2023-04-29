from collections import deque, defaultdict
S = [input() for _ in range(9)]

#前処理 #の(x, y)
point = []
for i in range(9):
    for j in range(9):
        if S[i][j] == "#":
            point.append((i, j))

#正方形の条件　辺の長さと対角線？

#長さ
def dist(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2

x = len(point)
count = 0
for i in range(x):
    c1 = point[i]
    for j in range(x):
        c2 = point[j]
        if c1 == c2:
            continue
        for k in range(x):
            c3 = point[k]
            if c3 == c2 or c3 == c1:
                continue
            for l in range(x):
                c4 = point[l]
                if c4 == c1 or c4 == c2 or c4 == c3:
                    continue
                a = dist(c1, c2)
                b = dist(c2, c3)
                c = dist(c3, c4)
                d = dist(c4, c1)
                e = dist(c1, c3)
                f = dist(c2, c4)
                if a == b == c == d:
                    if e == f:
                        count += 1
                        
print(count//8)  