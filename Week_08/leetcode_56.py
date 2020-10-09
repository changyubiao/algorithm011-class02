"""
56. 合并区间
给出一个区间的集合，请合并所有重叠的区间。



示例 1:

输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].



示例 2:

输入: intervals = [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
注意：输入类型已于2019年4月15日更改。 请重置默认代码定义以获取新方法签名。

https://leetcode-cn.com/problems/merge-intervals/submissions/

"""

from typing import List


class Solution:
    """


    """

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals:
            return intervals

        # 按照起点排序
        intervals.sort(key=lambda e: e[0])

        # 先把第一个放入结果集中
        res = [intervals[0]]

        for i in range(1, len(intervals), 1):
            cur = intervals[i]
            # 每次新遍历到的列表与当前结果集中的最后一个区间的末尾端点进行比较
            peek = res[-1]

            if cur[0] > peek[1]:
                res.append(cur)
            else:
                peek[1] = max(cur[1], peek[1])

        return res


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

    r = Solution().merge(intervals)
    print(r)
