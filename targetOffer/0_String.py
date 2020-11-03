class Solution:
    def __init__(self):
        self.s = ''
        self.hash = [0] * 256
    def replaceSpace(self, s):
        """ simple
        2. 请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
        思路：1) 直接用string的replace方法 2) 用一个新的的数组，从前向后边判断边复制 3) 在原来数组上从后向前边判断边复制
        """
        return s.replace(' ', '%20')

    def replaceSpace2(self, s):
        s_len = len(s)
        space_count = 0
        for i in s:
            if i == ' ':
                space_count += 1

        s_len += 2 * space_count
        # new_array = [' '] * s_len
        new_array = [''] * s_len
        j = 0
        for i in range(len(s)):
            if s[i] == ' ':
                new_array[j] = '%'
                new_array[j + 1] = '2'
                new_array[j + 2] = '0'
                j += 3
            else:
                new_array[j] = s[i]
                j += 1
        return ''.join(new_array)

    def replaceSpace3(self, s):
        if not s:
            return None
        s_len = len(s)
        if s_len <= 0:
            return ''
        space_count = 0
        for i in s:
            if i == ' ':
                space_count += 1

        s += ' ' * space_count * 2
        j = space_count
        for i in range(s_len-1, -1, -1):
            if s[i] != ' ':
                s[i + j * 2] = s[i]
            else:
                s[i + j * 2] = '0'
                s[i + j * 2 - 1] = '2'
                s[i + j * 2 - 2] = '%'
                j -= 1
        return s


    def Permutation(self, ss):
        """
        27.字符串排序输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,
        则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
        :param ss:
        :return:
        """
        if len(ss) <= 1:
            return ss
        res = set()
        for i in range(len(ss)):
            for j in self.Permutation(ss[:i] + ss[i+1:]):
                res.add(ss[i] + j)
        return sorted(res)

    def Permutation2(self, ss):
        if len(ss) <= 1:
            return ss
        from itertools import permutations
        res = list(map(lambda x: ''.join(list(x)), permutations(ss)))
        return res


    def FirstNotRepeatingChar(self, s):
        """
        34. 在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
        idea: 暴力判断（用字符串的count方法，实际是采用哈希方法 （字典））
        :param s:
        :return:
        """
        if len(s) > 10000 or len(s) <= 0:
            return -1
        for i in s:
            if s.count(i) == 1:
                return s.index(i)

    def FirstNotRepeatingChar2(self, s):
        """
        使用字典
        :param s:
        :return:
        """
        if not s or len(s) > 1000 or len(s) <= 0:
            return -1
        d = {}
        for i in s:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
        for k, v in d.items():
            if v == 1:
                return s.index(k)

    def FirstNotRepeatingChar3(self, s):
        """
        用字典，k为字符，v为位置，当存在时，v += len(s)
        :param s:
        :return:
        """
        s_len = len(s)
        if not s or s_len > 1000 or s_len <= 0:
            return -1
        d = {}
        for i in range(s_len):
            if s[i] in d:
                d[s[i]] += s_len
            else:
                d[s[i]] = i
        res = s_len
        for k, v in d.items():
            if v < s_len:
                res = min(res, v)
        if res == s_len:
            return -1
        else:
            return res




    def LeftRotateString(self, s, n):
        """
        43. 循环左移n位后的序列输出
        例如: "1234", 循环左移7位为："4123"
        idea: 字符串拼接技巧
        :param s:
        :param n:
        :return:
        """
        if len(s) == 0 or n < 0:
            return ''
        n = n % len(s)
        return s[n:] + s[:n]

    def StrToInt(self, s):
        """
        49. 字符串转成整数，非法输出0
        :param s:
        :return:
        """
        if not s or len(s) == 0:
            return 0
        flag = 1
        if s[0] == '+':
            s = '0' + s[1:]
        elif s[0] == '-':
            s = '0' + s[1:]
            flag = -1
        res = 0
        for i in s:
            if '0' <= i <= '9':
                res = res * 10 + ord(i) - ord('0')
            else:
                return 0
        return flag * res

    def ReverseSentence(self, s: str):
        """
        44. 反转单词顺序："student. a am I" --> "I am a student."
        idea: 字符串拆分与拼接，注意边界
        :param s:
        :return:
        """
        if s == '':
            return ''
        words = s.split(' ')[::-1]
        res = ' '.join(words)
        return res

    def match(self, s, pattern):
        """
        52. 匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
         在本题中，匹配是指字符串的所有字符匹配整个模式。
        例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
        idea: 利用状态机，分为几种情况（分类讨论，可合并的要和合并）
        （1）当第二个字符不为‘*’时：匹配就是将字符串和模式的指针都下移一个，不匹配就直接返回false
        （2）当第二个字符为'*'时：
                匹配：
                        a.字符串下移一个，模式不动
                        b.字符串下移一个，模式下移两个
                        c.字符串不动，模式下移两个
                不匹配：字符串下移不动，模式下移两个
        搞清楚这几种状态后，用递归实现即可：
        :param s:
        :param pattern:
        :return:
        """
        if len(s) == 0 and len(pattern) == 0:
            return True
        elif len(s) > 0 and len(pattern) == 0:
            return False
        elif len(s) == 0 and len(pattern) > 0:
            if len(pattern) > 1 and pattern[1] == '*':
                return self.match(s, pattern[2:])
            else:
                return False

        if len(pattern) > 1 and pattern[1] == '*':
            if s[0] == pattern[0] or pattern[0] == '.':
                return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)
            else:
                return self.match(s, pattern[2:])
        else:
            if pattern[0] == s[0] or pattern[0] == '.':
                return self.match(s[1:], pattern[1:])
            else:
                return False

    def FirstAppearingOnce(self):
        """
        54. 请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
        当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
        当当前字符流没有存在出现一次的字符是返回“#”
        :return:
        """
        for i in self.s:
            if self.hash[ord(i)] == 1:
                return i
        return '#'

    def Insert(self, char):
        # python 中将字符转换成ASCII码用ord(ch)
        # ASCII转换成字符用chr
        self.s += char
        self.hash[ord(char)] += 1
        print(ord(char))

    def isNumeric(self, s):
        # 53.请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
        # 例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
        # 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
        sign, point, hasE = False, False, False
        for i in range(len(s)):
            if s[i].lower() == 'e':
                if hasE: return False
                if i == len(s) - 1: return False
                hasE = True
            elif s[i] == '+' or s[i] == '-':
                if sign and s[i - 1].lower() != 'e': return False
                if not sign and i > 0 and s[i - 1].lower() != 'e': return False
                sign = True
            elif s[i] == '.':
                if hasE or point: return False
                point = True
            elif ord(s[i]) < ord('0') or ord(s[i]) > ord('9'):
                return False
        return True

    def KMP1(self, pat, txt):
        m = len(pat)
        n = len(txt)
        for i in range(n-m+1):
            j = 0
            while j < m:
                if pat[j] != txt[i+j]:
                    break
                else:
                    j += 1
            if j == m:
                return i
        return -1




