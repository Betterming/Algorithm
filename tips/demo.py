import sys

import sys

if __name__ == '__main__':
    for line in sys.stdin:
        n, *ln = map(int, line.strip().split())
        if n == 0:
            break
        s = 0
        for i in range(n):
            s += ln[0]
        print(s)

import re

