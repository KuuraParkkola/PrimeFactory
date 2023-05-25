from math import gcd


def run_algorithm(n, o, c) -> int:
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

def pollard_rho_factor(n):
    c = 0
    factor = None
    while factor is None:
        c += 1
        factor = run_algorithm(n, 2, c)
    return factor
