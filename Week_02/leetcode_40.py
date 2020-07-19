# -*- coding: utf-8 -*- 

"""
@Time   : 2020/7/19 17:23
@File   : leetcode_40.py
@Author : 15769162764@163.com



剑指 Offer 40. 最小的k个数
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。



示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]


限制：

0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000





 https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/

1 方法一 直接调用库 函数
2 自己 使用堆 来实现
3 排序数组,取前k 个就可以了


"""
from typing import List
from heapq import nsmallest, heappush, heappop


class Solution01:
    """
    调用 库函数
    """
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        r = nsmallest(n=k, iterable=arr)

        return r


class Solution02:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]

class Solution:
    """
    使用heapq 来实现 模拟 堆操作
    """
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:

        h = []
        if k == 0:
            return h

        for num in arr:
            if len(h) < k:
                heappush(h, num * -1)
            elif len(h) > 0 and num < (h[0] * -1):
                heappop(h)
                heappush(h, num * -1)

        result = [heappop(h) * -1 for i in range(k)]

        return result


if __name__ == '__main__':
    # arr = [3, 2, 1]
    # k = 2

    # arr = [0, 1, 2, 1]
    # k = 1
    arr = [0, 0, 0, 2, 0, 5]
    k = 0
    r = Solution().getLeastNumbers(arr, k)
    print(r)
    pass



if __name__ == '__main__':
    pass