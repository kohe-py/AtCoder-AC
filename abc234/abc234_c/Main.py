K = int(input())
b = bin(K)[2:]
ans = ""
for i in range(len(b)):
    if b[i] == "1":
        ans += "2"
    else:
        ans += "0"
print(int(ans))