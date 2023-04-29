S = input()
K = int(input())

N = len(S)

if S.count(".") <= K:
    print(N)
    exit()

s = []
for i in range(N):
    if S[i] == ".":
        s.append(i)
leng = len(s)
result = -1
if leng >= K:
    for i in range(leng-K-1):
        result = max(result, s[i+K+1] - s[i] - 1)
    if result < s[K]:
        result = s[K]
    if result < N - s[-K-1] - 1:
        result = N - s[-K-1] - 1
        
else:
    result = max(s[-1], N - s[0] - 1)
print(result)