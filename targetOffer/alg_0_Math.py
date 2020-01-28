# -*- coding:utf-8 -*-

"""
对于数学问题，首先要从小数举例开始，然后找到规律，用dp比较多，或者一些操作技巧，比如搜索技巧
"""
import functools


class Solution:
    """

    """
    def Fibonacci(self, n):
        """
        1. 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。n<=39
        idea: 动态规划：dp[0] = 0, dp[1] = 1, dp[i] = dp[i-1] + dp[i-2]
        :param n:
        :return:
        """
        # write code here
        f0 = 0
        f1 = 1
        if n < 2:
            return n
        for i in range(n):
            f1, f0 = f1 + f0, f1
        return f0

    def jumpFloorII(self, number):
        """
        2. 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
        idea: 动态规划：f(1) = 1, f(n) = 2*f(n)
        :return: 
        """
        if number <= 0:
            return 0
        if number == 1:
            return 1
        f = 1
        for _ in range(number - 1):
            f = f * 2
        return f

    def rectCover(self, number):
        """
        3. 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法
        idea：dp法，f(n) = f(n-1) + f(n-2)
        :return:
        """
        if number <= 0:
            return 0
        if number <= 3:
            return number

        f1 = 1
        f2 = 2
        for _ in range(number - 2):
            f2, f1 = f2 + f1, f2

        return f2

    def NumberOf1Between1AndN_Solution(self, n):
        """
        3.求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13
        因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,
        可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）
        idea: 将1到n之间的所有数字字符串化，然后全部来连起来统计1的个数
        :param n:
        :return:
        """
        if n <= 0:
            return 0
        res = ''
        for i in range(n+1):
            res += str(i)
        return res.count('1')

    def NumberOf1Between1AndN_Solution2(self, n):
        """
        idea:像类似这样的问题，我们可以通过归纳总结来获取相关的东西。首先可以先分类：
    个位: 我们知道在个位数上，1会每隔10出现一次，例如1、11、21等等，我们发现以10为一个阶梯的话，每一个完整的阶梯里面都有一个1，
    例如数字22，按照10为间隔来分三个阶梯，在完整阶梯0-9，10-19之中都有一个1，但是19之后有一个不完整的阶梯，
    我们需要去判断这个阶梯中会不会出现1，易推断知，如果最后这个露出来的部分小于1，则不可能出现1（这个归纳换做其它数字也成立）。
    我们可以归纳个位上1出现的个数为：n/10 * 1+(n%10!=0 ? 1 : 0)

    十位:
    现在说十位数，十位数上出现1的情况应该是10-19，依然沿用分析个位数时候的阶梯理论，我们知道10-19这组数，每隔100出现一次，
    这次我们的阶梯是100，例如数字317，分析有阶梯0-99，100-199，200-299三段完整阶梯，每一段阶梯里面都会出现10次1（从10-19），
    最后分析露出来的那段不完整的阶梯。我们考虑如果露出来的数大于19，那么直接算10个1就行了，因为10-19肯定会出现；如果小于10，
    那么肯定不会出现十位数的1；如果在10-19之间的，我们计算结果应该是k - 10 + 1。例如我们分析300-317，17个数字，1出现的个数应该是17-10+1=8个。
    那么现在可以归纳：十位上1出现的个数为：设k = n % 100，即为不完整阶梯段的数字
    归纳式为：(n / 100) * 10 + (if(k > 19) 10 else if(k < 10) 0 else k - 10 + 1)

    百位:现在说百位1，我们知道在百位，100-199都会出现百位1，一共出现100次，阶梯间隔为1000，100-199这组数，
    每隔1000就会出现一次。这次假设我们的数为2139。跟上述思想一致，先算阶梯数 * 完整阶梯中1在百位出现的个数，
    即n/1000 * 100得到前两个阶梯中1的个数，那么再算漏出来的部分139，沿用上述思想，不完整阶梯数k199，
    得到100个百位1，100<=k<=199则得到k - 100 + 1个百位1。那么继续归纳百位上出现1的个数：设k = n % 1000
    归纳式为：(n / 1000) * 100 + (if(k >199) 100 else if(k < 100) 0 else k - 100 + 1)
    后面的依次类推....再次回顾个位,我们把个位数上算1的个数的式子也纳入归纳式中
    k = n % 10
    个位数上1的个数为：n / 10 * 1 + (if(k > 1) 1 else if(k < 1) 0 else k - 1 + 1)

    完美！归纳式看起来已经很规整了。 来一个更抽象的归纳，设i为计算1所在的位数，i=1表示计算个位数的1的个数，10表示计算十位数的1的个数等等。
    k = n % (i * 10)
    count(i) = (n / (i * 10)) * i + (if(k > i * 2 - 1) i else if(k < i) 0 else k - i + 1)
    好了，这样从10到10的n次方的归纳就完成了。
    sum1 = sum(count(i))，i = Math.pow(10, j), 0<=j<=log10(n)
    但是有一个地方值得我们注意的，就是代码的简洁性来看，有多个ifelse不太好，能不能进一步简化呢？
    我们可以把后半段简化成这样，我们不去计算i * 2 - 1了，我们只需保证k - i + 1在[0, i]区间内就行了，最后后半段可以写成这样
    min(max((n mod (i*10))−i+1,0),i)
        :param n:
        :return:
        """
        if n <= 0:
            return 0
        count = 0
        i = 1
        while i <= n:
            div = i * 10
            count += (n // div) * i + min(max(n % div - i + 1, 0), i)
            i *= 10
        return count

    def compare(self, x, y):
        if x + y < y + x:
            return -1
        elif x + y > y + x:
            return 1
        else:
            return 0

    def PrintMinNumber(self, numbers):
        """
        4. 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，
        则打印出这三个数字能排成的最小数字为321323。
        idea: 重写排序规则，由数组中的某两个元素来定，如果x+y < y+x, 那么x排在y前面
        总结一下排序规则：
        1.由元素本身大小直接用numbers.sort(),正排序还是逆排序由reverse来决定
        2.由元素某一部分或元素的某几个部分综合或者元素的非大小特征来决定排序规则用numbers.sort(key=lambda x.i + x.j : x)，
            numbers.sort(key=lambda x % 2 : x)，得到的是numbers中偶数在前，奇数在后序列
        3.由若干个元素比较规则：则用cmp, numbers.sort(key=functools.cmp_to_key(self.compare)), 自己重写compare，这是一般做法
        :param numbers:
        :return:
        """
        if not numbers:
            return ""
        numbers = list(map(str, numbers))
        numbers.sort(key=functools.cmp_to_key(self.compare))
        return "".join(numbers).lstrip('0')


if __name__ == '__main__':
    solution = Solution()
    res1 = solution.Fibonacci(5)
    print("Fibonacci: ", res1)

    res2 = solution.jumpFloorII(5)
    print("jumpFloorII:", res2)
