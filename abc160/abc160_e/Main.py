from collections import deque
X, Y, A, B, C = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p = sorted(p, reverse=True)
q = sorted(q, reverse=True)
r = sorted(r, reverse=True)

rr = [0]
for i in range(C):
    rr.append(rr[-1] + r[i])

pq = [0]
x, y = 0, 0
for i in range(A + B):
    if y <= Y - 1 and x <= X - 1:
        if p[x] > q[y]:
            pq.append(pq[-1] + p[x])
            x += 1
        else:
            pq.append(pq[-1] + q[y])
            y += 1
        continue
    elif y <= Y - 1:
        pq.append(pq[-1] + q[y])
        y += 1
        continue
    elif x <= X - 1:
        pq.append(pq[-1] + p[x])
        x += 1
        continue
    else:
        break

ans = -1
for i in range(C + 1):
    ans = max(ans, rr[i] + pq[X + Y - i])
    if i >= X + Y:
        break
print(ans)