from math import gcd


def run_algorithm(n, o, c) -> int:
    def iterate(x: int) -> int:
        return x**2 + c % n

    S = o
    F = o
    factor = 1

    while factor == 1:
        # Iterate the algorithm once for the fast and slow numbers
        S = iterate(S)
        F = iterate(iterate(F))

        # Check the result of this iteration
        factor = gcd(S-F, n)

    # If the found factor is equal to n, no factors were found
    # otherwise the algorithm found a factor
    return None if factor == n else factor

def pollard_rho_factor(n):
    ##
    #   Run the Pollard Rho algorithm to find one factor of n
    #   if the algorithm fails, try again with a different
    #   iteration function.
    #
    c = 0
    factor = None
    while factor is None:
        c += 1
        factor = run_algorithm(n, 2, c)
    return factor
