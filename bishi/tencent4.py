import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    line = list(map(int, sys.stdin.readline().strip().split()))

    def getMedian(nums):
        n = len(nums)
        nums.sort()
        if n % 2 == 1:
            return nums[n // 2]
        else:
            return (nums[n//2-1] + nums[n//2]) // 2

    for i in range(len(line)):
        print(getMedian(line[:i] + line[i+1:]))
