from operator import *
from collections.abc import *


# 1. 链式比较
def chain_comparison():
    i = 3
    print(1 < i < 3)
    print(1 < i <= 3)


# ***
# 2. 不用if else 实现计算器
def calculator(a, b, k):
    return {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv,
        '**': pow
    }[k](a, b)


# 3.函数链
def add_or_sub(a, b, k):
    return (add if k == '+' else sub)(a, b)


# 4. 字符串长度
def str_byte_n(my_str):
    return len(my_str.encode('utf-8'))


# ***
# 5.求某一字符在字符串中第n次出现的位置
def search_n(target_str, pattern_char, n):
    size = 0
    for i, item in enumerate(target_str):
        if item == pattern_char:
            size += 1
        if size == n:
            return i

    return -1


# 6. 去掉最高最低求平均
def score_mean(lis):
    lis.sort()
    lis2 = lis[1:(len(lis) - 1)]
    return round(sum(lis2) / len(lis2), 2)  # round 采用传统的四舍五入法则，后面的2为精确到小数点后面2位


# 7. 交换元素
def swap(a, b):
    return b, a


# ***
# 8. 二分查找
def binary_search(arr, left, right, x):
    while left <= right:
        mid = int(left + (right - left) / 2)
        if arr[mid] == x:
            print("found %d, the index is %d" % (x, mid))
            return mid
        elif arr[mid] > x:
            right = mid - 1
            print("the area  reduced to [%d, %d]" % (left, right))
        else:
            left = mid + 1
            print("the area  reduced to [%d, %d]" % (left, right))
    return -1


# 10. 打印9*9乘法表
def print_9_table():
    for i in range(1, 10):
        for j in range(1, i+1):
            print("{0} * {1} = {2}".format(j, i, i * j), end="\t")
        print()


# ***
# 嵌套数组展开
def flatten(input_arr, output_arr=None):
    if output_arr is None:
        output_arr = []
    for ele in input_arr:
        if isinstance(ele, Iterable):
            flatten(ele, output_arr)
        else:
            output_arr.append(ele)
    return output_arr


def main():
    chain_comparison()
    print("a * b = ", calculator(5, 3, '*'))
    print("a ** b = ", calculator(2, 10, '**'))
    print("a +/- b = ", add_or_sub(32, 3, '+'))
    print(str_byte_n("i my python"))
    print(search_n("That was a banana!", "a", 3))
    print(search_n("That was a banana!", "a", 30))
    print(score_mean([90, 89, 70, 90, 84, 94, 73, 93, 70, 90, 99]))
    print(swap(2, 5))
    print(binary_search([34, 37, 39, 50, 54, 70], 1, 5, 54))
    print_9_table()
    print(flatten([[1, 2, 3, [10, 11], [21, 22, [31, 33]]], [5, 6]]))


if __name__ == '__main__':
    main()
