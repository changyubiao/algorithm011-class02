# -*- coding: utf-8 -*- 

"""
@Time   : 2020/7/6 20:26
@File   : leetcode_42.py
@Author : 15769162764@163.com

42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



int trap(vector<int>& height)
{
    int ans = 0;
    int size = height.size();
    for (int i = 1; i < size - 1; i++) {
        int max_left = 0, max_right = 0;
        for (int j = i; j >= 0; j--) { //Search the left part for max bar size
            max_left = max(max_left, height[j]);
        }
        for (int j = i; j < size; j++) { //Search the right part for max bar size
            max_right = max(max_right, height[j]);
        }
        ans += min(max_left, max_right) - height[i];
    }
    return ans;
}

作者：LeetCode
链接：https://leetcode-cn.com/problems/trapping-rain-water/solution/jie-yu-shui-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""
from typing import List


class Solution:

    def trap(self, height: List[int]) -> int:

        """

        暴力解法

        timeout

        https://leetcode-cn.com/problems/trapping-rain-water/solution/jie-yu-shui-by-leetcode/
        :param height:
        :return:
        """
        result = 0

        size = len(height)

        for i in range(1, size - 1, 1):

            max_left, max_right = 0, 0

            j = i
            while j >= 0:
                max_left = max(max_left, height[j])
                j -= 1

            j = i
            while j < size:
                max_right = max(max_right, height[j])

                j += 1

            result += min(max_left, max_right) - height[i]

        return result

        pass


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

    r = Solution().trap(height=height)

    print(r)

    pass
