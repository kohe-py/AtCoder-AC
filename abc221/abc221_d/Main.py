N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

due = []
for i in range(N):
    due.append((AB[i][0], 1))
    due.append((AB[i][0] + AB[i][1], -1))

due.sort(key=lambda x: x[0])
ans = [0] * (N + 1)
count = 0
for i in range(N * 2 - 1):
    count += due[i][1]
    ans[count] += due[i + 1][0] - due[i][0]

print(*ans[1:])