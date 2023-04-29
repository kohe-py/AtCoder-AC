S = input()
b = {"a", "b", "c", "d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
hako = []
hozonj = []
hozoni = []
for i in range(len(S)):
    if S[i] in b:
        if hako.count(S[i])==0:
            hako.append(S[i])
            #print(hako)
        else:
            print("No")
            exit()
            
    elif S[i] == "(":
        hozonj.append(i)
        
    elif S[i] == ")":
        hozoni.append(i)
        
        m = len(hozoni)
        j = hozonj[-m]
        
        for x in range(i, j, -1):
            if S[x] in b and len(hako)>0:
                p = hako.pop()
            if len(hako)==0:
                break
                #print("pop",p)
print("Yes")