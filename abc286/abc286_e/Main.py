N = int(input())
A = list(map(int, input().split()))
S = [input() for _ in range(N)]
cost = [[[10 ** 18, -10 ** 18] for _  in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if S[i][j] == "Y":
            cost[i][j] = [1, A[j]]

for center in range(N):
    for left in range(N):
        for right in range(N):
            if cost[left][center][0] + cost[center][right][0] < cost[left][right][0]:
                cost[left][right][0] = cost[left][center][0] + cost[center][right][0]
                cost[left][right][1] = cost[left][center][1] + cost[center][right][1]
            elif cost[left][center][0] + cost[center][right][0] == cost[left][right][0]:
                cost[left][right][0] = cost[left][center][0] + cost[center][right][0]
                cost[left][right][1] = max(cost[left][center][1] + cost[center][right][1], cost[left][right][1])

Q = int(input())

for _ in range(Q):
    u, v = map(int, input().split())
    if cost[u - 1][v - 1][0] == 10 ** 18:
        print("Impossible")
        continue
    print(cost[u - 1][v - 1][0], cost[u - 1][v - 1][1] + A[u - 1])
