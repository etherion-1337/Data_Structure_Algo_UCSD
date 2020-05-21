# Uses python3
def calc_fib(n):
    """ Slowest. Use Fibonacci definition
    """
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_algo(n):
    """ Faster algo. Use human like algo to  calculate
    """
    if n <= 1:
        return n
    else:
        prev = 0
        curr = 1
        for i in range(n - 1):
            prev, curr = curr, prev + curr
        return curr

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

n = int(input())

#print(calc_fib(n))
#print(calc_fib_algo(n))
print(calc_fib_fast(n))
