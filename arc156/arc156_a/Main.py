T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    flag = False
    # 累積和　0 1
    s = [[0,0]]
    for i in range(1, N+1):
        if S[i-1] == "0":
            s.append([s[i-1][0] + 1, s[i-1][1]])
        if S[i-1] == "1":
            s.append([s[i-1][0], s[i-1][1] + 1])
        if i < N:
            if S[i-1] == "1" and S[i] == "1":
                flag = True
            
    #print(s)
    if s[-1][1] % 2 == 1:
        print(-1)
        
    else:
        if s[-1][1] == 2:
            if flag:
                if N >= 5:
                    print(2)
                elif N == 4:
                    if S[0] == "1" or S[-1] == "1":
                        print(2)
                    else:
                        print(3)
                else:
                    print(-1)
            else:
                print(1)
        else:
            print(s[-1][1] // 2)