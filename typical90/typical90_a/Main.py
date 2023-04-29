N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

B = [A[0]]
for i in range(1, N):
    B.append(A[i] - A[i-1])
B.append(L - A[-1])

left = 0
right = L

while right - left > 1:
    center = left + (right - left) // 2 # これが答えになる
    count = 0 
    min_ = L
    now = 0 #　羊羹の長さ　二分探索のcenterを超えるまで長くする
    for i in range(N + 1):
        now += B[i]
        if now >= center and count < K: # centerを超えたので切る　
            min_ = min(min_, now)
            now = 0
            count += 1

    min_ = min(min_, now)
    
    if min_ >= center:
        left = center # もっと長くできる  等号成立のときも長くできる（centerが小さいくて羊羹的に取りうる値なら等号成立する）
    else:
        right = center # すべての羊羹をcenterにするには羊羹が小さすぎた...

print(left)
