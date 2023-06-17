N = int(input())
A = list(map(int, input().split()))

## i < j < k

from collections import deque, defaultdict
count_number = defaultdict(int)
for i in range(N):
    count_number[A[i]] += 1

ans = 0
left = 0
right = N
sort_list = list(sorted(count_number.keys()))

for i in sort_list:
    right -= count_number[i]
    ans += left * right * count_number[i]
    left += count_number[i]     

print(ans)                    
