H, W = map(int, input().split())

w = W // 2
h = H // 2

if W % 2 == 1:
    w += 1
if H % 2 == 1:
    h += 1
    
if W == 1 or H == 1:
    print(W*H)
else:
    print(w*h)