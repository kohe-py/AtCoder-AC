N, M = map(int, input().split())

ans = 0
# まずSをそのまま使う
if M // 2 >= N:
    ans += N
else:
    exit(print(M // 2))
M -= ans * 2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             

# cからSをつくる
ans += (M // 4)
print(ans)