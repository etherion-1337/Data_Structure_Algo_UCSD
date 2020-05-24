# Uses python3
import sys

def gcd_naive(a, b):
    """brutal way to get gcd
    """
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_algo(a,b):
    """find gcd using Euclidean algo
    """
    i = max(a,b)
    j = min(a,b)

    if j == 0:
        return i
    else:
        reminder = i%j
        return gcd_algo(j, reminder)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    # print(gcd_naive(a, b))
    print(gcd_algo(a,b))
