N = int(input())
A = [input() for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i != j:
            if A[i][j] == "L" and A[j][i] =="W":
                pass
            elif A[i][j] == "W" and A[j][i] =="L":
                pass
            elif A[i][j] == "D" and A[j][i] == "D":
                pass
            else:
                print("incorrect")
                exit()

print("correct")