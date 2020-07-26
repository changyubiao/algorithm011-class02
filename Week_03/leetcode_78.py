# -*- coding: utf-8 -*- 

"""
@Time   : 2020/7/25 15:04
@File   : leetcode_78.py
@Author : 15769162764@163.com


78. 子集
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]


https://leetcode-cn.com/problems/subsets/solution/zi-ji-by-leetcode/

解法1 : 比较神奇

解法2 : 分支 ,递归思想



"""
from typing import List


class Solution01:
    """

    解法 比较神奇 ,
    https://leetcode-cn.com/problems/subsets/solution/zi-ji-by-leetcode/
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            result += [curr + [num] for curr in result]

        return result


class Solution02:
    """


    1 terminator
    2 process  current logic  (split your problem)
    3 drill down  (sub problem) , merge sub result
    4 reverse  current level states



    分治 思想

    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        current_result = []
        if not nums:
            return answer

        self.helper(answer, nums, current_result, 0)
        return answer

    def helper(self, answer: List, nums: List[int], current_result: List[int], level: int):
        length = len(nums)

        # terminator
        if level == length:
            answer.append(current_result.copy())
            return

        # not pick  the number
        self.helper(answer, nums, current_result, level + 1)

        # pick the number
        current_result.append(nums[level])
        self.helper(answer, nums, current_result, level + 1)

        # reverse states
        current_result.pop(-1)


class Solution:
    """


    1 terminator
    2 process  current logic  (split your problem)
    3 drill down  (sub problem) , merge sub result
    4 reverse  current level states



    分治 思想

    修改了一下 递归函数

    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.answer = []
        current_result = []
        if not nums:
            return self.answer

        self.helper(nums, current_result, 0)
        return self.answer

    def helper(self, nums: List[int], current_result: List[int], level: int):
        length = len(nums)

        # terminator
        if level == length:
            self.answer.append(current_result.copy())
            return

        # not pick  the number
        self.helper(nums, current_result, level + 1)

        # pick the number
        current_result.append(nums[level])
        self.helper(nums, current_result, level + 1)

        # reverse states
        current_result.pop(-1)


if __name__ == '__main__':
    nums = [1, 2, 3]
    r = Solution().subsets(nums=nums)
    print(r)

    real_result = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

    # assert r == real_result
    pass
