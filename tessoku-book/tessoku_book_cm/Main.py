N,K = map(int, input().split())
A = list(map(int, input().split()))


c = set()
for bit in range(2**(N//2)):
    s = 0
    for i in range(N//2):
        if bit >> i & 1 == 1:
            s += A[i]
    c.add(s)

d = set()
for bit in range(2**(N-N//2)):
    s = 0
    #print(bin(bit))
    for i in range(N-N//2):
        if bit >> i & 1 == 1:
            s += A[i + N//2]
    d.add(s)
count=0
for i in c:
    X = K - i
    if X in d:
        count += 1

if count == 0:
    print("No")
else:
    print("Yes")