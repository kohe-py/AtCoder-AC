N, K= map(int, input().split())
a = list(map(int, input().split()))


nlist = [False] * (N + 1)
for i in range(N + 1):
    for j in range(K):
        if i >= a[j] and nlist[i - a[j]] == False:
            nlist[i] = True
        
#print(nlist)
if nlist[N] == True:
    print("First")
else:
    print("Second")