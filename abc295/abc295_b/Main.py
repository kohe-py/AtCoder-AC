R, C = map(int, input().split())
B = [input() for _ in range(R)]
#print(B)
c = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
s = set()
for i in range(R):
    for j in range(C):
        if B[i][j] in c:
            x = int(B[i][j])
            for k in range(R):
                for l in range(C):
                    if abs(i - k) + abs(j - l) <= x:
                        s.add((k, l))

for i in range(R):
    B[i] = list(B[i])
    for j in range(C):
        if (i, j) in s:
            B[i][j] = "."

for i in range(R):
    print("".join(B[i]))