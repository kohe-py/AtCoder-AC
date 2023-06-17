import bisect

N = int(input())
A = list(map(int, input().split()))

# 累積和
B = [0]
for i in range(1, N - 1, 2):
    B.append(B[-1] + A[i + 1] - A[i])
#print(B)  

Q = int(input())
for _ in range(Q):
    ans = 0
    l, r = map(int, input().split())
    indl = bisect.bisect_left(A, l)
    indr = bisect.bisect_left(A, r)
    #print(indl, indr)
    if indr % 2 == 0 and indr != 0:
        ans += B[indr // 2]
        ans -= (A[indr] - r)
        #print(ans, A[indr], r)
    if indl % 2 == 0 and indl != 0:
        ans -= (l - A[indl - 1])
        ans -= B[indl // 2 - 1]
    if indr % 2 == 1:
        ans += B[indr // 2]
    if indl % 2 == 1:
        ans -= B[indl // 2]
        pass
    if indr == indl and indr % 2 == 0 and indr != 0:
        ans = (r - l)
    if indr == indl and indr % 2 == 1:
        ans = 0
    if indr == 0:
        ans = 0
    print(ans)