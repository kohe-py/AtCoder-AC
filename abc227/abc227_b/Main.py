N = int(input())
S = list(map(int, input().split()))

result = set()
for i in range(N):
    for a in range(1,1001):
        if i in result :
            break
        for b in range(1,1001):
            if S[i] == 4*a*b + 3*a + 3*b:
                result.add(i)
                break
ans = 0              
for i in range(N):
    if i not in result:
        ans += 1
        
#print(result)
print(ans)