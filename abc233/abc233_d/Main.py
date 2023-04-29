from collections import defaultdict
N, K = map(int, input().split())
A = list(map(int, input().split()))


B = [0]
for i in range(1, N+1):
    B.append(B[i-1] + A[i-1])
    
dic = defaultdict(int)  
ans = 0

for i in range(N+1):
    l = B[i] - K
    ans += dic[l]
    dic[B[i]] += 1 
print(ans)