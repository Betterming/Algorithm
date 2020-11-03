import sys

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().strip().split())
    nums = []
    s = set()
    for i in range(m):
        line = set(map(int, sys.stdin.readline().strip().split()))
        nums.append(line)
        if 0 in line:
            for j in line:
                s.add(j)
    for i in range(m):
        if len(s.intersection(nums[i])) > 0:
            for j in nums[i]:
                s.add(j)
    print(len(s))