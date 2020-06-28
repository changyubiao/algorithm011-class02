# -*- coding: utf-8 -*- 

"""
@Time   : 2020/7/1 07:18
@File   : leetcode_26.py
@Author : 15769162764@163.com

26. 删除排序数组中的重复项
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。



示例 1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。



https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        这里借助了 set 的空间 空间复杂度 为 O(不重复的个数)
        :param nums:
        :return:
        """
        result = set()
        j = 0
        for i, num in enumerate(nums):

            if num not in result:
                result.add(num)
                nums[j] = num
                j += 1

        return j


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4,5,5,5,5]

    r = Solution().removeDuplicates(nums=nums)
    print(r)
    print(nums[0:r])
    print(nums)

    pass
