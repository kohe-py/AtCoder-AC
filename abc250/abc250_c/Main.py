N, Q = map(int, input().split())

nlist = list(range(1,N+1))
dic = {}
for i in range(N):
    dic[i+1] = i
#print(nlist)
#print(dic)
for i in range(Q):
    x = int(input())
    if dic[x] == N-1:
        dic[x] = N-2
        dic[nlist[N-2]] = N-1
        nlist[-1], nlist[N-2] = nlist[N-2], nlist[-1]
    else:
        nlist[dic[x]],nlist[dic[x] + 1] = nlist[dic[x] + 1], nlist[dic[x]]
        #print(nlist[dic[x]])
        dic[nlist[dic[x]]] -= 1
        dic[nlist[dic[x] + 1]] += 1
    #print(*nlist)
    #print(dic)
    #print("----------------------------")
print(*nlist)