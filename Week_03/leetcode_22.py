# -*- coding: utf-8 -*- 

"""
@Time   : 2020/7/19 20:25
@File   : leetcode_22.py
@Author : 15769162764@163.com

22. 括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。



示例：

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]




https://leetcode-cn.com/problems/generate-parentheses/

"""
from typing import List


class Solution01:
    def generateParenthesis(self, n: int) -> List[str]:
        self._generate(level=0, end=2 * n, r="")
        return []

        pass

    def _generate(self, level, end, r):
        """

        左括号 随时可以加, 只要不超过 n 即可,
        右括号 添加 是有条件的,   左括号的个数 > 右括号的个数.


        :param level:
        :param end:
        :param r:
        :return:
        """

        #  termainal
        if level >= end:
            # valid s 验证 s 的合法性
            print(r)
            return r

        # process current
        s1 = r + "("
        s2 = r + ")"

        # drill down , next level .
        self._generate(level=level + 1, end=end, r=s1)
        self._generate(level=level + 1, end=end, r=s2)

        # recurcisive  status
        pass


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self._generate(left=0, right=0, end=n, r="")

        return self.result

    def _generate(self, left, right, end, r):
        # terminal
        if left == end and right == end:
            # print(r)
            self.result.append(r)

        # drill down
        if left < end:
            # process
            r1 = r + "("
            self._generate(left + 1, right, end, r1)

        if left > right:
            r2 = r + ")"
            self._generate(left, right + 1, end, r2)


if __name__ == '__main__':
    r = Solution().generateParenthesis(n=2)

    print(r)
    pass
