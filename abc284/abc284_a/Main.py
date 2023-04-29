N = int(input())
s = [input() for _ in range(N)]

for i in range(N-1, -1, -1):
    print(s[i])
