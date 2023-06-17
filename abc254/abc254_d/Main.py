N = int(input())
a = []
for i in range(N + 1):
    a.append(i)

for i in range(2, N + 1):
    for j in range(i ** 2, N + 1, i ** 2):
        tmp = i ** 2
        while a[j] % tmp == 0:
            a[j] //= tmp

count = [0] * (N + 1)

for i in a:
    count[i] += 1

ans = 0
for i in range(1, N + 1):
    ans += count[i] ** 2

print(ans)