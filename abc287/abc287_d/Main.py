# len(S) > len(T)
S = input() 
T = input()

mae = 0
usiro = 0
leng = len(T)

for i in range(leng):
    if S[i] == T[i] or S[i] == "?" or T[i] == "?":
        mae += 1
    else:
        break

for i in range(leng):
    if S[-1-i] == T[-1-i] or S[-1-i] == "?" or T[-1-i] == "?":
        usiro += 1
    else:
        break

for i in range(leng+1):
    if i <= mae and leng - i <= usiro:
        print("Yes")
    else:
        print("No")