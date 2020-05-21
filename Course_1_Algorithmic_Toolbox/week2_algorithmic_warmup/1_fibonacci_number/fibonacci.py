# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_fast(n):
    if n <= 1:
        return n
    else:
        fib_p = ((1+5**0.5)/2)**n
        fib_m = ((1-5**0.5)/2)**n
        fib = (fib_p - fib_m)/(5**0.5)
        return fib

n = int(input())
print(calc_fib(n))
print(calc_fib_fast(n))
