# -*- coding: utf-8 -*- 

"""
@Time   : 2020/7/28 23:11
@File   : leetcode_77.py
@Author : 15769162764@163.com




77. 组合
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
通过次数63,714提交次数85,717

https://leetcode-cn.com/problems/combinations/




1 解法1  递归实现
2  优化版 ，提前判断一些没有必要的递归 计算

"""
from typing import List


class Solution01:
    """
    递归
    """

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.result = []

        # bound check
        if n <= 0 or k <= 0 or k > n:
            return self.result

        level = 0
        cur_result = []
        # 这里从 1 开始
        start = 1

        self._generate(n, k, level, start, cur_result)
        return self.result

    def _generate(self, n, k, level: int, start: int, cur_result: List):

        if level == k:
            self.result.append(cur_result.copy())
            return

        # process current loggic
        # drill down
        for i in range(start, n + 1):
            cur_result.append(i)
            # 注意这里是 start = i +1
            self._generate(n, k, level + 1, i + 1, cur_result)

            # reverse states if necessary
            cur_result.pop(-1)


class Solution:
    """
    递归 +  分支 优化，去掉不需要 递归条件

     剪枝优化版本：

    """

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.result = []

        # bound check
        if n <= 0 or k <= 0 or k > n:
            return self.result

        level = 0
        cur_result = []
        begin = 1

        self._generate(n, k, level, begin, cur_result)
        return self.result

    def _generate(self, n, k, level: int, begin: int, cur_result: List):
        # terminator
        if level == k:
            self.result.append(cur_result.copy())
            return

        # process current loggic
        # drill down
        end = n - (k - len(cur_result)) + 1
        # print(f"begin={begin}, end={end}, [begin:end]")
        for i in range(begin, end + 1):
            cur_result.append(i)
            self._generate(n, k, level + 1, i + 1, cur_result)

            # reverse states if necessary
            cur_result.pop(-1)


if __name__ == '__main__':
    r = Solution().combine(n=4, k=2)
    for item in r:
        print(item)
    # print(r)
    pass

if __name__ == '__main__':
    pass
