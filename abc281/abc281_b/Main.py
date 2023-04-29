import sys
S=input()
a = {"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"}
b = {"1","2","3","4","5","6","7","8","9", "0"}
c = 0
if len(S) != 8:
    print("No")
else:
    if S[0] in a and S[-1] in a:
        for i in range(6):
            if i == 0 and S[i+1] == "0":
                print("No")
                sys.exit()
            elif S[i+1] not in b:
                print("No")
                sys.exit()
        print("Yes")
    else:
        print("No")