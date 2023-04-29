N = int(input())
#長さ10　1~9が一回ずつ
S = [input() for _ in range(N)]

ans = [-1] * 10
for i in range(10):
    visited = set()
    while len(visited) != N:
        ans[i] += 1
        for j in range(N):
            if j not in visited:
                #print("S[j][ans[i]%10]:", S[j][ans[i]%10], i)
                if S[j][ans[i]%10] == str(i):
                    visited.add(j)
                    break
print(min(ans))