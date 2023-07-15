from functools import lru_cache

@lru_cache(maxsize=1000)
def main(n):
    if n <= 1:
        return 100
    if n == 2:
        return 200
    return main(n - 1) + main(n - 2) + main(n - 3)

print(main(19))