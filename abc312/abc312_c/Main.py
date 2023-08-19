N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

import bisect


def cheack(center):
    ind = bisect.bisect_left(B, center)
    ind2 = bisect.bisect_right(A, center)
    if ind2 >= M - ind:
        return True
    return False

def binary_search():
    left = 0
    right = 10 ** 9 + 300
    while abs(right - left) > 1:
        center = left + (right - left) // 2
        if cheack(center):
            right = center
        else:
            left = center
    return right

print(binary_search())