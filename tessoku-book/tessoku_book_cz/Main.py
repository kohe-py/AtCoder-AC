A,B = map(int, input().split())

def GCD(A, B):
    if B == 0:
        return A
    r = A % B
    return GCD(B, r)

ans = A * B // GCD(A, B)
print(ans)