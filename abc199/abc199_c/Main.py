N = int(input())
S = list(input())
front = S[:N]
back = S[N:]
Q = int(input())
#print(front)
#print(back)
for _ in range(Q):
    t, a, b = map(int, input().split())
    if t == 1:
        #Sのa文字目とb文字目を入れ替える
        if a <= N and b <= N:
            front[a-1], front[b-1] = front[b-1], front[a-1]
        elif a <= N and b > N:
            b -= N
            front[a-1], back[b-1] = back[b-1], front[a-1]
        else:
            a -= N
            b -= N
            back[a-1], back[b-1] = back[b-1], back[a-1]
    else:
        #Sの前半N文字と後半N文字を入れ替える
        front, back = back, front
        
ans = front + back
print("".join(ans))