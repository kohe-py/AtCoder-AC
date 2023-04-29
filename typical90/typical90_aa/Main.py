N = int(input())
S = [input() for _ in range(N)]

s = set()
ans = []
for i in range(N):
    if S[i] not in s:
        s.add(S[i])
        print(i+1)