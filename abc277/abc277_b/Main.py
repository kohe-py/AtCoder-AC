N = int(input())
moji1 = ["H","D", "C","S"]
moji2 = ["A", "2","3","4","5","6","7", "8", "9", "T","J","Q","K"]
result =[]
for i in range(N):
    s =input()
    if s[0] in moji1 and s[1] in moji2 and s not in result:
        pass
    else:
        print("No")
        exit()
    result.append(s)
print("Yes")