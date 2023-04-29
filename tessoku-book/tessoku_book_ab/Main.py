N = int(input())
ta = [list(map(str, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    if ta[i][0] == "+":
        ans += int(ta[i][1])
    elif ta[i][0] == "-":
        ans -= int(ta[i][1])
    else:
        ans *= int(ta[i][1])
    ans %= 10000
    print(ans)