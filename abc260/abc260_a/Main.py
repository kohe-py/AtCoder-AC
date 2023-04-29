S = input()
for i in range(len(S)):
    if S.count(S[i]) == 1:
        print(S[i])
        exit()
print(-1)