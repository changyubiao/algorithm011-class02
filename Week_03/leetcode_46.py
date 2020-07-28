# -*- coding: utf-8 -*- 

"""
@Time   : 2020/7/28 23:16
@File   : leetcode_46.py
@Author : 15769162764@163.com



46. 全排列
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
通过次数159,870提交次数208,763



https://leetcode-cn.com/problems/permutations

"""
from typing import List


class Solution01:
    """
    1 递归 实现

    """

    def permute(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return []

        self.result = []
        cur_result = []
        length = len(nums)

        self._generate_permute(nums, length, 0, cur_result)

        return self.result
        pass

    def _generate_permute(self, nums: List[int], length: int, level: int, cur_result: List):

        # terminator
        if level == len(nums):
            self.result.append(cur_result.copy())
            return

        # process current logic
        # drill down
        for num in nums:
            if num not in set(cur_result):
                cur_result.append(num)
                self._generate_permute(nums, length, level + 1, cur_result)

                # reverse states
                cur_result.pop()


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []

        if not nums:
            return self.result

        cur_result = []
        length = len(nums)

        #  代表 当前数字 有没有被使用过
        used = [None] * length

        self._generate_permute(nums, length, 0, cur_result, used)
        return self.result
        pass

    def _generate_permute(self, nums: List[int], length: int, level: int, cur_result: List, used: List):

        # terminator
        if level == len(nums):
            self.result.append(cur_result.copy())
            return

        # process current logic
        # drill down
        for i, num in enumerate(nums):

            if not used[i]:
                cur_result.append(num)
                used[i] = True
                self._generate_permute(nums, length, level + 1, cur_result, used)

                # reverse states
                used[i] = False
                cur_result.pop()


if __name__ == '__main__':
    nums = [1, 2, 3]
    r = Solution().permute(nums=nums)

    for item in r:
        print(item)
    # print(r)

    pass

if __name__ == '__main__':
    pass