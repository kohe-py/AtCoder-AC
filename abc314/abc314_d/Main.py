N = int(input())
S = list(input())
Q = int(input())

flag = [[False, -1] for _ in range(N)]

a = {"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"}
b = {"a", "b", "c", "d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
for i in range(N):
    if S[i] in a:
        flag[i][0] = True


flag_syou_to_dai = -1
flag_dai_to_syou = -1

for i in range(Q):
    t, x, c = map(str, input().split())
    t, x = int(t), int(x)
    if t == 1:
        if c in a:
            flag[x - 1][0] = True
        else:
            flag[x - 1][0] = False
        flag[x - 1][1] = i
        S[x - 1] = c
    elif t == 2:
        flag_dai_to_syou = i
    else:
        flag_syou_to_dai = i

if flag_dai_to_syou == -1 and flag_syou_to_dai == -1:
    print("".join(S))
    exit()
if flag_dai_to_syou < flag_syou_to_dai:
    for i in range(N):
        if flag[i][0] == False and flag[i][1] > flag_syou_to_dai:
            continue
        if ord(S[i]) > 91:
            S[i] = chr(ord(S[i]) - 32)

else:
    for i in range(N):
        if flag[i][0] == True and flag[i][1] > flag_dai_to_syou:
            continue
        if ord(S[i]) < 91:
            S[i] = chr(ord(S[i]) + 32)

print("".join(S))