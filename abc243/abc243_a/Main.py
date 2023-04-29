V,A,B,C = map(int, input().split())
l = ["F","M","T"]
i = 0
while True:
    if i % 3 == 0:
        V -= A
    elif i % 3 == 1:
        V -= B
    elif i % 3 == 2:
        V -= C
    
    if V < 0:
        break
    i+=1
print(l[i%3])