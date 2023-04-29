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

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


N, M = map(int, input().split())
d = defaultdict(int)
uf = UnionFind(N)
for _ in range(M):
    u, v = map(int, input().split())
    uf.union(u-1, v-1)
    e = uf.find(u-1)
    d[e] += 1

result = uf.all_group_members()
for i in range(N):
    if d[i] == len(result[i]):
        pass
    else:
        print("No")
        exit()
print("Yes")