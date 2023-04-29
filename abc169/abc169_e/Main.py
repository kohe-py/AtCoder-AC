N = int(input())
ans = 0
a = []
b = []
for _ in range(N):
    A, B = map(int, input().split())
    a.append(A)
    b.append(B)

    # 中央値自体は O(1) で出せる
    # 区間を変えてなんやかんやする？
    # 中央の２文字ないし１文字を決める？

a.sort()
b.sort()

#中央の値の範囲を出したい
# 奇数　偶数で場合分け
if N % 2 == 1:
    m, M = a[N // 2], b[N // 2]
    print(M - m + 1)

else:
    # 偶数の時　奇数の時より２倍くらいになりそう
    # サンプル１　中央値　1.5 2 2.5
    # m = 1.5 M = 2.5
    m = (a[N//2 - 1] + a[N//2]) / 2
    M = (b[N//2 - 1] + b[N//2]) / 2
    print(int((M - m + 0.5) * 2))