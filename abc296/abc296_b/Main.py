S = [input() for _ in range(8)]
b = ["a", "b", "c", "d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for i in range(8):
    for j in range(8):
        if S[i][j] == "*":
            x = i
            y = j
            break
ans = ""
ans += b[y]
ans += str(8-x)
print(ans)