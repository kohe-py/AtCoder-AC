N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]

def rotate(before):
    after = [["."] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            after[j][N - 1 - i] = before[i][j]
    return after

def cheack(S, after):
    s, a = [], []
    for i in range(N):
        for j in range(N):
            if S[i][j] == "#":
                s.append((i, j))
            if after[i][j] == "#":
                a.append((i, j))
    if len(s) != len(a):
        return False
    dx, dy = s[0][0] - a[0][0], s[0][1] - a[0][1]
    for i in range(1, len(s)):
        if s[i][0] - a[i][0] != dx or s[i][1] - a[i][1] != dy:
            return False
    return True

def watch(before):
    print("-----------------------")
    for i in range(N):
        print(before[i])
before = T
for i in range(4):
    if cheack(S, before):
        print("Yes")
        exit()
    before = rotate(before)
    #watch(before)
print("No")
