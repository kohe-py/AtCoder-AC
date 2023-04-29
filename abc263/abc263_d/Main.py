N, L, R = map(int, input().split())
A = list(map(int, input().split()))

cnt = [0]
for i in range(1, N+1):
    cnt.append(cnt[i-1] + A[i-1])

cnt_min_x = [0]
for i in range(1, N+1):
    cnt_min_x.append(min(cnt_min_x[-1], L*i - cnt[i]))

cnt_min_y = [cnt[N]]
for i in range(1, N+1):
    cnt_min_y.append(min(cnt_min_y[i-1], cnt[N - i] + i*R))

ans = cnt[-1]
for i in range(N+1):
    ans = min(ans, cnt_min_x[i] + cnt_min_y[N-i])

print(ans)