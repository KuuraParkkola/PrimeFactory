from random import randint
from math import gcd

    
def fermat_primality(a: int, rounds: int) -> bool:
    def iteration(a) -> bool:
        t = randint(1, a-1)
        return gcd(a, t) == 1 and t**(a-1) % a == 1
    
    for _ in range(rounds):
        if not iteration(a):
            return False
        
    return True
