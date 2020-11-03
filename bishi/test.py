import sys


def solve(nums, m):
    n_len = len(nums)
    a = nums[:n_len // 2]
    b = nums[n_len // 2:]

    res = list()
    while m > 0:
        res = []
        i = 0
        while i < len(a):
            res.append(b[i])
            res.append(a[i])
            i += 1
        if len(b) % 2 == 1:
            res.append(b[-1])
        a, b = res[:n_len // 2], res[n_len // 2:]
        m -= 1
    return res


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().strip().split())
    line = list(map(int, sys.stdin.readline().strip().split()))
    num = solve(line, m)
    for i in range(n):
        if i < n-1:
            print(num[i], end=' ')
        else:
            print(num[i])