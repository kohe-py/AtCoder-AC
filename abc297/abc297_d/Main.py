A, B = map(int, input().split())

count = 0
while A != B:
    #print(A, B)
    if A == 1 or B == 1:
        count += abs(A - B)
        break

    elif A < B:
        if A != 0:
            x = (B // A)
            if B % A != 0 and x > 2:
                count += x
                B = B - A * x
            else:
                B = B - A
                count += 1
        else:
            break

    else:
        if B != 0:
            y = (A // B)
            if A % B != 0 and y > 2:
                count += y
                A = A - B * y
            else:
                A = A - B
                count += 1
        else:
            break
print(count)