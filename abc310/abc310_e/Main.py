N = int(input())
S = input()

zero, one = 0, 0
ans = 0

for i in range(N):
    if S[i] == "0":
        zero, one = 1, zero + one
    else:
        zero, one = one, zero + 1
    ans += one
    #print(zero, one, ans)

print(ans)