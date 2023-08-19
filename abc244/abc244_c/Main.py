N = int(input())
visit = set(list(range(1, 2 * N + 2)))
for _ in range(2 * N + 1):
    for s in visit:
        print(s)
        break
    visit.discard(s)
    visit.discard(int(input()))