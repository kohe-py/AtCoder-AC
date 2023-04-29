S = input()
a = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
A = {}
for i in range(26):
    A[a[i]] = i+1
a = len(S)
if a == 1:
    print(A[S])
    exit()
ans = 0

for i in range(len(S)-1):
    ans += 26 ** (i+1)
#print(ans)
for i in range(len(S)):
    ans += (A[S[i]]-1) * (26 ** (a-i-1))

    #print(ans)
print(ans+1)