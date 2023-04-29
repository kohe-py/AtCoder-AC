A, B = map(int, input().split())

def GCD(A, B):
    if B == 0:
        return A
    r = A % B
    return GCD(B, r)

LCM = A*B//GCD(A, B)
if LCM > 10**18:
    print("Large")
else:
    print(LCM)