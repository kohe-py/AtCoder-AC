S = input()
T = input()

ans = len(T)
for i in range(len(S)):
    x = 0
    for j in range(len(T)):
        if i+j > len(S) - 1:
            x = len(T)
            break
        if S[i+j] != T[j]:
            x += 1
    #print(x)
    ans = min(ans, x)
print(ans)