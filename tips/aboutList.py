# 一，递归调用的理解：
# 1. 想要将n个值列表反转放进result_array数组中，可以先将后面n-1个节点值放入result_array数组，然后第一个节点值在放入
# 2. 若想将后n-1个值列表反转放进result_array数组中，可以先将后面n-2个节点值放入result_array数组，然后第二个节点值在放入，依次类推。。。
# 3. 边界：最后一个值想要放入result_array数组中，则先将最后一个值的next节点的值即None放入result_array数组中，
# 而当printListFromTailToHead的入参为None时结束递归，进行下一步，将最后一个值放入result_array中，依次反向带入值，完成原列表反向所有值放入到result_array中

# 二，Python中列表[]对stack，queue，array的实现
# stack常见操作：push，pop，isEmpty,size,clear  python实现：append(object), pop(-1)=pop(),len(stack)/None/''/[], len(stack), clear
# queue常见操作：enqueue，dequeue，isEmpty,size,clear  Python实现：append(object),pop(0),len(queue)/None/''/[], len(stack), clear
# array常见操作：add，insert，isEmpty,size,clear Python实现：append(object), insert(index, object), len(queue)/None/''/[], len(stack), clear
# 另外关于数组还可以实现:
# 1) a.sort(key=lambda x: x.val, reverse=True)
# 2) array.index(object, start, stop),object在array数组从start到stop中的序号；
# 3) remove(object)(去除数组中第一个等于object的元素),
# 4) reserve()(反转);
# 5) copy(),
# 6) a.count(2),统计a数组中值等于2的个数
# 7) extend(): 用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表),返回值为None。只能a.extend(b)，若想用a，b的一部分数据，必须先处理好后再用extend

# 三、Python中字符串
a = " jjj jk , ajg l aj; a k"
import re
re.split(r'[,;\s]\s*', a)
# 1) 相加：str1 + str2, 两字符串可直接相加拼接，但是不能和其他类型直接相加
# 2) 截取：a[2:5:2], a[start:end:step]
# 3) 分割：a.split(sep, maxSplit),sep为分割符，默认为空字符(包括空格，换行“\n", 制表"\t")，maxSplit:最大分割次数，默认或者-1为没有限制.
#    若想复杂的分割可用re.split(pattern, anyString, maxSplit), pattern为正则表达式，一般用 r'[,;.\s]\s*' 表示
# 4)

# 四，对于Node的理解：
# 1.常量 None（N 必须大写）和 False 不同，它不表示 0，也不表示空字符串，而表示没有值，也就是空值，它属于 NoneType 类型。
# 2.None 是 NoneType 数据类型的唯一值（其他编程语言可能称这个值为 null、nil 或 undefined），也就是说，我们不能再创建其它 NoneType 类型的变量，
#   但是可以将 None 赋值给任何变量。如果希望变量中存储的东西不与任何其它值混淆，就可以使用 None。
# 3. None 常用于 assert、判断以及函数无返回值的情况。例如：print() 函数输出数据，其实该函数的返回值就是 None。
#    因为它的功能是在屏幕上显示文本，根本不需要返回任何值，所以 print() 就返回 None。
# 4. 没有return语句的函数定义，Python 都会在末尾加上 return None，使用不带值的return 语句（也就是只有return关键字本身），那么就返回None。
# 5. 进行逻辑判断（比如if）时，Python当中等于False的值并不只有False一个，它也有一套规则。
# 对于基本类型来说，基本上每个类型都存在一个值会被判定为False。大致是这样：
# 布尔型，False表示False，其他为True
# 整数和浮点数，0表示False，其他为True
# 字符串和类字符串类型（包括bytes和unicode），空字符串表示False，其他为True
# 序列类型（包括tuple，list，dict，set等），空表示False，非空表示True
# None永远表示False
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


result_array = []
def printListFromTailToHead(listNode):
    # write code here
    if listNode:
        printListFromTailToHead(listNode.next)
        result_array.append(listNode.val)
    return result_array

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print(printListFromTailToHead(node1))


def test():
    a = [1, 2, 3, 4, 5]
    stack = []
    for item in a:
        stack.append(item)
    stack.pop(0)
    # stack.pop(-1)
    for i in stack:
        print(i)
    print('-----------------------------')
    while stack:
        print(stack.pop())

print('-----------------------------')
def test2():
    a = [ListNode(2), ListNode(3), ListNode(1), ListNode(5), ListNode(4)]
    stack = [1, 2, 2, 3, 1, 3, 1, 3, 4]
    extend = [1, 1, 1, 1, 1]
    # stack[:-2].extend(extend) # 不能改变stack结果
    stack.extend(extend)
    print('stack extend list extend: ', stack)
    print('-------------')
    a.sort(key=lambda x: x.val, reverse=True)
    for i in a:
        print(i.val)
    print(stack.count(1))
    print('-----------------------------')
    print(stack.index(1, 1, 5)) # 找出stack中元素1在[1,5)中的位置序号（该序号是在stack中的序号）
    print('-----------------------------')
    stack.remove(2)
    for i in stack:
        print(i)
test2()