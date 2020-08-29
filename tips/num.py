import sys

def solution():
    li = []
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        line = list(map(int, sys.stdin.readline().strip().split()))
        if line[0] == 1:
            li.insert(line[1]-1, line[2])
        elif line[0] == 2:
            li.pop(line[1]-1)
        else:
            for i in li:
                print(i, end=' ')


if __name__ == '__main__':
    solution()


