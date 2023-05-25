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

def pollard_rho_factor(n, o, c) -> int:
    def iterate(x: int) -> int:
        return x**2 + c % n

    S = o
    F = o
    factor = 1

    while factor == 1:
        S = iterate(S)
        F = iterate(iterate(F))
        factor = gcd(S-F, n)

    return None if factor == n else factor

def find_factor(n):
    c = 0
    factor = None
    while factor is None:
        c += 1
        factor = pollard_rho_factor(n, 2, c)
    return factor

def factorize(n: int) -> set[int]:
    factors = set()
    stack = [n]
    
    while len(stack):
        num = stack.pop()
        if fermat_primality(num, 60):
            factors.add(num)
            continue

        factor = find_factor(num)
        print(factor, num // factor)
        stack.append(factor)
        stack.append(num // factor)

    return factors    

if __name__ == '__main__':
    n = 26541
    print(factorize(n))
