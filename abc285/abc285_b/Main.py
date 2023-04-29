N = int(input())
S = input()

for i in range(1, N):
    ans = []
    for l in range(N-i):
        if S[l+i] != S[l]:
            ans.append(l+1)
        else:
            break
    
    #print(ans)
    if len(ans) == 0:
        print(0)
    else:
      print(ans[-1])