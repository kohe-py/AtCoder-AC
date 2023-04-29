N, M = map(int, input().split())


abc = [[] * N for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    abc[a-1].append(b)
    abc[b-1].append(a)


#print(ab)
for i in range(N):
    abc[i].sort()
    print(len(abc[i]), *abc[i])