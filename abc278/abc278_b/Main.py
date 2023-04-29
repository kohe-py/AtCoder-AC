H, M = map(int, input().split())


while H < 24:
    h = str(H)
    if len(h) != 2:
        h = "0" + h
    m = str(M)
    if len(m) != 2:
        m = "0" + m
        
    if 10 * int(h[0]) + int(m[0]) > 23 or 10 * int(h[1]) + int(m[1]) > 59:
        if M <= 58:
            M += 1
        if M > 58:
            M = 0
            H = H + 1
            if H == 24:
                M = 0
                H = 0
            
        
    else:
        print(H, M)
        break