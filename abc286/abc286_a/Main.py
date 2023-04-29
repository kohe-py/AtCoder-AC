N,P,Q,R,S = map(int, input().split())
A = list(map(int, input().split()))

if P == 1:
    B = A[R-1:S] + A[Q:R-1] + A[P-1:Q] + A[S:N]
else:
    B = A[:P-1] + A[R-1:S] + A[Q:R-1] + A[P-1:Q] + A[S:N]
print(*B)