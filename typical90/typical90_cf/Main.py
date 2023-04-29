import bisect
N = int(input())
S = input()

o = []
x = []
for i in range(N):
    if S[i] == "o":
        o.append(i)
    else:
        x.append(i)

if len(o) == 0 or len(x) == 0:
    print(0)
    exit()

ans = 0
leng_o = len(o)
leng_x = len(x)
for i in range(N):
    if S[i] == "o":
        ind = bisect.bisect_right(x, i)
        #print(ind)
        if ind <= leng_x - 1:
            ans += (N - x[ind])
    else:
        ind = bisect.bisect_right(o, i)
        #print(ind)
        if ind <= leng_o - 1:
            ans += (N - o[ind])

print(ans)

