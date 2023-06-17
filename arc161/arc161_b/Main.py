T = int(input())

## 10^18 は2進数表記で 60桁
from collections import deque

for _ in range(T):
    N = int(input())
    if N <= 6:
        print(-1)
        continue
    s = deque(bin(N))
    s.popleft()
    s.popleft()
    count = s.count("1")
    if count == 1:
        s[0] = "0"
        for i in range(1, 4):
            s[i] = "1"
    elif count == 2:
        ind = []
        for i in range(len(s)):
            if s[-i-1] == "1":
                ind.append(i)
            if len(ind) == 2:
                break
        if ind[0] >= 2:
            s[-ind[0]-1] = "0"
            s[-ind[0]] = "1"
            s[-ind[0] + 1] = "1"
        else:
            s = ["1"] * 3 + [0] * (len(s) - 4)
    
    elif count == 3:
        pass

    else:
        for i in range(N):
            if s[-i-1] == "1":
                s[-i-1] = "0"
                count -= 1
            if count == 3:
                break
    
    ans = 0
    for i in range(len(s)):
        if s[-i-1] == "1":
            ans += (2 ** i)
    print(ans)