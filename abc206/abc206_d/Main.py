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

N = int(input())
A = list(map(int, input().split()))

from collections import defaultdict
change = defaultdict(int)
B = set(A)

count = 0
for i in B:
    change[i] = count
    count += 1

g = UnionFind(count)

count = set()
count2 = set()
for i in range(N // 2):
    if A[-1 - i] != A[i]:
        g.union(change[A[-i-1]], change[A[i]])

ans = 0
for i in B:
    if change[i] != g.find(change[i]):
        ans += 1
print(ans)