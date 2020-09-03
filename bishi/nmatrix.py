import sys


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    a = [[0] * n for _ in range(n)]
    x, y = n//2, n//2
    for i in range(n):
        for j in range(n):
            if i < x:
                if j < y:
                    if i < j:
                        a[i][j] = 2
                    elif i > j:
                        a[i][j] = 3
                elif j >= n - y:
                    if i < n - 1 - j:
                        a[i][j] = 1
                    elif i > n - 1 - j:
                        a[i][j] = 8
            elif i >= n - x:
                if j < y:
                    if i < n - 1 - j:
                        a[i][j] = 4
                    elif i > n - 1 - j:
                        a[i][j] = 5
                elif j >= n - y:
                    if i < j:
                        a[i][j] = 7
                    elif i > j:
                        a[i][j] = 6
    for i in range(n):
        for j in range(n):
            if j < n - 1:
                print(a[i][j], end=' ')
            else:
                print(a[i][j], end='')
        if i < n - 1:
            print()





