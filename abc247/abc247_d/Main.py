from collections import deque
Q = int(input())
S = deque()
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        S.append([q[1], q[2]])
    else:
        x = q[1]
        ans = 0
        #print(S)
        while True:
            #print(ans)
            s = S.popleft()
            if s[1] > x:
                ans += s[0]*x
                s[1] -= x
                S.appendleft(s)
                break
            elif s[1] == x:
                ans += s[0]*x
                break
            
            else:
                ans += s[0]*s[1]
                x -= s[1]
        print(ans)