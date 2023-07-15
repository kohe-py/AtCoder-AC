N = int(input())
A = list(map(int, input().split()))

ans = []
count = 0
result = 0
for i in range(7 * N):
    result += A[i]
    count += 1
    if count == 7:
        ans.append(result)
        result = 0
        count = 0
print(*ans)

    
