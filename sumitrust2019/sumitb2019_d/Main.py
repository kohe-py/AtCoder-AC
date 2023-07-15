N = int(input())
S = input()

ans = 0
for i in range(1000):
    pas = f"{i:03}"
    ind = 0
    #print(pas)
    for j in range(N):
        if pas[ind] == S[j]:
            ind += 1
        if ind >= 3:
            ans += 1
            break
print(ans)