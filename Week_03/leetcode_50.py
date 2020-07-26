# -*- coding: utf-8 -*- 

"""
@Time   : 2020/7/25 14:26
@File   : leetcode_50.py
@Author : 15769162764@163.com



50. Pow(x, n)
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25




1 暴力求解


"""


class Solution01:
    """

    1 暴力求解


    timeout

    """

    def myPow(self, x: float, n: int) -> float:

        result = 1

        x, n = self.convert_n(x, n)

        for i in range(0, n):
            result *= x

        return result

    def convert_n(self, x, n):
        """
        当 n 为负数的时候 进行 处理

        :param x:
        :param n:
        :return:
        """

        if n < 0:
            x = 1 / x
            n = -n

        return x, n


class Solution02:
    """

    二分思想 递归，复杂度是对数级的。

    AC

    """

    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1
        if n == 1:
            return x

        if n == -1:
            return 1 / x

        half = self.myPow(x, n // 2)
        rest = self.myPow(x, n % 2)

        return rest * half * half


class Solution:
    """

    递归 + 分治 思想


    分治 思想


    1 terminator
    2 process  current logic  (split your problem)
    3 drill down  (sub problem) , merge sub result
    4 reverse  current level states



    """

    def myPow(self, x: float, n: int) -> float:

        x, n = self.convert_n(x, n)

        return self.fast_pow(x, n)

    def convert_n(self, x, n):
        """
        当 n 为负数的时候 进行 处理

        :param x:
        :param n:
        :return:
        """

        if n < 0:
            x = 1 / x
            n = -n

        return x, n

    def fast_pow(self, x, n):

        if n == 0:
            return 1.0

        if n == 1:
            return x

        half = self.fast_pow(x, n // 2)

        if n % 2 == 0:
            return half * half
        else:
            return half * half * x


if __name__ == '__main__':
    x, n = 2, 6
    # x, n = 2, -2
    r = Solution().myPow(x, n)

    print(r)
    pass
