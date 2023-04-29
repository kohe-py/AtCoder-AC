S = input()

N = len(S)
h = []
ans = 0

for bit in range(1 << 2*N-1):
    c = 0
    for j in range(0,2*N+1,2):
        if bit & (1 << j):
            c += 1
        else:
            break
    if c == N:
        h.append(bit)
        
        
for bit in h:
    f = []
    for i in range(1,2*N-1,2):
        if bit & (1 << i):
            f.append(1)    
        else:
            f.append(0)

    
    num = S[0]
    for i in range(N-1):
        if f[i] == 1:
            ans += int(num)
            num = S[i+1]
        else:
            num += S[i+1]

    if num != "":
        ans += int(num)

        
print(ans) 