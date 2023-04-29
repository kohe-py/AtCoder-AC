H, W = map(int, input().split())
R,C = map(int, input().split())

count = 4
if R == 1 or R == H:
    count -= 1
    if H == 1:
        count -= 1
if C == 1 or C == W:
    count -= 1
    if W == 1:
        count -= 1
print(count)