import sys


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    base = arr[0]
    less = [v for v in arr[1:] if base >= v]
    more = [v for v in arr[1:] if base < v]
    return quick_sort(less) + [base] + quick_sort(more)


if __name__ == '__main__':
    for line in sys.stdin:
        lst = list(map(int, line.strip().split()))
        if lst[0] == 0:
            break
        print(quick_sort(lst))