if __name__ == '__main__':
    solution = Solution()
    # print(solution.replaceSpace('We are Happy!'))
    print(solution.replaceSpace2('We are Happy!'))
    print(solution.replaceSpace3(['W', 'e', ' ', 'a', ' ', 'H']))
    res2 = solution.Permutation("abcbd")
    print("Permutation", len(res2), res2)
    res3 = solution.FirstNotRepeatingChar("abadfabdefaaac")
    print("FirstNotRepeatingChar: ", res3)
    res9 = solution.StrToInt('+123')
    print("StrToInt: ", res9)
    solution.Insert('g')
    print(solution.FirstAppearingOnce())
    solution.Insert('o')
    print(solution.FirstAppearingOnce())
    solution.Insert('o')
    print(solution.FirstAppearingOnce())
    solution.Insert('g')
    print(solution.FirstAppearingOnce())
    solution.Insert('l')
    print(solution.FirstAppearingOnce())
    solution.Insert('e')
    print(solution.FirstAppearingOnce())

    print(solution.Permutation2('abc'))

    res44 = solution.ReverseSentence("student. a am I")
    print("ReverseSentence", res44)
    print("KMP1", solution.KMP1('abc', 'fjafafabceabc'))

    res66 = solution.FirstNotRepeatingChar3("aabcceff")
    print(res66)




