# -*- coding: utf-8 -*- 

"""
@Time   : 2020/6/28 22:02
@File   : letcode_88.py
@Author : 15769162764@163.com


给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

 

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
 



说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
 

示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


有点难度  看题解 才搞定的,  之后再看下

"""
from typing import List


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.

        #todo  还有点问题 .... 待处理

        """

        nums1_copy = nums1[0:m]

        # 保留空间
        nums1[:] = []

        p, q = 0, 0

        while p < m and q < n:

            if nums1_copy[p] < nums2[q]:
                nums1.append(nums1_copy[p])
                p = p + 1
            else:
                nums1.append(nums2[q])
                q = q + 1

        if p < m:
            nums1[p + q:] = nums1_copy[p:]

        if q < n:
            nums1[p + q:] = nums2[q:]

        # print(nums1)


if __name__ == '__main__':


    nums1 = [1,2,3,0,0,0]
    m = 3

    nums2 = [2,5,6]
    n = 3
    r = Solution().merge(nums1,m,nums2,n)

    print(r)

    print(nums1)
    pass
