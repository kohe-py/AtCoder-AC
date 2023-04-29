N, X, Y = map(int, input().split())

def red1(n):
    cnt = red[n]
    red[n] = 0
    red[n-1] += cnt
    blue[n] += cnt * X
    
def blue1(n):
    cnt = blue[n]
    blue[n-1] += cnt * Y
    red[n-1] += cnt

red = [0 for _ in range(N+1)]
blue = [0 for _ in range(N+1)]
red[N] = 1

for i in range(N, 1, -1):
    red1(i)
    blue1(i)
print(blue[1])