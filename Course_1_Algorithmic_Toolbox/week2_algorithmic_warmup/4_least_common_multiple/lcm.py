# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

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

def lcm_algo(a,b):
    """ find lcm using gcd
    """
    ans = (a*b)/gcd_algo(a,b)
    return int(ans)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    # print(lcm_naive(a, b))
    print(lcm_algo(a,b))

