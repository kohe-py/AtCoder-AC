N, K = map(int, input().split())
S = input()

ans = []
for i in range(N):
    if K > 0 and S[i] == "o":
        ans.append("o")
        K -= 1
    else:
        ans.append("x")
    
print("".join(ans))