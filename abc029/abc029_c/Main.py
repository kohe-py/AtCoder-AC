N = int(input())

import itertools
result = itertools.product("abc", repeat = N)
for i in (result):
    print("".join(i))