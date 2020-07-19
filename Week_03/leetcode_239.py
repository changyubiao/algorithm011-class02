# -*- coding: utf-8 -*- 

"""
@Time   : 2020/7/2 07:01
@File   : leetcode_239.py
@Author : 15769162764@163.com



239. 滑动窗口最大值
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。



进阶：

你能在线性时间复杂度内解决此题吗？



示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7



https://leetcode-cn.com/problems/sliding-window-maximum/

"""
from typing import List

from collections import deque


class MyDeque(deque):

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

    def empty(self):
        """
        判断当前队列是否为空
        :return:
        """
        return len(self) == 0

    def size(self):
        """
        返回当前队列元素的数量
        :return:
        """
        return len(self)

    def right(self):
        """
        查看最右边的元素
        :return:
        """
        return self[-1]

    def left(self):
        """
        查看最左边的元素
        :return:
        """
        return self[0]


class MonotonicQueue:

    def __init__(self, maxlen=None):
        self.data = MyDeque(maxlen=maxlen)

    def push(self, num):
        while (not self.data.empty()) and self.data.right() < num:
            """
            调队列的 push 方法依然在队尾添加元素，
            但是要把前面比新元素小的元素都删掉
            """
            self.data.pop()

        self.data.append(num)

    def pop(self, n: int):
        """
         队头元素如果是 n，删除它
        :param n:
        :return:
        这里不是直接pop ,要
        要判断 data.front() == n，是因为我们想删除的队头元素 n 可能已经被「压扁」了, 被之前 push  的时候 删除了.

        """
        if not self.data.empty() and self.data.left() == n:
            self.data.popleft()

    def max(self):
        """
        查看队列的最大值
        :return:
        """
        return self.data.left()


class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        """
        :param nums:
        :param k:
        :return:
        """

        q = MonotonicQueue()
        result = []
        length = len(nums)
        for i in range(0, length, 1):
            q.push(nums[i])
            if i - k + 1 >= 0:
                result.append(q.max())
                #  滑动窗口 最左边的元素
                q.pop(nums[i - k + 1])

        return result


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    # nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    r = Solution().maxSlidingWindow(nums=nums, k=3)

    print(r)
    pass
