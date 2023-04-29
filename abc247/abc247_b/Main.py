from collections import defaultdict
N = int(input())
st = [list(map(str, input().split())) for _ in range(N)]

a = defaultdict(int)
for i in range(N):
    a[st[i][0]] += 1
    a[st[i][1]] += 1
    if st[i][0] == st[i][1]:
        a[st[i][1]] -= 1

for i in range(N):
    if a[st[i][0]] == 1 or a[st[i][1]] == 1:
        pass
    else:
        print("No")
        exit()
        
print("Yes")