import bisect

N = int(input())
S = input()
W = list(map(int, input().split()))

child_max = 0
adult_min = 10**9
adult = []
child = []
for i in range(N):
    if S[i] == "1":
        adult.append(W[i])
        adult_min = min(adult_min, W[i])
    else:
        child.append(W[i])
        child_max = max(child_max, W[i])

adult.sort()
child.sort()
la = len(adult)
lc = len(child)

leng = min(la, lc)
if child_max < adult_min:
    print(N)
    exit()

if child_max == adult_min:
    x = child.count(child_max)
    y = adult.count(child_max)
    c = min(x, y)
    print(N-c)
    exit()
#print(child)
#print(adult)

ans = 0
for i, v in enumerate(adult):
    ind = bisect.bisect_left(child, v)
    ans = max(ans, ind + la - i)
print(ans)