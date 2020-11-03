import sys

def getCommon(a, b):
    res = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            res.append(a[i])
            i += 1
            j += 1
        elif a[i] > b[j]:
            i += 1
        else:
            j += 1
    return res


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    m = int(sys.stdin.readline().strip())
    b = list(map(int, sys.stdin.readline().strip().split()))
    ans = getCommon(a, b)
    for i in range(len(ans)):
        if i < len(ans) - 1:
            print(ans[i], end=' ')
        else:
            print(ans[i], end='')
