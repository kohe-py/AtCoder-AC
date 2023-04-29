N = int(input())

from collections import defaultdict
def f_memo(N):
    memo = defaultdict(lambda: -1)
    memo[0] = 1
   
    def f(N):
        if N == 0:
            return 1
        
        if memo[N] != -1:
            return memo[N]
        
        memo[N] = f( N//2 ) + f( N//3 )
        return memo[N]
    
    return f(N)
    
print(f_memo(N))