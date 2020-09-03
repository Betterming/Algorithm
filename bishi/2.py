import sys

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().strip().split())
    a = []

    for i in range(n):
        line = list(map(int, sys.stdin.readline().strip().split()))
        a.append(line)
    if n <= 2 and m <= 2:
        s = 0
        for i in range(n):
            for j in range(m):
                if a[i][j] == 1:
                    s += 1
        print(s)
