"""

231. 2的幂
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:

输入: 1
输出: true
解释: 20 = 1
示例 2:

输入: 16
输出: true
解释: 24 = 16
示例 3:

输入: 218
输出: false

https://leetcode-cn.com/problems/power-of-two/


# todo 位运算 来解决 这个题目

"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n == 0:
            return False

        while n % 2 == 0:
            n /= 2
        return n == 1


if __name__ == '__main__':
    r = Solution().isPowerOfTwo(n=16)
    print(r)
