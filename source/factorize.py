from time import time
from typing import Callable, Any
from source.algorithms.fermat_primality import fermat_primality
from source.algorithms.pollard_rho_factor import pollard_rho_factor


def factorize(n: int, is_composite: bool = False, on_match: Callable[[int], None] = None) -> dict[int: dict[str: Any]]:
    ##
    #   Find all primenumber factors
    #
    # Create containers for holding intermediate factors
    # and the final prime factors
    factors = set()
    stack = [n]
    
    # Algorithm starts
    start_time = time()

    # Prerun algorithm once for guaranteed composite numbers
    # to improve performance
    if is_composite:
        num = stack.pop()
        factor = pollard_rho_factor(num)
        stack.append(factor)
        stack.append(num // factor)

    # While there are intermediary factors in the stack, find factors
    while len(stack):
        # Pick a number from the stack
        num = stack.pop()

        # The Pollard Rho implementation seems to break on 4,
        # this workaround temporarily fixes the problem
        if num == 4:
            if 2 not in factors and on_match is not None:
                on_match(2)
                factors.add(2)
            continue

        # If the number is a prime, mark it as a prime factor
        if fermat_primality(num, 120):
            if num not in factors and on_match is not None:
                on_match(num)
            factors.add(num)
            continue
        
        # Run the Pollard Rho algorithm
        factor = pollard_rho_factor(num)

        # Add the found factors to intermediary factors for
        # the next round of checks
        stack.append(factor)
        stack.append(num // factor)

    # Algorithm has finished
    runtime = time() - start_time

    return { 'factors': tuple(factors), 'runtime': runtime }
