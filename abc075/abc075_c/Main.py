from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    def group_count(self):
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


#certmagr.msc

N, M = map(int, input().split())
uf = UnionFind(N)
nlist = []
for i in range(M):
    a,b = map(int, input().split())
    nlist.append([a-1, b-1])

count=0
for i in range(M):
    uf2 = UnionFind(N)
    for j in range(M):
        if i != j:
            uf2.union(nlist[j][0], nlist[j][1])
    if len(uf2.roots())>1:
        count +=1

print(count)