# -*- coding: utf-8 -*- 

"""
@Time   : 2020/7/19 16:53
@File   : leetcode_347.py
@Author : 15769162764@163.com


347. 前 K 个高频元素
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。



示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]


https://leetcode-cn.com/problems/top-k-frequent-elements/
"""
from typing import List

from collections import defaultdict, Counter
from heapq import heappop, heappush


class Solution01:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """

        速度 还可以
        :param nums:
        :param k:
        :return:
        """

        result = []
        h = []
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1

        for num, count in counter.items():
            # 构建一个大顶堆 来实现,把 次数 * -1 放入堆中.
            heappush(h, (-count, num))

        for i in range(k):
            t = heappop(h)
            result.append(t[1])

        return result


class Solution:
    """

    使用Counter  效率有点低
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pass

        result = []
        h = []
        counter = Counter(nums)

        for num, count in counter.items():
            # 构建一个大顶堆 来实现,把 次数 * -1 放入堆中.
            heappush(h, (-count, num))

        for i in range(k):
            t = heappop(h)
            result.append(t[1])

        return result


if __name__ == '__main__':
    # nums = [1,2,2,3,4,4,5,2,1,1,1,1,1,4,4,4,4,2,2]

    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    r = Solution().topKFrequent(nums=nums, k=k)

    print(r)
    pass
