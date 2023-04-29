import math
a,b,d = map(int, input().split())

r = (a**2 + b**2)**(1/2)
if a == 0 and b == 0:
    print(0,0)
    exit()

kakudoa = math.radians(d) + math.atan2(b,a)
kakudob = math.radians(d)+ math.atan2(b,a)
A = r * math.cos(kakudoa)
B = r * math.sin(kakudob)

print(A,B)