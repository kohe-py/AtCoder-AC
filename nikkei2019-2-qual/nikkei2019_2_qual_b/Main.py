N = int(input())
D = list(map(int, input().split()))

count = [0] * (N)
for i in range(N):
    count[D[i]] += 1

if D[0] != 0 or count[0] != 1:
    print(0)
    exit()

ans = 1
for i in range(N - 1):
    ans *= count[i] ** count[i + 1]
    ans %= 998244353
#print(count)
print(ans)