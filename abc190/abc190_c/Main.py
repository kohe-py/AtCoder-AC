N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
cd = [list(map(int, input().split())) for _ in range(K)]

ans = 0
for bit in range(2 ** K):
    s = set()
    result = 0
    #print(bin(bit))
    for i in range(K):
        if ((bit >> i) & 1):
            s.add(cd[i][1])
        else:
            s.add(cd[i][0])
    
    for j in range(M):
        if ab[j][0] in s and ab[j][1] in s:
            result += 1
    #print(s, result, ans)
    ans = max(ans, result)
    
print(ans)