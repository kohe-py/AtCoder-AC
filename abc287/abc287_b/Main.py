N, M = map(int, input().split())
s = [input() for _ in range(N)]
t = {input() for _ in range(M)}
#print(s)
#print(t)
ans = 0
for i in range(N):
    #print(s[i][4:])
    if s[i][3:] in t:
        #print(s[i][4:])
        ans += 1
print(ans)