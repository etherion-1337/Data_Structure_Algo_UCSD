def max_pairwise_product(numbers):
    """Slow method that exhaustively find pairs that gives the maximum product
    """
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

def max_pairwise_product_sort(numbers):
    """Sort the list first, then take the last two number (biggest) and multiply them
    """
    sorted_list = sorted(numbers)
    ans = sorted_list[-1]*sorted_list[-2]
    return ans

def max_pairwise_product_fast(numbers):
    """Find the largest 2 numbers by scanning through the list
    """
    num_list = numbers.copy()
    max_num_1 = max(num_list)
    num_list.remove(max_num_1)
    max_num_2 = max(num_list)
    ans = max_num_1*max_num_2
    return ans


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_sort(input_numbers))

