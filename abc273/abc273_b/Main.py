X,K=map(int, input().split())
for i in range(K):
    x = str(X)
    x = x.zfill(K+1)
    if int(x[-1-i]) >= 5:
        X=(int(x[:-i-1])+1) * 10 ** (i+1)
    elif int(x[-1-i]) < 5:
        X=int(x[:-i-1]) * 10 ** (i+1)

print(X)