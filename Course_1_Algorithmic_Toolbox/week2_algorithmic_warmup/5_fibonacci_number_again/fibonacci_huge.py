# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def get_fibonacci_huge(n,m):
    previous = 0
    current = 1
    
    for i in range(m*m):
        previous, current = current, (current+previous)%m
        if (previous, current) == (0,1):
            period = i + 1
            break

    j = n%period

    if j == 0:
        return j
    else:
        previous = 0
        current = 1
        for i in range (2, j+1):
            previous, current = current, (current+previous)%m
        return current

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    # print(get_fibonacci_huge_naive(n, m))
    print(get_fibonacci_huge(n,m))
