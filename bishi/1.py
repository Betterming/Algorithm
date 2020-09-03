import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    red, blue = [], []

    for i in range(n):
        a, b = map(int, sys.stdin.readline().strip().split())
        if b == 1:
            red.append((a, i+1))
        else:
            blue.append((a, i+1))
    import heapq
    red3, blue3 = [], []
    # if len(red) >= 3:
    #     red3 = heapq.nlargest(3, red, key=lambda x: x[0])
    #
    # if len(blue) >= 3:
    #     blue3 = heapq.nlargest(3, blue, key=lambda x: x[0])
    red3 = sorted(red, key=lambda x: x[0], reverse=True)[:3]
    blue3 = sorted(blue, key=lambda x: x[0], reverse=True)[:3]
    if len(red3) == 0 and len(blue3) == 0:
        print("null")
    else:
        res = 0
        index = []
        flag = 1
        sred, sblue = 0, 0
        index_red, index_blue = [], []
        for item in red3:
            sred += item[0]
            index_red.append(item[1])
            index_red.sort()
        for item in blue3:
            sblue += item[0]
            index_blue.append(item[1])
            index_blue.sort()
        if sred > sblue:
            res = sred
            index = index_red
        elif sred < sblue:
            res = sblue
            index = index_blue
            flag = 2
        else:
            if index_red[0] < index_blue[0]:
                res = sred
                index = index_red
            else:
                res = sblue
                index = index_blue
                flag = 2

        for i in range(3):
            if i < 2:
                print(index[i], end=' ')
            else:
                print(index[i])
        print(flag)
        print(res)