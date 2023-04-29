import numpy as np

v = [list(map(int, input().split())) for _ in range(4)]
V = []
for i in range(4):
    x = np.array(v[(i-1)%4])
    y = np.array(v[i])
    z = np.array(v[(i+1)%4])
    vec_1 = y - x
    vec_2 = z - x
    if (vec_1[0]*vec_2[1] - vec_1[1]*vec_2[0]) < 1:
        print("No")
        exit()
print("Yes")