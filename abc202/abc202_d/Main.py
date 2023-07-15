A, B, K = map(int, input().split())

leng = A + B
from collections import defaultdict
import math

ans = ""
now = 0
decided_cnt = defaultdict(int)
for i in range(leng): # i桁目を見る
    for one, two in [(1, 0), (0, 1)]: # i桁目が1と2の時
        if decided_cnt[1] >= A and one == 1:
            continue
        if decided_cnt[2] >= B and two == 1:
            continue
        
        now += math.factorial(A + B - 1 - decided_cnt[1] - decided_cnt[2])//(math.factorial(A - one - decided_cnt[1]) * math.factorial(B - two - decided_cnt[2]))
        if K <= now:
            now -= math.factorial(A + B - 1 - decided_cnt[1] - decided_cnt[2])//(math.factorial(A - one - decided_cnt[1]) * math.factorial(B - two - decided_cnt[2]))
            if one == 1:
                decided_cnt[1] += 1
                ans += "a"
            else:
                decided_cnt[2] += 1
                ans += "b"
            break

print(ans)