class Solution:
    """
    1. 请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
    思路：1.直接用string的replace方法
    2. 用一个新的的数组，对原理的数组判断
    """
    def replaceSpace(self, s):
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

    def Permutation(self, ss):

        if len(ss) <= 1:
            return ss
        res = set()
        for i in range(len(ss)):
            for j in self.Permutation(ss[:i] + ss[i+1:]):
                res.add(ss[i] + j)
        return sorted(res)

    def FirstNotRepeatingChar(self, s):
        """
        3. 在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
        idea: 暴力判断
        :param s:
        :return:
        """
        if len(s) > 10000 or len(s) <= 0:
            return -1
        for i in s:
            if s.count(i) == 1:
                return s.index(i)


if __name__ == '__main__':
    solution = Solution()
    # print(solution.replaceSpace('We are Happy!'))
    print(solution.replaceSpace2('We are Happy!'))
    res2 = solution.Permutation("abcbd")
    print("Permutation", len(res2), res2)
    res3 = solution.FirstNotRepeatingChar("abadfabdefaaac")
    print("FirstNotRepeatingChar: ", res3)
