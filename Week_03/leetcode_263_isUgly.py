# -*- coding: utf-8 -*- 

"""
@Time   : 2020/7/18 20:13
@File   : leetcode_isUgly.py
@Author : 15769162764@163.com


263. 丑数
编写一个程序判断给定的数是否为丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。

示例 1:

输入: 6
输出: true
解释: 6 = 2 × 3
示例 2:

输入: 8
输出: true
解释: 8 = 2 × 2 × 2
示例 3:

输入: 14
输出: false
解释: 14 不是丑数，因为它包含了另外一个质因数 7。


解法1  直接除 2 3  5 最后如果num==1 就是丑数 否则不是 .

Solution01 和 Solution  几乎是一样的方法 .

https://leetcode-cn.com/problems/ugly-number/submissions/

"""


class Solution01:
    def isUgly(self, num: int) -> bool:

        if num <= 0:
            return False

        while num % 5 == 0:
            num = num / 5

        while num % 3 == 0:
            num = num / 3
        while num % 2 == 0:
            num = num / 2

        return 1 == num


class Solution:

    def isUgly(self, num: int) -> bool:

        if num <= 0:
            return False

        factors = [2, 3, 5]

        for i in factors:

            while num % i == 0:
                num = num / i

        return 1 == num


if __name__ == '__main__':
    r = Solution().isUgly(num=17)
    print(r)
    pass
