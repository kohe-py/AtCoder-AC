x1, y1, x2, y2 = map(int, input().split())

dxy = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
xy = [(2, 1), (1, 2)]

visit = set()
for dx, dy in dxy:
    for x, y in xy:
        visit.add((x1 + (x * dx), y1 + (y * dy)))

for dx, dy in dxy:
    for x, y in xy:
        if (x2 + (x * dx), y2 + (y * dy)) in visit:
            exit(print("Yes"))
print("No")