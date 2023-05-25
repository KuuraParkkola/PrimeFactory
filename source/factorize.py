from time import time
from typing import Callable, Any
from source.algorithms.fermat_primality import fermat_primality
from source.algorithms.pollard_rho_factor import pollard_rho_factor


def factorize(n: int, on_match: Callable[[int], None] = None) -> dict[int: dict[str: Any]]:
    factors = set()
    stack = [n]
    
    start_time = time()
    while len(stack):
        num = stack.pop()
        if fermat_primality(num, 60):
            if num not in factors and on_match is not None:
                on_match(num)
            factors.add(num)
            continue

        factor = pollard_rho_factor(num)
        stack.append(factor)
        stack.append(num // factor)
    runtime = time() - start_time

    return { 'factors': tuple(factors), 'runtime': runtime }
