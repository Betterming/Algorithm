import sys

def getMax(nums):
    return max(nums)


if __name__ == '__main__':
    line = list(map(int, input().strip().split()))
    print(getMax(line))