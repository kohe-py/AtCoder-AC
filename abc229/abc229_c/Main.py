N, W = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort(reverse=True, key=lambda x: x[0])

ans, w, i = 0, 0, 0
while w < W and i <= N - 1:
    if w + AB[i][1] <= W:
        w += AB[i][1]
        ans += (AB[i][0] * AB[i][1])
    else:
        ans += AB[i][0] * (W - w)
        break
    i += 1
print(ans)