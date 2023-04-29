import math
a, b,x = list(map(int,input().split()))
if a*a*b/2 <= x:
  print(math.atan((b*2-x*2/a/a)/a)/math.pi*180)
else:
  print(math.atan(b/x*a*b/2)/math.pi*180)