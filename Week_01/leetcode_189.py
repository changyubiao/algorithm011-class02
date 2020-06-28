# -*- coding: utf-8 -*- 

"""
@Time   : 2020/6/28 19:52
@File   : leetcode_189.py
@Author : 15769162764@163.com

给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释:
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""

from typing import List


class Solution01:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.


        时间复杂度 太高

        """
        last_index = len(nums) - 1

        for j in range(k):
            # print(f"j={j}")
            temp = nums[last_index]

            for i in range(last_index - 1, -1, -1):
                # print(i)
                nums[i + 1] = nums[i]

            nums[0] = temp


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.


        三次旋转法
        k = 4
        分为三步：
        反转整体，[7, 6, 5, 4, 3, 2, 1]
        反转第一段，[4,5,6,7,  3,2,1]
        反转第二段，[4,5,6,7,  1,2,3]


        或者
        先反转  第一部分
        先反转  第二部分
        最后反转  整体

        """

        length = len(nums)
        k = k % length
        # 自己先 reverse 一下
        self.reverse(nums, 0, length - 1)

        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, length - 1)
        # print(f" in function : {nums}")

    def reverse(self, nums, l, r):
        """
        要求 l<r  在 [l,r] 区间 进行交换,reverse
        :param l: left
        :param r: right
        :return:
        """
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l = l + 1
            r = r - 1


if __name__ == '__main__':
    # nums = [1, 2, 3, 4, 5, 6, 7]
    # k = 4

    nums = [-1]
    k = 2
    r = Solution().rotate(nums=nums, k=k)

    print(nums)

    # print(r)
    pass
