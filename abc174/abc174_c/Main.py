K = int(input())

tmp = 7
ans = [10 ** 8] * (K + 1)
for i in range(10 ** 6 + 1):
    tmp %= K
    ans[tmp] = min(ans[tmp], i + 1)
    tmp *= 10
    tmp += 7

if ans[0] == 10 ** 8:
    print(-1)
else:
    print(ans[0])