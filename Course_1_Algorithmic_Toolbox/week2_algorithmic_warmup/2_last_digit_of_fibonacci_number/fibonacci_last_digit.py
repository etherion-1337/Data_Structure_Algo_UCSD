# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def calc_fib_fast(n):
    """ Directly use maths formula
    """
    if n <= 1:
        return n
    else:
        fib_p = ((1+5**0.5)/2)**n
        fib_m = ((1-5**0.5)/2)**n
        fib = (fib_p - fib_m)/(5**0.5)
        return int(fib)


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
