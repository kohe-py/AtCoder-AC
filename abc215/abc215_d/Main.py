N, M = map(int, input().split())
A = list(map(int, input().split()))
Max = max(max(A), M)

k = [True] * (Max+1)
k[0] = False
is_prime = [True] * (Max+1)
prime = []

for i in range(N):
    k[A[i]] = False
    
for i in range(2, Max+1):
    if not is_prime[i]:
        continue
    for j in range(i*2, Max+1, i):
        is_prime[j] = False
        k[i] = k[i] and k[j]
    if not k[i]:
        prime.append(i)

for i in prime:
    for j in range(i*2, M+1, i):
        k[j] = k[i] and k[j]

k[1] = True
ans = [1]
for i in range(2, M+1):
    if k[i]:
        ans.append(i)
print(len(ans))
for i in ans:
    print(i)