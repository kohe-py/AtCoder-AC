N = int(input())
s = [input() for _ in range(N)]

#N = 1000 N*N

for i in range(N):
    for j in range(N):
        for k in range(4):
            white = 2
            count = 0
            for l in range(6):   
                if k == 0:
                    K = [l, l]
                elif k == 1:
                    K = [l, 0]
                elif k == 2:
                    K = [0, l]
                else:
                    K = [-l, l]
                    
                if (i+K[0] >= N or j+K[1] >= N) or (i+K[0] < 0 or j+K[1] < 0):
                    break
                elif s[i + K[0]][j + K[1]] == ".":
                    white -= 1
                count += 1
            if white >= 0 and count == 6:
                print("Yes")
                exit()

print("No")