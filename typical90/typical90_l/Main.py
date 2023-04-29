from collections import defaultdict
 
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
 
    def find(self, x):
        #親を探す
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
 
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            #親が同じ　何もしない
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
 
    def size(self, x):
        # x が属しているグループの要素数
        return -self.parents[self.find(x)]
 
    def same(self, x, y):
        # 親が同じかどうか True or False
        return self.find(x) == self.find(y)
 
    def roots(self):
        # 根の要素を出力
        return [i for i, x in enumerate(self.parents) if x < 0]
    
    def group_count(self):
        # 連結している要素の数
        return len(self.roots())
 
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
    
H, W = map(int, input().split())
Q = int(input())

d = [[0] * W for i in range(H)]
table = [[0] * W for _ in range(H)]
uf = UnionFind(H*W)

count = 0
for i in range(H):
    for j in range(W):
        d[i][j] = count
        count += 1

for _ in range(Q):
    q = list(map(int, input().split()))
    if  q[0] == 1:
        x = d[q[1] - 1][q[2] - 1]
        table[q[1] - 1][q[2] - 1] = 1
        for i, j in ([0, 1], [1, 0], [-1, 0], [0, -1]):
            if 0 <= q[1] + i - 1 <= H - 1 and 0 <= q[2]- 1 + j <= W - 1:
                y = d[q[1] + i - 1][q[2]- 1 + j]
                if table[q[1] + i - 1][q[2]- 1 + j] == 1:
                    uf.union(x, y)

    else:
        x = d[q[1] - 1][q[2] - 1]
        y = d[q[3] - 1][q[4] - 1]
        if table[q[1] - 1][q[2] - 1] == 1 and table[q[3] - 1][q[4] - 1] == 1:
            if uf.same(x, y):
                print("Yes")
            else:
                print("No")
        else:
            print("No")