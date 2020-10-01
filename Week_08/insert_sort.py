from typing import List

import random

"""
将一个记录插入到已排好序的序列中，从而得到一个新的有序序列（将序列的第一个数据看成是一个有序的子序列，

然后从第二个记录逐个向该有序的子序列进行有序的插入，直至整个序列有序）





https://www.cnblogs.com/onepixel/p/7674659.html

"""


class Solution01:

    def insert_sort(self, array):
        """

        :param array:
        :return:
        """
        # 遍历数组中的所有元素，其中0号索引元素默认已排序，因此从1开始
        # i  为待排序列下标，从下标1开始取值，默认下标0是排好的。
        for i in range(1, len(array)):
            # 将该元素与已排序好的前序数组依次比较，如果该元素小，则交换
            # range(i-1,-1,-1):从i-1倒序循环到0  i-1 --> 0
            k = i
            temp = array[k]
            for j in range(i - 1, -1, -1):
                # 判断：如果符合条件则交换
                if array[j] > temp:
                    # 元素往后移动，k 用来记录带插入位置
                    array[j + 1] = array[j]
                    k = j
            # 元素插入到正确位置
            array[k] = temp
        return array


class Solution:

    def insert_sort(self, array:List):
        """

        :param array:
        :return:
        """
        length = len(array)

        for i in range(1, length):

            pre_index = i - 1
            current = array[i]

            while pre_index >= 0 and array[pre_index] > current:
                array[pre_index + 1] = array[pre_index]
                pre_index -= 1

            array[pre_index + 1] = current

        return array


if __name__ == '__main__':
    times = 1000
    for i in range(times):
        array = list(range(20))
        array.sort()
        sorted_arr = array.copy()

        random.shuffle(array)

        # print(array)
        r = Solution().insert_sort(array)

        assert sorted_arr == r
        print(f"{i} assert True")
