from collections import deque
S = [input() for _ in range(10)]

    
S=deque(S)
S.append("..........")
S.appendleft("..........")

for i in range(12):
    S[i] = "." + S[i] + "."
a, b, c, d = 0,0,0,0
for i in range(1,11):
    for j in range(1,11):
        if S[i].count("#") > 0:
            B = i
            if a == 0:
                A = i
                a += 1
            if S[i][j] == "#":
                D = j
                if c == 0:
                    C = j
                    c += 1

print(A,B)
print(C,D)