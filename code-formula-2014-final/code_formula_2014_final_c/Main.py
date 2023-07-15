S = input()

ans = []
flag = False
tmp = ""
for i in range(len(S)):
    if S[i] == "@":
        if flag and tmp != "":
            ans.append(tmp)
        flag = True
        tmp = ""
    elif flag and S[i] == " ":
        flag = False
        if tmp != "":
            ans.append(tmp)
    elif flag:
        tmp += S[i]
    if i == len(S) - 1 and flag and tmp != "":
        ans.append(tmp)

ans = list(set(ans))
ans.sort()
for i in (ans):
    print(i)
