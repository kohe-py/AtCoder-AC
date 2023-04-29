X, N = map(int, input().split())
p = list(map(int, input().split()))

P = set(p)
y = X
while True:
    if X not in P:
        print(X)
        break
    X += 1
    y -= 1
    if y not in P:
        print(y)
        break
    if X not in P:
        print(X)
        break