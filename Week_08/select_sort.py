import random


class Solution:

    def select_sort(self, nums):

        length = len(nums)
        for i, item in enumerate(nums):
            min_index = i
            for j in range(i + 1, length):

                if nums[j] < nums[min_index]:
                    min_index = j

            if min_index != i:
                nums[i], nums[min_index] = nums[min_index], nums[i]


if __name__ == '__main__':
    times = 100
    for i in range(times):
        array = list(range(20))
        array.sort()
        sorted_arr = array.copy()

        random.shuffle(array)

        # print(array)
        r = Solution().select_sort(array)

        assert sorted_arr == array
        print(f"{i} assert True")
