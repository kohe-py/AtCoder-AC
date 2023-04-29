S = input()
if S[0] == "1":
    print("No")
    exit()
s = [[S[6]], [S[3]], [S[1], S[7]],[S[0],S[4]],[S[2], S[8]], [S[5]], [S[9]]]
for i in range(7):
    if s[i].count("1") >= 1:
        s[i] = 1
    else:
        s[i] = 0
#print(s)
a,b, c = -1,-1,-1
for i in range(7):
    if c == -1:
        if s[i] == 1:
            a = i
            c = i
    else:
        if s[i] == 1:
            c=i
        if s[i] == 0:
            b=i
        if a < b < c:
            print("Yes")
            exit()
print("No")