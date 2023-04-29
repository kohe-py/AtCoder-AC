S=input()
T=input()

if S == T:
    print("Yes")
    exit()
if len(S) > len(T):
    print("No")
    exit()

slist = [[S[0], 1]]
count=0
for i in range(len(S)-1):
    if S[i] == S[i+1]:
        slist[count][1] += 1
    else:
        count+=1
        slist.append([S[i+1],1])
#print(slist)

tlist = [[T[0], 1]]
c = 0
for i in range(len(T)-1):
    if T[i] == T[i+1]:
        tlist[c][1] += 1
    else:
        c+=1
        tlist.append([T[i+1],1])
#print(tlist)
        
if len(slist) != len(tlist):
    print("No")
    exit()

count = 0
for i in range(len(slist)):
    if tlist[i][1] == slist[i][1] and tlist[i][0] == slist[i][0]:
        count+=1
    else:
        if tlist[i][0] == slist[i][0] and slist[i][1] >= 2 and tlist[i][1] >= 2 and tlist[i][1] >= slist[i][1]:
            count+=1

if count == len(slist):
    print("Yes")
else:
    print("No")