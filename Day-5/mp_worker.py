"""Worker function for the multiprocessing.Pool demo in task.ipynb.

Needs to live in a real module (not a notebook cell) so Windows' spawn-based
multiprocessing can pickle and import it in child processes.
"""


def count_primes_below(n):
    count = 0
    for num in range(2, n):
        is_prime = True
        for d in range(2, int(num ** 0.5) + 1):
            if num % d == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count
