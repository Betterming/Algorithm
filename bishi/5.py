import sys

if __name__ == '__main__':
    m, n = map(int, sys.stdin.readline().strip().split(','))
    mat = []
    for i in range(m):
        line = sys.stdin.readline().strip()
        mat.append(line)
    if n == 1 and m == 1:
        if mat[0][0] == 'S':
            print(1)
        else:
            print(0)