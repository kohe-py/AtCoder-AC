N, A, B = map(int, input().split())

nlist = [4] * (N + 1)
for i in range(N + 1):
    if i >= A and nlist[i - A] == False:
        nlist[i] = True
    elif i >= B and nlist[i - B] == False:
        nlist[i] = True
    else:
        nlist[i] = False
#print(nlist)
if nlist[N] == True:
    print("First")
else:
    print("Second")