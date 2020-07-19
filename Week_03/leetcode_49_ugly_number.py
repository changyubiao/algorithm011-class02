# -*- coding: utf-8 -*- 

"""
@Time   : 2020/7/18 18:30
@File   : leetcode_ugly_number.py
@Author : 15769162764@163.com


剑指 Offer 49. 丑数
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。



示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:

1 是丑数。
n 不超过1690。




#解法1 解法使用堆这种数据结构,+ set 用来去重

reference:

https://leetcode-cn.com/problems/chou-shu-lcof/solution/li-yong-xiao-gen-dui-wan-mei-jie-jue-by-yanshaojia/




解法2  动态规划
    https://leetcode-cn.com/problems/chou-shu-lcof/solution/mian-shi-ti-49-chou-shu-dong-tai-gui-hua-qing-xi-t/


"""

from heapq import heappop, heappush


class Solution01:

    def nthUglyNumber(self, n: int) -> int:

        h = []
        ugly_number = [2, 3, 5]

        heappush(h, 1)
        num_set = {1}

        # 记录出堆的个数，出堆的元素完全按照从小到大排序
        count = 0

        while h:
            # 获取当前堆顶元素
            current = heappop(h)
            count += 1
            if count >= n:
                return current

            for num in ugly_number:
                next_ugly = num * current
                if next_ugly not in num_set:
                    num_set.add(next_ugly)
                    heappush(h, next_ugly)


class Solution:
    """

    动态规划
    """

    def nthUglyNumber(self, n: int) -> int:

        # dp记录 所有的丑数
        dp, a, b, c = [1] * n, 0, 0, 0

        for i in range(1, n):
            n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            # 当前第i个丑数,这三个中的最小值
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2:
                a += 1
            if dp[i] == n3:
                b += 1
            if dp[i] == n5:
                c += 1

        return dp[-1]


if __name__ == '__main__':

    # 1 2 3 4 5

    for n in range(17, 18):
        r = Solution().nthUglyNumber(n=n)

        print(r, end=' ')
    pass
