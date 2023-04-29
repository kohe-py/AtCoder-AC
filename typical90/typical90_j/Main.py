N = int(input())

one = [0] * (N+1)
two = [0] * (N+1)
for i in range(N):
    c, p = map(int, input().split())
    if c == 1:
        one[i+1] = p
    else:
        two[i+1] = p

#累積和
one_sum = [one[0]]
two_sum = [two[0]]
for i in range(1, N+1):
    one_sum.append(one_sum[i-1] + one[i])
    two_sum.append(two_sum[i-1] + two[i])

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    o = one_sum[R] - one_sum[L - 1]
    t = two_sum[R] - two_sum[L - 1]
    print(o)
    print(t)