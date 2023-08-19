N, M = map(int, input().split())
S = [input() for _ in range(N)]

d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
ans = set()
result = set()
result.add((1, 1))
ans.add((1, 1))
todo = []
todo.append((1, 1))
while todo:
    y, x = todo.pop()
    for i, j in d:
        if S[y + i][x + j] == "#":
            continue
        flag = 1
        while True:
            if S[y + i * flag][x + j * flag] == "#":
                if (y + i * (flag - 1), x + j * (flag - 1)) not in result:
                    result.add((y + i * (flag - 1), x + j * (flag - 1)))
                    todo.append((y + i * (flag - 1), x + j * (flag - 1)))
                break
            ans.add((y + i * flag, x + j * flag))
            flag += 1
print(len(ans))