X, Y = map(int, input().split())
count = 1
while X*2 <= Y:
    X *= 2
    #print(X)
    count += 1
print(count)