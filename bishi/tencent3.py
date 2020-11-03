import sys


if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().strip().split())
    nums = []
    for i in range(n):
        line = sys.stdin.readline().strip()
        nums.append(line)
    from collections import Counter
    temp = Counter(nums).most_common()
    a = temp[:k]
    a_len = len(a)
    for i in range(a_len):
        print(a[i][0], end=' ')
        print(a[i][1], end='')
        if i < a_len-1:
            print()

    print()

    from functools import cmp_to_key
    def cmp(a, b):
        if a[1] > b[1]:
            return 1
        elif a[1] == b[1]:
            if a[0] > b[0]:
                return 1
            else:
                return -1
        else:
            return -1
    temp.sort(key=cmp_to_key(cmp))
    last = temp[:k]
    print(last)
    last_len = len(last)
    for item in range(last_len):
        print(last[item][0], end=' ')
        print(last[item][1], end='')
        if item < last_len - 1:
            print()
