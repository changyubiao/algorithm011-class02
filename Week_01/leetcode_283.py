# -*- coding: utf-8 -*- 

"""
@Time   : 2020/6/28 22:53
@File   : leetcode_283.py
@Author : 15769162764@163.com


给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/move-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        j = 0
        for i, num in enumerate(nums):
            if num != 0:
                if i != j:
                    nums[j], nums[i] = nums[i], nums[j]
                j = j + 1


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]

    r = Solution().moveZeroes(nums=nums)

    print(nums)
    pass
