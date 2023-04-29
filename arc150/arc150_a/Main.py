T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    S = input()
    
    #前計算 累積和 0 ? 1
    s = [[0,0,0]]
    for i in range(1, N+1):
        if S[i-1] == "0":
            s.append([s[i-1][0] + 1, s[i-1][1], s[i-1][2]])
        elif S[i-1] == "?":
            s.append([s[i-1][0], s[i-1][1] + 1, s[i-1][2]])
        else:
            s.append([s[i-1][0], s[i-1][1], s[i-1][2] + 1])
    #print(s)
    
    result = s[-1][2]
    count = 0
    for i in range(N-K+1):
        question = s[i+K][1] - s[i][1]
        zero = s[i+K][0] - s[i][0]
        one = s[i+K][2] - s[i][2]
        #print(question, zero, one)
        if one == result and zero == 0:
            count += 1
    if count == 1:
        print("Yes")
    else:
        print("No")