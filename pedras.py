# (sem cache)
def vence_puro(n: int) -> bool:
    if n == 0:
        return False

    for i in [1, 2, 3]:
        if n - i >= 0:
            if not vence_puro(n - i):  
                return True

    return False


# (com cache)
from functools import lru_cache

@lru_cache(maxsize=None)
def vence(n: int) -> bool:
    if n == 0:
        return False

    for i in [1, 2, 3]:
        if n - i >= 0:
            if not vence(n - i):
                return True

    return False