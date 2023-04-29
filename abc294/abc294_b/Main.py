H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

a = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
ans = []
b = dict()
for i in range(len(a)):
    b[i+1] = a[i]

for i in range(H):
    result = []
    for j in range(W):
        if A[i][j] == 0:
            result.append(".")
        else:
            for k in range(len(a)):
                if A[i][j] == k+1:
                    result.append(str(a[k]))
    ans.append(result)
for i in range(H):
    print("".join(ans[i]))