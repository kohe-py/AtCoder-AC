A,B,C,D,E,F = map(int, input().split())
x =  998244353 
y = (A*B*C-D*E*F)%x
print(y)