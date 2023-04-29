N, M = map(int, input().split())
c = []
a = []
count = 0
for _ in range(M):
    C = int(input())
    A = list(map(int, input().split()))
    c.append(C)
    a.append(A)

for bit in range(1 << M):
    #print(bin(bit))
    s = set()
    for i in range(M):
        if bit & (1 << i):
            #print(i)
            for j in range(c[i]):
                s.add(a[i][j])
    if len(s) == N:
        count += 1
print(count)