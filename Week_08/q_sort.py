import random

from typing import List, Union

"""
quick sort  




"""


class Solution:
    def quick_sort(self, nums: List, begin, end):
        if begin >= end:
            return
        pivot_index = self.partition(nums, begin, end)
        self.quick_sort(nums, begin, pivot_index - 1)
        self.quick_sort(nums, pivot_index + 1, end)

    def partition(self, nums: List, begin, end) -> Union[int, None]:
        """
        partition 过程详解
        https://blog.csdn.net/u010339879/article/details/104079246


        在  [start,end] 的闭区间里 寻找一个 pivot


        pivot

        arr[begin ..piovt-1 ]  <= nums[begin]


        arr[pivot+1, ... end]  > nums[begin]


        :param nums:
        :param begin:
        :param end:
        :return:
        """

        j = begin - 1
        pivot_element = nums[begin]

        for i in range(begin, end + 1):
            if nums[i] <= pivot_element:
                j += 1
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]

        # pivot_element 放到正确的位置上， 所以要交换一下。j是找到正确的位置
        nums[j], nums[begin] = nums[begin], nums[j]
        return j

    def partition01(self, nums, begin, end) -> Union[int, None]:
        if end <= begin:
            return

        pivot = end
        counter = begin

        for i in range(begin, end):
            if nums[i] < nums[pivot]:
                nums[counter], nums[i] = nums[i], nums[counter]
                counter += 1

        nums[pivot], nums[counter] = nums[counter], nums[pivot]

        return counter

    def partition2(self, nums, begin, end):
        pivot = nums[begin]
        mark = begin
        for i in range(begin + 1, end + 1):
            if nums[i] < pivot:
                mark += 1
                nums[mark], nums[i] = nums[i], nums[mark]
        nums[begin], nums[mark] = nums[mark], nums[begin]
        return mark


if __name__ == '__main__':
    times = 10000
    for i in range(times):
        array = list(range(20))
        array.sort()
        sorted_arr = array.copy()

        random.shuffle(array)

        # print(array)
        r = Solution().quick_sort(array, 0, 19)

        assert sorted_arr == array
        print(f"{i} assert True")
