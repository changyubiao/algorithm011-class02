"""

https://leetcode-cn.com/problems/number-of-1-bits/

191. 位1的个数
编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。



示例 1：

输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。

"""


class Solution:
    def hammingWeight(self, n: int) -> int:

        string = bin(n)[2:]
        count = 0
        for char in string:
            if char == '1':
                count += 1

        return count
        pass


if __name__ == '__main__':

    r = Solution().hammingWeight(n=31)
    print(r)
