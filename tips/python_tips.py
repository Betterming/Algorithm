"""
python刷题常用功能
"""


class Solution:
    # 1.list
    # 初始化, 遍历，枚举enumerate，拉链聚合
    def listDemo(self, arr, arr2):
        l = [0 for _ in range(len(arr))]
        l = [0] * len(arr)
        rows = len(arr2)
        cols = len(arr2[0])
        l = [[0] for i in range(cols) for j in range(rows)]

        # 从后向前遍历
        for i in range(0, -10, -1):
            print(i)

        # enumerate用法
        for index, item in enumerate(arr):
            print('NO {0}: {1}'.format(index, item))
            print('NO {1}: {0} : {1}'.format(index, item))
            print('N0 {index}: {item}'.format(index=index, item=item))

        # zip聚合用法, 能成多少对取决于最短的那个
        d = dict()
        for x, y in zip([1, 3, 5, 7], ['a', 'c', 'e']):
            d[x] = y
            print(x, y)
        print(d)

    # 2.copy, 深浅拷贝：浅拷贝，拷贝对象，但不拷贝对象里面引用的对象。深拷贝，拷贝对象，而且拷贝对象里面引用的对象。
    def copyDemo(self):
        a = [1, 2, [3, 4]]
        a1 = a
        print(a1)

        b = a[:]
        a[2].append(5)
        print(a, b)

        import copy
        c = copy.deepcopy(b)
        a[2].append(5)
        print(a, c)

    # reduce：可以分别对相邻元素使用同一种计算规则，同时每一步结果作为下一步的参数，很典型的函数式编程用法。
    def reduceDemo(self, arr):
        from functools import reduce
        print('The sum of the array is ', reduce(lambda a, b: a+b, arr))

    # map:它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回,可以将参数一一映射来计算.
    def mapDemo(self, arr):
        lis = map(lambda x: x**x, arr)
        print(list(lis))

        s = '123'
        s_int = map(int, s)
        print(list(s_int))

        format_name = ['admin', 'LISA', 'boB']
        print(list(map(lambda s: s[0].upper() + s[1:].lower(), format_name)))
        d = {'math': 89, 'English': 70, 'history': 90, 'piano': 95}

        def f(st, i):
            return st[0].upper() + st[1:] + str(i), i * 1.2
        print(list(map(f, d.keys(), d.values())))

    # deque: list 删除末尾的操作是`O(1)`的，但是删除头操作就是`O(n)`，这时候我们就需要一个双端队列 `deque`。
    # 在序列的前后你都可以执行添加或删除操作。
    # 首尾的常规操作为：
    # - `append`，添加到末尾
    # - `appendleft`, 添加到开头
    # - `pop`, 剔除末尾
    # - `popleft`，移除开头
    def dequeDemo(self):
        """
        运行结果：
        deque([2, 3, 4], maxlen=3)
        deque([2, 3], maxlen=3)
        deque([50, 2, 3], maxlen=3)
        deque([60, 50, 2], maxlen=3)
        deque([50, 2], maxlen=3)
        :return:
        """
        from collections import deque
        dq = deque(maxlen=3)
        dq.append(1)
        dq.append(2)
        dq.append(3)
        dq.append(4)
        print(dq)

        dq.pop()
        print(dq)
        dq.appendleft(50)
        print(dq)
        dq.appendleft(60)
        print(dq)
        dq.popleft()
        print(dq)

    # 排序， 不改变原list
    def sortedDemo(self):
        l1 = [('math', 90), ('history', 80), ('English', 89)]
        l2 = sorted(l1, key=lambda x: x[1], reverse=True)
        print(l2)

    def lambdaDemo(self):
        from math import sqrt
        f = lambda x, y: sqrt(x**2 + y**2)
        print(f(3, 4))

    # cmp_to_key: 在 python3 中，sorted 函数取消了自带的cmp函数，需要借助functools 库中的 cmp_to_key来做比较。比如如果要按照数组元素的绝对值来排序
    def cmpDemo(self, arr):
        def sortFunc(a, b):
            if abs(a) < abs(b):
                return -1
            elif abs(a) > abs(b):
                return 1
        from functools import cmp_to_key
        newArr = sorted(arr, key=cmp_to_key(sortFunc))
        print(newArr)

    """
    set 的查找操作复杂度为`O(1)`，有时候可以替代`dict` 来存储中间过程。

    - `add` : set 的添加是 `add` 不是`append`
    - `remove` vs `discard`: 都是删除操作，区别在于`remove`不存在的元素会报错，`discard`不会。
    - `union`, `intersection`: 快速获得并集和交集，方便一些去重操作。
    """
    def setDemo(self):
        a = {1, 3, 1}
        print(a)

        st = set()
        st.add(1)
        st.add(2)
        st.add(1)
        st.remove(1)
        print(st)

    # dict
    # OrderedDict: 能记录你 key 和 value 插入的顺序，底层其实是一个双向链表加哈希表的实现。我们甚至可以使用move_to_end这样的函数
    # defaultdict: 以很好地来解决一些初始化的问题，比如 value 是一个 list，每次需要判断 key 是否存在的情况
    def dictDemo(self):
        a = dict()

        a.setdefault(1, 'null')  # 先尝试把如果key=1不存在的话，就插入{1:0},若存在就插入无效
        print(a)
        a[1] = 'hello'
        a.setdefault(1, 'null')
        print(a)
        a[2] = 'this'
        a[3] = 'world'
        for k, v, item in zip(a.keys(), a.values(), a.items()):
            print('key = %03d, value = %s' % (k, v))
            print(item)

        from collections import OrderedDict, defaultdict
        od =OrderedDict()
        od.fromkeys('abcde')
        od.setdefault('a', 1)
        od.setdefault('b', 2)
        od.setdefault('c', 3)
        od.setdefault('d', 1)
        od.move_to_end('a')
        print(od)

        dd = defaultdict(list)
        s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
        for k, v in s:
            dd[k].append(v)
        sorted(dd.items())  # 字典按照key排序
        print(dd)

    # heapq: 即priority queue，heapq 就是 python 的 `priority` queue，`heapq[0]`即为堆顶元素。
    # heapq 的实现是小顶堆，如果需要一个大顶堆，常规的一个做法是把值取负存入，取出时再反转。以下是借助 heapq 来实现 heapsort 的例子：
    # heapq.heappush,heappop,nlargest(k, nums)
    def heapqDemo(self, arr, k):
        import heapq
        res = heapq.nlargest(k, arr)[-1]
        print(res)
        h = []
        for item in arr:
            heapq.heappush(h, item)

        print([heapq.heappop(h) for _ in range(len(h))])

    # 统计频率相关的，counter(list) 返回一个字典，可以使用most_common(3)统计频率最高的3个tuple元素
    def counterDemo(self, k):
        s = 'abracadabra'
        from collections import Counter
        for index, item in enumerate(Counter(s).most_common(k)):
            print("No %d: (item: %s, freq: %d)" % (index+1, item[0], item[1]))

    # string中ord，chr，字符的unicode码和字符转换
    def stringsDemo(self):
        print(ord('a'))  # 97
        print(chr(100))  # 'd'

        import re
        a = " jjj jk , ajg l aj; a k"
        array = re.split(r'\s*[,;\s]\s*', a.strip())  # 切割的匹配模式是0个或多个空个或者，或者；或者（，；前后0个或者多个空格）
        print(array)
        print(''.join(array))
        print('+'.join(array))

    # float/int最值
    # float('inf')/float('-inf')
    def maxOrminDemo(self):
        print(float('inf'))
        print(float('-inf'))

    # all() 函数用于判断给定的可迭代参数 iterable中的所有元素是否不为 0、''、False 或者 iterable 为空，如果是返回 True，否则返回 False。
    # any() 函数用于判断给定的可迭代参数 iterable 是否全部为空对象，如果都为空、0、false，则返回 False，
    # 如果不都为空、0、false，则返回 True.  有一个不为空返回True
    def anyOrallDemo(self):
        names = ('name', 'laoda', 'laoer',)
        names2 = ('name', 'laoda', 'laoer', False)
        names3 = ('name', 'laoda', 'laoer', [])

        print(all(names))  # True
        print(all(names2))  # False
        print(all(names3))  # False

        #  简单来说,有一个不为空,返回True
        names = ('frank', 'lijiaxuan', 'weiliang', 'lile', ' ')
        defaults = ('', None, [], (), False,)
        hobbys = ['name', False, [], (), ]

        print(any(names))  # True
        print(any(defaults))  # False
        print(any(hobbys))  # True

    # permutations/combinations 排列组合A(n,m), C(n, m)
    def permutationsOrCombinations(self):
        from itertools import permutations, combinations
        s = 'abcde'
        perList = []
        combList = []
        for item in list(permutations(s, 3)):
            perList.append(''.join(item))
        for item in list(combinations(s, 3)):
            combList.append(''.join(item))

        print(perList)
        print(combList)


if __name__ == '__main__':
    solution = Solution()
    arr = [1, 3, 5]
    testArr = [3, -6, 7, -2, 1, 5, 4]
    arr2 = [[2, 4, 5], [2, 3, 6]]

    solution.listDemo(arr, arr2)
    solution.copyDemo()
    solution.reduceDemo(arr)
    solution.mapDemo(arr)
    solution.dequeDemo()
    solution.sortedDemo()
    solution.lambdaDemo()
    solution.cmpDemo(testArr)
    solution.setDemo()
    solution.dictDemo()
    solution.heapqDemo(testArr, 4)
    solution.counterDemo(4)
    solution.stringsDemo()
    solution.maxOrminDemo()
    solution.anyOrallDemo()
    solution.permutationsOrCombinations()


