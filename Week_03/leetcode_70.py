# -*- coding: utf-8 -*- 

"""
@Time   : 2020/7/19 20:16
@File   : leetcode_70.py
@Author : 15769162764@163.com


70. 爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶



https://leetcode-cn.com/problems/climbing-stairs/

"""


class Solution:


    def climbStairs(self, n: int) -> int:
        """
        直接递归

        :param n:
        :return:
        """
        if n <= 2:
            return n

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)



class Solution01:

    def climbStairs(self, n: int) -> int:
        """
        动态规划的方法

        :param n:
        :return:
        """

        if n <= 2:
            return n

        dp = [None] * (n + 1)

        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


class Solution02:

    def climbStairs(self, n: int) -> int:
        """
        递归 方法
        :param n:
        :return:
        """

        if n <= 2:
            return n

        f1, f2, f3 = 1, 2, 0

        for i in range(3, n + 1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3

        return f3


if __name__ == '__main__':
    n = 5
    r = Solution().climbStairs(n=n)
    print(r)

    r = Solution01().climbStairs(n=n)
    print(r)


    r = Solution02().climbStairs(n=n)
    print(r)


    pass
