N = int(input())

ans = ""
while N != 0:
    if N % 2 == 0:
        ans = "0" + ans
    elif N % 2 == 1:
        ans = "1" + ans
    N = N // 2
    
print("{:0>10}".format(ans))