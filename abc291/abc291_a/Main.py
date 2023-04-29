S = input()
a = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
a = set(a)
for i in range(len(S)):
    if S[i] in a:
        print(i+1)
        break