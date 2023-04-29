N = int(input())
A = list(map(int, input().split()))

# それぞれの動物について考える
# 動物２なら A1 を選ぶ A2 を選ぶ 両方選ぶ の３種類がある
# 行動２をしない選択をした場合行動１は絶対しないといけない

#行動１をする場合
dp = [[10**18] * 2 for _ in range(N)]
dp[0][1] = A[0]
ans = 10**18
for i in range(1, N):
    dp[i][0] = dp[i-1][1]
    dp[i][1] = min(dp[i-1]) + A[i]

# 行動１をしない場合
dp_2 = [[10**18] * 2 for _ in range(N)]
dp_2[0][0] = 0
for i in range(1, N):
    dp_2[i][0] = dp_2[i-1][1]
    dp_2[i][1] = min(dp_2[i-1]) + A[i]

print(min(min(dp[-1]), dp_2[-1][1]))