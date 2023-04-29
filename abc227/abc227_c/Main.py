N = int(input())

count=0
Flag = True
for a in range(1, N+1):
    if a**3 > N:
        break
    for b in range(a, N + 1):
        if a*b*b > N:
            break
        if int(N //(a*b)) >= b:
            count += (N //(a*b)) -b + 1
        else:
            break

#print(result)
print(count)