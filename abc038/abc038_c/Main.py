N = int(input())
a = list(map(int, input().split()))

ans = N
count = 0
for i in range(N - 1):
    if a[i] < a[i+1]:
        count += 1
    else:
        ans += count * (count + 1) // 2
        count = 0

print(ans + count * (count + 1) // 2)