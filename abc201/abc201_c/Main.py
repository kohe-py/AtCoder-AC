import itertools
S = input()
N = S.count("o")
o = []
h = []
x = []
for i in range(len(S)):
    if S[i] == "o":
        o.append(str(i))
    elif S[i] == "?":
        h.append(str(i))
    else:
        x.append(str(i))

x = set(x)
ans = 0
for i in range(0, 10000):
    i = str(i).zfill(4)
    oo = set(o)
    Flag = True
    for j in range(4):
        #print(i[j])
        if i[j] in x:
            Flag = False
            break
        elif i[j] in oo:
            oo.discard(i[j])
            #print(oo)
    if len(oo) == 0 and Flag:
        ans += 1
print(ans)