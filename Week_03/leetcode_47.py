# -*- coding: utf-8 -*- 

"""
@Time   : 2020/7/28 23:19
@File   : leetcode_47.py
@Author : 15769162764@163.com

47. 全排列 II
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]


https://leetcode-cn.com/problems/permutations-ii/

"""

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        self.result = []
        if not nums:
            return self.result

        length = len(nums)
        cur_result = []
        used = [0] * length
        level = 0

        # 先排序 方便剪枝
        nums.sort()
        self._generate_permute(nums, length, level, cur_result, used)
        return self.result

    def _generate_permute(self, nums: List[int], length: int, level: int, cur_result: List, used: List):

        if level == length:
            self.result.append(cur_result[:])
            return

        # process current level
        # drill down
        for i in range(0, length):
            if used[i]:
                continue

            #  在回退的过程中 被撤销了选择
            # 剪枝条件：i > 0 是为了保证 nums[i - 1] 有意义
            #  写 !used[i - 1] 是因为 nums[i - 1] 在深度优先遍历的过程中刚刚被撤销选择
            if i > 0 and nums[i] == nums[i - 1] and bool(used[i - 1]) is False:
                continue

            cur_result.append(nums[i])
            used[i] = True

            self._generate_permute(nums, length, level + 1, cur_result, used)

            # reverse current states
            used[i] = False
            cur_result.pop(-1)


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2]
    r = Solution().permuteUnique(nums)
    for item in r:
        print(item)
    # print(r)
    pass
