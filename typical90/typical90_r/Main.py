import math
import numpy as np
T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())
for _ in range(Q):
    E = int(input())
    wt = 2 * np.pi * E / T
    y = -math.sin(wt) * (L / 2)
    z = L / 2 - (L/2) * math.cos(wt)
    # 観覧車　（0, y, z）
    # ました　(0, y, 0)
    # 直大　　(X, Y, 0)
    dist = math.sqrt((Y - y) ** 2 + (X ** 2) + (z ** 2))
    dist2 = math.sqrt(z)
    ans = math.degrees(math.asin(z/dist))
    print(ans)