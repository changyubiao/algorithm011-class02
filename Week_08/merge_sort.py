import random
from typing import List


"""
meger sort 归并 排序 

"""


class Solution:

    def mergesort(self, array: List, left, right):
        if right <= left:
            return
        mid = (left + right) // 2
        self.mergesort(array, left, mid)
        self.mergesort(array, mid + 1, right)
        self.merge(array, left, mid, right)

    def merge(self, array: List, left: int, mid: int, right: int):
        # 中间数组
        tmp = [None] * (right - left + 1)
        i = left
        j = mid + 1
        k = 0

        while i <= mid and j <= right:
            if array[i] < array[j]:
                tmp[k] = array[i]
                i += 1
            else:
                tmp[k] = array[j]
                j += 1
            k += 1

        while i <= mid:
            tmp[k] = array[i]
            k += 1
            i += 1

        while j <= right:
            tmp[k] = array[j]
            k += 1
            j += 1

        array[left:right + 1] = tmp


class Solution02:

    def mergesort(self, nums, left, right):
        if right <= left:
            return
        #  右移运算符 等于 // 2
        mid = (left + right) >> 1
        self.mergesort(nums, left, mid)
        self.mergesort(nums, mid + 1, right)
        self.merge(nums, left, mid, right)

    def merge(self, nums, left, mid, right):
        temp = []
        i = left
        j = mid + 1
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
        while i <= mid:
            temp.append(nums[i])
            i += 1
        while j <= right:
            temp.append(nums[j])
            j += 1
        nums[left:right + 1] = temp


if __name__ == '__main__':
    times = 1000
    for i in range(times):
        array = list(range(200))

        array.sort()
        sorted_arr = array.copy()

        left, right = 0, len(array) - 1

        random.shuffle(array)

        r = Solution().mergesort(array, left, right)

        assert sorted_arr == array
        print(f"{i} assert True")
