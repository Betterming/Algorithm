import sys

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().strip().split())
    nums = []
    s = set()
    for i in range(m):
        nums.append(int(sys.stdin.readline().strip()))
        for j in range(1, n+1):
            if j % nums[i] == 0:
                s.add(j)

    print(len(s))