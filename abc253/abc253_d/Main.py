import math
N, A, B = map(int, input().split())

s = N * (N+1) // 2
x = N // A
y = N // B
w = A*B // math.gcd(A,B)
z = N // w
# 2(a1+an)/n  等差数列の和
s_x = x * (A + x*A) // 2
s_y = y * (B + y*B) // 2
if z != 0:
    s_z = z * (w + z*w) // 2
    print(s + s_z - s_x - s_y)
else:
    print(s - s_x - s_y)