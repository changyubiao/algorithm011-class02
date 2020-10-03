from heapq import heappush, heappop
from typing import List

from random import shuffle


class Solution:

    def heapsort(self, array: List):
        heap = []
        for item in array:
            heappush(heap, item)

        # 原地修改数组
        array[:] = [heappop(heap) for _ in range(len(heap))]


if __name__ == '__main__':
    times = 10000
    for i in range(times):
        array = list(range(20))

        array.sort()
        sorted_arr = array.copy()

        shuffle(array)

        # print(array)
        Solution().heapsort(array)

        assert sorted_arr == array
        print(f"{i} assert True")