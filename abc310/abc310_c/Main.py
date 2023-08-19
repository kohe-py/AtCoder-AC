N = int(input())
S = [input() for _ in range(N)]

ans = set()
from collections import defaultdict
count = defaultdict(set)
for i in range(N):
    re = S[i][::-1]
    if re in ans or S[i] in ans:
        continue
    if S[i] not in ans:
        ans.add(S[i])
    
print(len(ans))
