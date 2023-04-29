N = int(input())
g = []
for _ in range(N):
    x, y = map(int, input().split())
    g.append((x, y))

visited = set()
magica = set()

def GCD(A, B):
    if B == 0:
        return A
    r = A % B
    return GCD(B, r)

for i in range(N):
    for j in range(N):
        if i == j:
            continue

        a = g[i][0] - g[j][0]
        b = g[i][1] - g[j][1]
        x = GCD(a, b)
        magica.add((a//x, b//x))

print(len(magica)*2)