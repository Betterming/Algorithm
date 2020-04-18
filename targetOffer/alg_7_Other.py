# -*- coding:utf-8 -*-
class Solution:

    def GetUglyNumber_Solution(self, index):
        """hard
        33. 把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。
         习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

        通俗易懂的解释：
        首先从丑数的定义我们知道，一个丑数的因子只有2,3,5，那么丑数p = 2 ^ x * 3 ^ y * 5 ^ z，换句话说一个丑数一定由另一个丑数乘以2或者乘以3或者乘以5得到，那么我们从1开始乘以2,3,5，就得到2,3,5三个丑数，在从这三个丑数出发乘以2,3,5就得到4，6,10,6，9,15,10,15,25九个丑数，我们发现这种方***得到重复的丑数，而且我们题目要求第N个丑数，这样的方法得到的丑数也是无序的。那么我们可以维护三个队列：
        （1）丑数数组： 1
        乘以2的队列：2
        乘以3的队列：3
        乘以5的队列：5
        选择三个队列头最小的数2加入丑数数组，同时将该最小的数乘以2,3,5放入三个队列；
        （2）丑数数组：1,2
        乘以2的队列：4
        乘以3的队列：3，6
        乘以5的队列：5，10
        选择三个队列头最小的数3加入丑数数组，同时将该最小的数乘以2,3,5放入三个队列；
        （3）丑数数组：1,2,3
        乘以2的队列：4,6
        乘以3的队列：6,9
        乘以5的队列：5,10,15
        选择三个队列头里最小的数4加入丑数数组，同时将该最小的数乘以2,3,5放入三个队列；
        （4）丑数数组：1,2,3,4
        乘以2的队列：6，8
        乘以3的队列：6,9,12
        乘以5的队列：5,10,15,20
        选择三个队列头里最小的数5加入丑数数组，同时将该最小的数乘以2,3,5放入三个队列；
        （5）丑数数组：1,2,3,4,5
        乘以2的队列：6,8,10，
        乘以3的队列：6,9,12,15
        乘以5的队列：10,15,20,25
        选择三个队列头里最小的数6加入丑数数组，但我们发现，有两个队列头都为6，所以我们弹出两个队列头，同时将12,18,30放入三个队列；
        ……………………
        疑问：
        1.为什么分三个队列？
        丑数数组里的数一定是有序的，因为我们是从丑数数组里的数乘以2,3,5选出的最小数，一定比以前未乘以2,3,5大，同时对于三个队列内部，按先后顺序乘以2,3,5分别放入，所以同一个队列内部也是有序的；
        2.为什么比较三个队列头部最小的数放入丑数数组？
        因为三个队列是有序的，所以取出三个头中最小的，等同于找到了三个队列所有数中最小的。
        实现思路：
        我们没有必要维护三个队列，只需要记录三个指针显示到达哪一步；“|”表示指针,arr表示丑数数组；
        （1）1
        |2
        |3
        |5
        目前指针指向0,0,0，队列头arr[0] * 2 = 2,  arr[0] * 3 = 3,  arr[0] * 5 = 5
        （2）1 2
        2 |4
        |3 6
        |5 10
        目前指针指向1,0,0，队列头arr[1] * 2 = 4,  arr[0] * 3 = 3, arr[0] * 5 = 5
        （3）1 2 3
        2| 4 6
        3 |6 9
        |5 10 15
        目前指针指向1,1,0，队列头arr[1] * 2 = 4,  arr[1] * 3 = 6, arr[0] * 5 = 5
        :param index:
        :return:
        """
        if index < 0:
            return None
        if index < 7:
            return index
        arr = []
        p1 = 0
        p2 = 0
        p3 = 0
        i = 0
        newData = 1
        arr.append(newData)
        while len(arr) < index:
            newData = min(arr[p1] * 2, arr[p2] * 3, arr[p3] * 5)
            arr.append(newData)
            if newData == arr[p1] * 2:
                p1 += 1
            if newData == arr[p2] * 3:
                p2 += 1
            if newData == arr[p3] * 5:
                p3 += 1

        return newData

    def printMatrix(self, matrix):
        """
        19. 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵：
        1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
        idea: 可以打印第一行，然后删除第一行，再将剩下的数组逆转90°，重复此操作。
        :param matrix:
        :return:
        """
        if not matrix:
            return []
        result = []
        while matrix:
            result += matrix.pop(0)
            if not matrix:
                break
            matrix = self.turn(matrix)
        return result

    def turn(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        newMat = []
        for i in range(col):
            newMat2 = []
            for j in range(row):
                newMat2.append(matrix[j][i])
            newMat.append(newMat2)
        newMat.reverse()
        return newMat

    def printMatrix2(self, matrix):
        """
        idea: 观察二维数组发现，可以逐层打印，先最外一层打印完了
        :param matrix:
        :return:
        """
        if not matrix:
            return []
        res = []
        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = col - 1
        top = 0
        bottom = row - 1
        while left <= right and top <= bottom:
            for i in range(left, right + 1):  # left to right
                res.append(matrix[top][i])
            for i in range(top + 1, bottom + 1):  # top to bottom
                res.append(matrix[i][right])
            if top < bottom:
                for i in range(right - 1, left - 1, -1):  # right to left
                    res.append(matrix[bottom][i])
            if left < right:
                for i in range(bottom - 1, top, -1):  # bottom to top
                    res.append(matrix[i][left])
            left += 1
            top += 1
            right -= 1
            bottom -= 1
        return res

    def MoreThanHalfNum_Solution(self, numbers):
        """array tips
        28. 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
        由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
        :param numbers:
        :return:
        """
        from collections import Counter
        count = Counter(numbers).most_common()
        if count[0][1] > len(numbers) / 2.0:
            return count[0][0]
        return 0

    def FindNumsAppearOnce(self, array):
        """
        40. 一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
        idea1: 利用python中统计的方法Counter
        :param array:
        :return:
        """
        from collections import Counter
        return list(map(lambda c: c[0], Counter(array).most_common()[-2:]))

    def FindNumsAppearOnce2(self, array):
        """
        idea2: 通用解法，哈希表统计每种数字出现的次数
        :param array:
        :return:
        """
        hashMap = {}
        for i in array:
            if str(i) in hashMap:
                hashMap[str(i)] += 1
            else:
                hashMap[str(i)] = 1
        res = []
        for k in hashMap.keys():
            if hashMap[k] == 1:
                res.append(int(k))
        return res

    def FindNumsAppearOnce3(self, array):
        """
        idea3: 异或法。
        此题用了两次异或运算特点：
        （1）第一次使用异或运算，得到了两个只出现一次的数相异或的结果。0与任何数异或为该数本身，相同的两个数异或为0
        （2）因为两个只出现一次的数肯定不同，即他们的异或结果一定不为0，一定有一个位上有1。另外一个此位上没有1，据此位上是否有1，将整个数组重新划分成两部分，
        一部分此位上一定有1，另一部分此位上一定没有1，然后分别对每部分求异或，因为划分后的两部分有这样的特点：
        其他数都出现两次，只有一个数只出现一次。因此，我们又可以运用异或运算，分别得到两部分只出现一次的数。
        :param array:
        :return:
        """
        if not array:
            return []
        tmp = 0
        for i in array:
            tmp ^= i

        # 找出tmp二进制从右到左第一个1出现的位置
        index = 0
        while (tmp & 1) == 0:
            tmp >> 1
            index += 1
        a = b = 0
        for i in array:
            if self.isBit(i, index):
                a ^= i
            else:
                b ^= i
        return [a, b]

    def isBit(self, num, index):
        num = num >> index
        return num & 1

    def FindContinuousSequence(self, tsum):
        """
        41.所有和为S的连续正数序列? 例如100为9到16这8个数之和，另外18,19,20,21,22之和也为100
        idea: 用双指针，若p1,p2所指范围的数之和等于tsum放入res,且p2++,若<tsum，p2++,若>tsum，p1++
        :param tsum:
        :return:
        """
        if len(tsum) == 0:
            return []
        res = []
        p1, p2 = 1, 2
        while p1 < p2:
            cur = (p1 + p2) * (p2 - p1 + 1) // 2
            if cur == tsum:
                arr = []
                for item in range(p1, p2 + 1):
                    arr.append(item)
                res.append(arr)
                p2 += 1
            elif cur < tsum:
                p2 += 1
            else:
                p1 += 1

    def FindNumbersWithSum(self, array, tsum):
        """
        42.输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
        如果有多对数字的和等于S，输出两个数的乘积最小的。小的先输出
        :param array:
        :param tsum:
        :return:
        """
        if len(array) <= 1:
            return []
        left, right = 0, len(array) - 1
        res = []
        while left < right:
            cur = array[left] + array[right]
            if cur == tsum:
                res.append(array[left])
                res.append(array[right])
                break
            elif cur < tsum:
                left += 1
            else:
                right -= 1
        return res

    def IsContinuous(self, numbers):
        """
        45. LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...
        他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！
        “红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以看成任何数字,
        并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。
        LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何，
        如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0
        idea: 判断numbers是不是顺子有三个条件：
        1. numbers长度为5
        2. numbers中最大值与最小值之差小于5
        3. 除了0之外，其余元素不能重复出现
        只要同时满足这三个条件就一定是顺子
        :param numbers:
        :return:
        """
        n_len = len(numbers)
        if n_len != 5:
            return False

        n_map = [0] * 14

        n_min, n_max = 14, -1
        for item in numbers:
            if item == 0:
                continue
            n_map[item] += 1

            if n_map[item] > 1:
                return False
            if item > n_max:
                n_max = item
            if item < n_min:
                n_min = item
        return True if n_max - n_min < 5 else False

    def LastRemaining_Solution(self, n, m):
        """
        46.题目：n个数字（0,1,…,n-1）形成一个圆圈，从数字0开始，每次从这个圆圈中删除序号为m-1。
        当一个数字删除后，从被删除数字的下一个继续删除第m个数字。求出在这个圆圈中剩下的最后一个数字。
        idea: 本题就是有名的约瑟夫环问题。可以用归纳法来做
        首先定义最初的n个数字（0,1,…,n-1）中最后剩下的数字是关于n和m的方程为f(n,m)。含义为：n个人需要喊m个数字（m-1号去除），最后一个人序号为f(n,m)
        该序号是n个人时从0到n-1的序号。在这n个数字中，第一个被删除的数字是(m-1)%n，记作k。
        删k后所剩n-1个数字为0,1,…,k-1,k+1,…,n-1，并且下一个开始计数的数字是k+1。相当于在剩下的序列中，k+1排到最前面，从而形成序列k+1,…,n-1,0,…k-1。
        该序列最后剩下的数字也应该是关于n和m的函数。由于这个序列的规律和前面最初的序列不一样（最初的序列是从0开始的连续序列），
        因此该函数不同于前面函数，记为f’(n-1,m)。最初序列最后剩下的数字f(n,m)一定是剩下序列的最后剩下数字f’(n-1,m)，所以f(n,m)=f’(n-1,m)。
        接下来我们把剩下的的这n-1个数字的序列k+1,…,n-1,0,…k-1作一个映射，映射的结果是形成一个从0到n-2的序列：
                k+1    ->    0
                k+2    ->    1
                …
                n-1    ->    n-k-2
                0   ->    n-k-1
                …
                k-1   ->   n-2

        把映射定义为p，则p(x)= (x-k-1)%n，即如果映射前的数字是x，则映射后的数字是(x-k-1)%n。对应的逆映射是p-1(x)=(x+k+1)%n。
        由于映射之后的序列和最初的序列有同样的形式，都是从0开始的连续序列，因此仍然可以用函数f来表示，记为f(n-1,m)。
        根据我们的映射规则，映射之前的序列最后剩下的数字f’(n-1,m)= p-1 [f(n-1,m)]=[f(n-1,m)+k+1]%n。
        把k=(m-1)%n代入得到f(n,m)=f’(n-1,m)=[f(n-1,m)+m]%n。当n=1时，也就是序列中开始只有一个数字0，那么很显然最后剩下的数字就是0。
        我们把这种关系表示为：
                 0                  n=1
        f(n,m)={
                 [f(n-1,m)+m]%n     n>1

        时间复杂度为O(n)，空间复杂度为O(1)

        总结：找f(n, m)和f(n-1, m)关系 => n人时被删除人的编号为k=(m-1)%n, 删除一人之后，前序号与后序列映射关系：p-1(x)=(x+k+1)%n
        (表示后序x经过p-1(x)得到前序)   =>
        :param n:
        :param m:
        :return:
        """
        # write code here
        if n < 1:
            return -1
        if n == 1:
            return 0
        s = 0
        for i in range(2, n + 1):
            s = (s + m) % i
        return s

    def duplicate(self, numbers, duplication):
        """
        50.在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。
        也不知道每个数字重复几次。请找出数组中任意一个重复的数字。
        例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2
        idea: hash法
        :param numbers:
        :param duplication:
        :return:
        """
        n_len = len(numbers)
        d = [0] * n_len
        for item in numbers:
            d[item] += 1
            if d[item] > 1:
                duplication[0] = item
                return True
        return False

    def duplicate2(self, numbers, duplication):
        """
        idea2:不需要额外的数组或者hash table来保存，题目里写了数组里数字的范围保证在0 ~ n-1 之间，
        所以可以利用现有数组设置标志，当一个数字被访问过后，可以设置对应位上的数 + n，之后再遇到相同的数时，
        会发现对应位上的数已经大于等于n了，那么直接返回这个数即可。
        :param numbers:
        :param duplication:
        :return:
        """
        n_len = len(numbers)
        for item in numbers:
            temp = item
            if temp >= n_len:
                temp -= n_len
            if numbers[temp] >= n_len:
                duplication[0] = temp
                return True
            numbers[temp] += n_len
        return False

    def multiply(self, A):
        """
        51.给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
        不能使用除法
        idea: 按上图把每行被1分割的两部分乘积都计算出来，这样可以从首尾分别用累乘算出两个列表，然后两个列表首尾相乘就是B的元素
        可以构造两个数组head = [1, A0, A0A1, A0A1A2, ..., A0A1...An-2]
        tail = [1, An-1, An-1An-2, An-1An-2An-3, ..., An-1An-2...A1]
        将两个数组对应交叉相乘可以B数组
        :param A:
        :return:
        """
        head = [1]
        tail = [1]
        for i in range(len(A) - 1):
            head.append(head[i] * A[i])
            tail.append(tail[i] * A[-i - 1])
        B = []
        for j in range(len(head)):
            B.append(head[j] * tail[-j - 1])
        return B

    def maxInWindows(self, num, size):
        """
        64.给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，
        那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
         {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}，
          {2,3,4,2,6,[2,5,1]}。
        idea: 用deque保留最后一个n个数
        :param num:
        :param size:
        :return:
        """
        length = len(num)
        if length <= 0 or size <= 0 or size > length:
            return []

        from collections import deque
        q = deque(maxlen=size)

        res = []
        for i in range(length):
            q.append(num[i])
            if i >= size - 1:
                res.append(max(q))
        return res

    def maxInWindows2(self, num, size):
        length = len(num)
        if length <= 0 or size <= 0 or size > length:
            return []
        res = []
        for i in range(length - size + 1):
            res.append(max(num[i:i + size]))
        return res

    def Find(self, param, param1):
        pass


if __name__ == '__main__':
    solution = Solution()
    res1 = solution.GetUglyNumber_Solution(0)
    print("GetUglyNumber_Solution: %s" % res1)

    res2 = solution.Find(4, [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]])
    print("Find: %s" % res2)
    res4 = solution.printMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    print("printMatrix: ", res4)
    res42 = solution.printMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    print("printMatrix: ", res42)

    res5 = solution.MoreThanHalfNum_Solution([1, 2, 3, 2, 2, 2, 5, 4, 2])
    print("MoreThanHalfNum_Solution: ", res5)
