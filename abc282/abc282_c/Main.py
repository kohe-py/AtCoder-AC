N = int(input())
S = input()

result = []
flag = 0
for i in range(N):
    if S[i] == '"':
        result.append(S[i])
        flag += 1
    elif S[i] == ',':
        if flag % 2 == 0:
            result.append(".")
        else:
            result.append(",")

    else:
        result.append(S[i])
print("".join(result))