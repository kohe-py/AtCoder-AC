A = int(input())
B = int(input())
C = int(input())
X = int(input())
i = 0
for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            if X == 500*a + 100*b + 50*c:
                i += 1
print(i)
            
        