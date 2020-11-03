import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    nums = list(map(int, sys.stdin.readline().strip().split()))
    import math
    print(math.log2(n))