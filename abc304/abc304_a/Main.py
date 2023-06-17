N = int(input())
sa = [list(map(str, input().split())) for _ in range(N)]

m = 10 ** 9
man = -1
for i in range(N):
    if m >= int(sa[i][1]):
        m = int(sa[i][1])
        man = i

for i in range(N):
    print(sa[(i + man) % N][0])
    