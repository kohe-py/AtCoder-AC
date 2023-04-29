N = int(input())
result = [0] * (N)
result[0] = 1
result[1] = 1
for i in range(2, N):
    result[i] = (result[i-1]+result[i-2])%1000000007
print(result[-1]%(10**9 + 7))