from typing import List

"""

493. 翻转对
给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。

你需要返回给定数组中的重要翻转对的数量。

示例 1:

输入: [1,3,2,3,1]
输出: 2
示例 2:

输入: [2,4,3,5,1]
输出: 3


https://leetcode-cn.com/problems/reverse-pairs/



"""


class Solution01:
    """
    暴力解法
    """

    def reversePairs(self, nums: List[int]) -> int:
        count = 0
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):

                if nums[i] > 2 * nums[j]:
                    count += 1

        return count


class Solution02:
    """

    """

    def reversePairs(self, nums: List[int]) -> int:

        return self.merge_sort(nums, 0, len(nums) - 1)

    def merge_sort(self, nums, start, end) -> int:
        if start >= end:
            return 0

        mid = start + (end - start) // 2
        cnt = self.merge_sort(nums, start, mid) + self.merge_sort(nums, mid + 1, end)

        j = mid + 1
        for i in range(start, mid + 1):
            # 统计逆序对
            while j <= end and (nums[i] / 2) > nums[j]:
                j += 1

            cnt += j - (mid + 1)

        # 排序这一段 数组
        nums[start:end + 1] = sorted(nums[start:end + 1])
        return cnt


class Solution03:
    """
    解法2  逻辑 更加清晰一些

    """

    def reversePairs(self, nums: List[int]) -> int:

        self.result = 0
        self.merge_sort(nums, 0, len(nums) - 1)
        return self.result

    def merge_sort(self, nums, left, right):

        if right <= left:
            return

        mid = left + (right - left) // 2

        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid + 1, right)

        # count elements
        count = 0
        r = mid + 1
        l = left

        while l <= mid:
            #  注意这里的条件
            if r > right or nums[l] <= 2 * nums[r]:
                l += 1
                self.result += count
            else:
                r += 1
                count += 1
        # sort
        nums[left:right + 1] = sorted(nums[left: right + 1])


class Solution:
    """
    解法4
    把 sort 的代码去掉， 自己排序， 不调用系统的函数 进行排序

    """

    def reversePairs(self, nums: List[int]) -> int:

        self.result = 0
        self.merge_sort(nums, 0, len(nums) - 1)
        return self.result

    def merge_sort(self, nums, left, right):

        if right <= left:
            return

        mid = left + (right - left) // 2

        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid + 1, right)

        # count elements
        count = 0
        r = mid + 1
        l = left

        while l <= mid:
            #  注意这里的条件
            if r > right or nums[l] <= 2 * nums[r]:
                l += 1
                self.result += count
            else:
                r += 1
                count += 1

        # merge sort
        self.my_sort(nums, left, right)


    def my_sort(self, nums, left, right):

        # merge sort
        cache = [None] * (right - left + 1)
        mid = left + (right - left) // 2

        i = left
        j = mid + 1
        k = 0

        while i <= mid and j <= right:
            if nums[i] < nums[j]:
                cache[k] = nums[i]
                i += 1
            else:
                cache[k] = nums[j]
                j += 1
            k += 1

        while i <= mid:
            cache[k] = nums[i]
            k += 1
            i += 1

        while j <= right:
            cache[k] = nums[j]
            k += 1
            j += 1

        nums[left:right + 1] = cache


if __name__ == '__main__':
    # nums = [1, 3, 2, 3, 1]
    nums = [1, 3, 2, 3, 1]
    # nums = [2, 4, 3, 5, 1]
    # r = Solution02().reversePairs(nums=nums)
    r = Solution02().reversePairs(nums=nums)

    print(r)
