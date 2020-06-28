# -*- coding: utf-8 -*- 

"""
@Time   : 2020/6/28 21:46
@File   : two_sum.py
@Author : 15769162764@163.com


1. 两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。



"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}

        for i, num in enumerate(nums):

            if (target - num) in hash_map:
                second = hash_map.get(target - num)

                return [i, second]

            hash_map[num] = i


if __name__ == '__main__':
    pass
