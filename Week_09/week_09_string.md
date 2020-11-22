
[TOC]



这一部分主要是 字符串中的一些题目。



- leetcode_387 字符串中的第一个唯一字符
- leetcode 58. 最后一个单词的长度
- leetcode 654. 最大二叉树
- leetcode 709. 转换成小写字母
- leet code 344. 反转字符串
- leetcode 541 反转字符串 II
- leetcode_151 翻转字符串里的单词
- leetcode 1143. 最长公共子序列
- leetcode 771. 宝石与石头
- leetcode557 反转字符串中的单词 III
- leetcode 917. 仅仅反转字母
- leetcode 125 验证回文串
- leetcode 680 验证回文字符串 Ⅱ
- leetcode 5. 最长回文子串
- leetcode 242. 有效的字母异位词
- leetcode 49. 字母异位词分组
- leetcode 438. 找到字符串中所有字母异位词
- leetcode 14. 最长公共前缀





## leetcode_387 字符串中的第一个唯一字符

```
"""

387. 字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。



示例：

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2


"""

from collections import defaultdict

from collections import Counter


class Solution01:
    def firstUniqChar(self, s: str) -> int:
        #  统计每个单词出现频次
        hash_map = defaultdict(int)

        for idx, char in enumerate(s):
            hash_map[char] += 1

        for idx, char in enumerate(s):
            if char in hash_map:
                if hash_map[char] == 1:
                    return idx
        return -1


class Solution:
    """
    调用Counter 来实现计数
    """
    def firstUniqChar(self, s: str) -> int:
        #  统计每个单词出现频次

        counter = Counter(s)

        for idx, char in enumerate(s):
            if counter[char] == 1:
                return idx
        return -1


if __name__ == '__main__':
    # s = "leetcode"
    s = "loveleetcode"

    r = Solution().firstUniqChar(s=s)

    print(r)
```



## leetcode 58. 最后一个单词的长度

```
"""


58. 最后一个单词的长度
给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。



示例:

输入: "Hello World"
输出: 5

"A "   1
"ABC"    3

https://leetcode-cn.com/problems/length-of-last-word/

"""


class Solution:
    """
    # TODO 有 bug 待看
    """

    def lengthOfLastWord(self, s: str) -> int:
        length = len(s)
        if not s:
            return 0

        # 翻转字符串
        reversed_s = list(reversed(s))

        for i in range(len(reversed_s)):
            if reversed_s[i] == ' ':
                continue
            for j in range(i + 1, length):
                if reversed_s[j] == ' ':
                    # get result
                    return j - i
        return 0


class Solution:
    """
    从字符串末尾开始向前遍历，其中主要有两种情况
    第一种情况，以字符串"Hello World"为例，从后向前遍历直到遍历到头或者遇到空格为止，即为最后一个单词"World"的长度5
    第二种情况，以字符串"Hello World "为例，需要先将末尾的空格过滤掉，再进行第一种情况的操作，即认为最后一个单词为"World"，长度为5
    所以完整过程为先从后过滤掉空格找到单词尾部，再从尾部向前遍历，找到单词头部，最后两者相减，即为单词的长度
    时间复杂度：O(n)，n为结尾空格和结尾单词总体长度


    """

    def lengthOfLastWord(self, s: str) -> int:
        """
        从后面往前 扫描 字符串
        :param s:
        :return:
        """
        length = len(s)
        end = length - 1
        if not length:
            return 0

        while end >= 0 and s[end] == ' ':
            end -= 1

        if end < 0:
            return 0

        start = end
        while start >= 0 and s[start] != ' ':
            start -= 1

        return end - start


if __name__ == '__main__':
    s = "Hello World"
    # s ="a"
    # s = "     "

    r = Solution().lengthOfLastWord(s=s)
    print(r)

```




## leetcode 654. 最大二叉树
```
"""

654. 最大二叉树
给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：

二叉树的根是数组中的最大元素。
左子树是通过数组中最大值左边部分构造出的最大二叉树。
右子树是通过数组中最大值右边部分构造出的最大二叉树。
通过给定的数组构建最大二叉树，并且输出这个树的根节点。



示例 ：

输入：[3,2,1,6,0,5]
输出：返回下面这棵树的根节点：

      6
    /   \
   3     5
    \    /
     2  0
       \
        1



https://leetcode-cn.com/problems/maximum-binary-tree/

"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution01:
    """
    [left,right) 寻找 最值
    """
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:

        return self.bulid(nums, 0, len(nums))

    def bulid(self, nums, left, right):
        if left == right:
            return

        max_index = self.get_max_index(nums,left,right)

        root = TreeNode(nums[max_index])
        root.left = self.bulid(nums, left, max_index)
        root.right = self.bulid(nums, max_index+1, right)
        return root

    def get_max_index(self,nums,left,right):
        """
        返回最大值的索引
        :param nums:
        :param left:
        :param right:
        :return:
        """
        max_index = left
        for  i in range(left,right):
            if nums[max_index] < nums[i]:
                max_index = i
        return max_index


class Solution02:
    """
    [left,right] 寻找 最值
    """

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:

        return self.bulid(nums, 0, len(nums) - 1)

    def bulid(self, nums, left, right):
        if left > right:
            return

        max_index = self.get_max_index(nums, left, right)

        root = TreeNode(nums[max_index])
        root.left = self.bulid(nums, left, max_index - 1)
        root.right = self.bulid(nums, max_index + 1, right)
        return root

    def get_max_index(self, nums, left, right):
        """
        返回最大值的索引
        :param nums:
        :param left:
        :param right:
        :return:
        """
        max_index = left
        for i in range(left, right + 1):
            if nums[max_index] < nums[i]:
                max_index = i
        return max_index



class Solution:
    """
    [left,right] 寻找 最值
    """

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:

        return self.bulid(nums, 0, len(nums) - 1)

    def bulid(self, nums, left, right):
        if left > right:
            return

        # max_index = self.get_max_index(nums, left, right)
        max_value = -float('inf')
        # max_index = left
        for i in range(left, right + 1):
            if max_value < nums[i]:
                max_index = i
                max_value = nums[i]

        print(f"max_value:{max_value},index:{max_index}")

        root = TreeNode(nums[max_index])
        root.left = self.bulid(nums, left, max_index - 1)
        root.right = self.bulid(nums, max_index + 1, right)
        return root

    def __get_max_index(self, nums, left, right):
        """
        返回最大值的索引
        :param nums:
        :param left:
        :param right:
        :return:
        """
        max_index = left
        for i in range(left, right + 1):
            if nums[max_index] < nums[i]:
                max_index = i
        return max_index


```





## leetcode 709. 转换成小写字母

```
"""


709. 转换成小写字母
实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。



示例 1：

输入: "Hello"
输出: "hello"
示例 2：

输入: "here"
输出: "here"
示例 3：

输入: "LOVELY"
输出: "lovely"

https://leetcode-cn.com/problems/to-lower-case/

"""


class Solution01:
    def toLowerCase(self, str: str) -> str:
        return str.lower()


class Solution:
    """
    方法1：ASCCII码
    思路：
    通过 ASCII 码表操作字符串即可。
    a-z：97-122
    A-Z：65-90
    0-9：48-57

    ord(char)  转成 ascii 码
    chr(int)  转成对应字符

    """

    def toLowerCase(self, str: str) -> str:

        new_string = ""

        for char in str:
            if 'A' <= char <= 'Z':
                new_string += chr(ord(char) + 32)
            else:
                new_string += char
        return new_string


if __name__ == '__main__':
    r = Solution().toLowerCase(str="LOVeLY")
    print(r)
```




## leet code 344. 反转字符串


```
"""
344. 反转字符串
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

 
 

示例 1：

输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
示例 2：

输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]


https://leetcode-cn.com/problems/reverse-string/


"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1


if __name__ == '__main__':
    s = ['h', 'e', 'l', 'l', 'o']
    r = Solution().reverseString(s=s)
    print(r)
    print(s)

```




## leetcode 541 反转字符串 II

```
"""

541. 反转字符串 II
给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。

如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。


示例:

输入: s = "abcdefg", k = 2
输出: "bacdfeg"


提示：

该字符串只包含小写英文字母。
给定字符串的长度和 k 在 [1, 10000] 范围内。


"""
from typing import List


class Solution01:
    def reverseStr(self, s: str, k: int) -> str:
        length = len(s)
        s = list(s)
        for i in range(0, length, 2 * k):
            if i + k > length:
                end = length - 1
            else:
                end = i + k - 1
            self._reverse(s, start=i, end=end)

        return "".join(s)

    def _reverse(self, s: List, start: int, end: int) -> None:
        """
        s  在[start,end] 的闭区间 开始 reverse 字符串， 翻转字符串
        :param s:
        :param start:
        :param end:
        :return:
        """
        if start >= end:
            return

        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1


class Solution:
    """
    官方题解
    """

    def reverseStr(self, s, k):
        a = list(s)
        for i in range(0, len(a), 2 * k):
            # 这里不用担心 越界的问题，如果i+k 超出长度 会自动 到字符串的末尾
            a[i:i + k] = reversed(a[i:i + k])
        return "".join(a)


if __name__ == '__main__':
    # s = "abcdefg"
    s = "a"
    k = 2

    expect = "bacdfeg"

    r = Solution().reverseStr(s, k)
    print(r)
    # assert r == expect


```




## leetcode_151 翻转字符串里的单词

```
"""
151. 翻转字符串里的单词
给定一个字符串，逐个翻转字符串中的每个单词。

说明：

无空格字符构成一个 单词 。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。


示例 1：

输入："the sky is blue"
输出："blue is sky the"
示例 2：

输入："  hello world!  "
输出："world! hello"
解释：输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例 3：

输入："a good   example"
输出："example good a"
解释：如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
示例 4：

输入：s = "  Bob    Loves  Alice   "
输出："Alice Loves Bob"


https://leetcode-cn.com/problems/reverse-words-in-a-string/



官方题解
https://leetcode-cn.com/problems/reverse-words-in-a-string/solution/fan-zhuan-zi-fu-chuan-li-de-dan-ci-by-leetcode-sol/
"""
from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()

        words = s.split()
        words = [w for w in words if w]

        length = len(words)

        self._reverse(words, start=0, end=length - 1)
        return " ".join(words)
        pass

    def _reverse(self, s: List, start: int, end: int) -> None:
        """
        s  在[start,end] 的闭区间 开始 reverse 字符串， 翻转字符串
        :param s:
        :param start:
        :param end:
        :return:
        """
        if start >= end:
            return

        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1


if __name__ == '__main__':
    s = "the sky is blue"
    expect = "blue is sky the"
    r = Solution().reverseWords(s=s)

    print(f"{r!r}")

```




## leetcode 1143. 最长公共子序列

题解  求最长公共子序列的长度 

先从 base case 考虑 
如果 有一个串 是空串 那结果 是就是 0 


- 空串的情况

s1=""
s2 = "xxxxxxx"
or   
s2=""
s1="xxxxxx"

- 还有一种情况 

s1 ="A"
s2="xxxxxAxxx"

s1 只有一个字符，只要看 s1 是否在s2 中 即可 


- 第二种情况
s1="xxxxxxA"
s2="xxxxxxxxxxA"
如果 s1 , s2 最后一个字符相同， 那么 结果一定在 
s1[0:-1],与s2[0:-1]的最长公共子序列 的值 +1


- 第三种情况

s1="xxxxxxA"
s2="xxxxxxxxxxB"

lcp(s1,s2) 的值 等于   lcp(s1[0:-1],s2) 和 lcp[s1,s2[0:-1]) 这两个 中其中 最大的那个值。 
这个是 递推的关键点，要想明白。 
即 s1 去掉最后一个字符 和s2 相比 看 最长公共子序列 
或者  s2 去掉最后一个字符 和 s1 相比， 看 最长公共子序列， 看看 这两个值  哪个值更大。


s1 ="ace"

s2 = "abcde"





|      | ""   |a      | c     |e      |
| ---- | ---- | ---- | ---- | ----    |
| ""   |  0    |    0  |  0 |  0      |
|  a   |  0    |    1  |  1 |  1      |
|  b   |  0    |    1  |  1 |  1      |
|  c   |  0    |    1  |  2 |  2      |
|  d   |  0    |    1  |  2 |  2      |
|  e   |  0    |    1  |2   |  3      |












```
"""
1143. 最长公共子序列
给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。

若这两个字符串没有公共子序列，则返回 0。



示例 1:

输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace"，它的长度为 3。
示例 2:

输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc"，它的长度为 3。
示例 3:

输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0。



https://leetcode-cn.com/problems/longest-common-subsequence/

"""


class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        if not text1 or not text2:
            return 0

        m = len(text1)
        n = len(text2)

        # 全部初始化为0
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):

            for j in range(1, n + 1):

                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]


if __name__ == '__main__':
    text1 = "abcde"
    text2 = "ace"

    r = Solution().longestCommonSubsequence(text1, text2)
    print((r))
    pass

```



## leetcode 771. 宝石与石头
```
"""

771. 宝石与石头
 给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。 S 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。

J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。

示例 1:

输入: J = "aA", S = "aAAbbbb"
输出: 3
示例 2:

输入: J = "z", S = "ZZ"
输出: 0
注意:

S 和 J 最多含有50个字母。
 J 中的字符不重复。


 https://leetcode-cn.com/problems/jewels-and-stones/
"""


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:

        stones = set(J)

        count = 0
        for char in S:
            if char in stones:
                count += 1

        return count


if __name__ == '__main__':
    J = "aA"
    S = "aAAbbbb"
    r = Solution().numJewelsInStones(J, S)

    print(r)

```



## leetcode557  反转字符串中的单词 III
```
"""

557. 反转字符串中的单词 III
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。


示例：

输入："Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"


提示：

在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。

https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/



字符串可变语言：

C/C++, Ruby, PHP, Swift

字符串不可变语言：

Java, Python, C#, Javascript, Go

"""


class Solution:

    def reverseWords(self, s: str) -> str:
        if not s:
            return s
        return ' '.join([w[::-1] for w in s.split(' ')])


if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    r = Solution().reverseWords(s=s)
    print(r)
    print(s)


```




## leetcode 917. 仅仅反转字母

```

"""
917. 仅仅反转字母
给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。

示例 1：
输入："ab-cd"
输出："dc-ba"

示例 2：
输入："a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"
示例 3：

输入："Test1ng-Leet=code-Q!"
输出："Qedo1ct-eeLg=ntse-T!"

https://leetcode-cn.com/problems/reverse-only-letters/solution/jin-jin-fan-zhuan-zi-mu-by-leetcode/
"""


class Solution01:
    """
    字母栈

    将 s 中的所有字母单独存入栈中，所以出栈等价于对字母反序操作。（或者，可以用数组存储字母并反序数组。）

    然后，遍历 s 的所有字符，如果是字母我们就选择栈顶元素输出。

    链接：https://leetcode-cn.com/problems/reverse-only-letters/solution/jin-jin-fan-zhuan-zi-mu-by-leetcode/
    """

    def reverseOnlyLetters(self, S: str) -> str:
        letters = [c for c in S if c.isalpha()]
        ans = []
        for c in S:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return "".join(ans)


class Solution:
    """
    双指针法 
    """

    def reverseOnlyLetters(self, S: str) -> str:

        i, j = 0, len(S) - 1

        s = list(S)
        while i < j:
            if s[i].isalpha() and s[j].isalpha():
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif not s[i].isalpha():
                i += 1
            elif not s[j].isalpha():
                j -= 1
        return "".join(s)


if __name__ == '__main__':
    S = "a-bC-dEf-ghIj"
    expect = "j-Ih-gfE-dCba"
    r = Solution().reverseOnlyLetters(S)
    # print(S)
    # print(r)
    assert r == expect
    pass


```





## leetcode 125 验证回文串
```python 


# -*- coding: utf-8 -*- 

"""
@Time   : 2020/6/23 05:52
@File   : leetcode_125.py
@Author : 15769162764@163.com

自顶向下 的  思考方式

要有  自顶向下 的思考方式



125. 验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false


https://leetcode-cn.com/problems/valid-palindrome/

"""

import re

import string


class Solution01:
    def isPalindrome(self, s: str) -> bool:
        s = self.filter_alpha_number(s)
        flag = self.compare_ignorecase(s, s[::-1])

        return flag

    @staticmethod
    def compare_ignorecase(s1, s2):
        """
        比较两个字符串 忽略大小写
        :param s1:
        :param s2:
        :return:
        """
        return s1.lower() == s2.lower()

    @staticmethod
    def filter_alpha_number(s):
        alpha_number = set(string.ascii_lowercase + string.ascii_uppercase + string.digits)

        return ''.join(filter(lambda x: x in alpha_number, s))


class Solution:

    def isPalindrome(self, s: str) -> bool:

        # 过滤有效的字符
        s = self.filter_alpha_number(s)

        length = len(s)

        i, j = 0, length - 1

        while i < j:

            if s[i].upper() != s[j].upper():
                return False
            i += 1
            j -= 1

        return True

    @staticmethod
    def filter_alpha_number(s):

        alpha_number = set(string.ascii_lowercase + string.ascii_uppercase + string.digits)

        return ''.join(filter(lambda x: x in alpha_number, s))


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"

    r = Solution().isPalindrome(s)
    print(r)
    pass

```




## leetcode 680 验证回文字符串 Ⅱ
```python
"""

680. 验证回文字符串 Ⅱ
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:

输入: "aba"
输出: True
示例 2:

输入: "abca"
输出: True
解释: 你可以删除c字符。
注意:

字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。

https://leetcode-cn.com/problems/valid-palindrome-ii/
"""


class Solution01:
    """
    我们换一种想法。首先考虑如果不允许删除字符，如何判断一个字符串是否是回文串。
    常见的做法是使用双指针。定义左右指针，初始时分别指向字符串的第一个字符和最后一个字符，每次判断左右指针指向的字符是否相同，如果不相同，则不是回文串；
    如果相同，则将左右指针都往中间移动一位，直到左右指针相遇，则字符串是回文串。

    在允许最多删除一个字符的情况下，同样可以使用双指针，通过贪心算法实现。初始化两个指针 low 和 high 分别指向字符串的第一个字符和最后一个字符。
    每次判断两个指针指向的字符是否相同，如果相同，则更新指针，令 low = low + 1 和 high = high - 1，然后判断更新后的指针范围内的子串是否是回文字符串。如果两个指针指向的字符不同，则两个字符中必须有一个被删除，
    此时我们就分成两种情况：即删除左指针对应的字符，留下子串 s[low + 1], s[low + 1], ..., s[high]，或者删除右指针对应的字符，留下子串 s[low], s[low + 1], ..., s[high - 1]。当这两个子串中至少有一个是回文串时，就说明原始字符串删除一个字符之后就以成为回文串。


    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/valid-palindrome-ii/solution/yan-zheng-hui-wen-zi-fu-chuan-ii-by-leetcode-solut/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



    """

    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j and s[i] == s[j]:
            i += 1
            j -= 1

        return self.recur(s, i, j - 1) or self.recur(s, i + 1, j)

    def recur(self, s, i, j):
        while i < j and s[i] == s[j]:
            i += 1
            j -= 1

        return i >= j


class Solution02:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        self.memo = dict()
        while i < j and s[i] == s[j]:
            i += 1
            j -= 1

        return self.recur(s, i, j - 1) or self.recur(s, i + 1, j)

    def recur(self, s, i, j):
        if (i, j) in self.memo:
            return self.memo[(i, j)]

        while i < j and s[i] == s[j]:
            i += 1
            j -= 1
        flag = i >= j
        self.memo[(i, j)] = flag

        return self.memo[(i, j)]


class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j and s[i] == s[j]:
            i += 1
            j -= 1

        return self.recur(s, i, j - 1) or self.recur(s, i + 1, j)

    def recur(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    # s = "aaabbb"
    # s = "121"

    # s = "1234b5d4321"
    s ="abc"
    r = Solution().validPalindrome(s)
    print(r)


```



## leetcode 5. 最长回文子串

https://leetcode-cn.com/problems/longest-palindromic-substring/


```python

class Solution:
    """
    5. 最长回文子串
    给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
    
    示例 1：
    
    输入: "babad"
    输出: "bab"
    注意: "aba" 也是一个有效答案。
    示例 2：
    
    输入: "cbbd"
    输出: "bb"
    
    
    
    https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zhong-xin-kuo-san-dong-tai-gui-hua-by-liweiwei1419/
    """
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s

        # dp[i][j] 表示 s[i, j] 是否是回文串
        dp = [[False for _ in range(size)] for _ in range(size)]

        max_len = 1
        start = 0

        #  对角线的值
        for i in range(size):
            dp[i][i] = True

        for j in range(1, size):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                # 只要 dp[i][j] == true 成立，就表示子串 s[i..j] 是回文，此时记录回文长度和起始位置
                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start + max_len]

```

第二种解法,枚举中心法 

```python

class Solution2:

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        length = len(s)
        for i in range(0, length):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]

    def expandAroundCenter(self, s, i, j):
        left, right = i, j
        length = len(s)
        # print(f"length:{length}")

        while left >= 0 and right < length and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left + 1 - 1 - 1

```









## leetcode 242. 有效的字母异位词


<p>给定两个字符串 <em>s</em> 和 <em>t</em> ，编写一个函数来判断 <em>t</em> 是否是 <em>s</em> 的字母异位词。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> <em>s</em> = &quot;anagram&quot;, <em>t</em> = &quot;nagaram&quot;
<strong>输出:</strong> true
</pre>


<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> <em>s</em> = &quot;rat&quot;, <em>t</em> = &quot;car&quot;
<strong>输出: </strong>false</pre>

<p><strong>说明:</strong><br>
你可以假设字符串只包含小写字母。</p>
<p><strong>进阶:</strong><br>
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？</p>
<div><div>Related Topics</div><div><li>排序</li><li>哈希表</li></div></div>





```python
from collections import Counter
from collections import defaultdict


# leetcode submit region begin(Prohibit modification and deletion)


class Solution1:
    """
    any  只要有一个值 为1，返回 True。 全为0 返回 False


    分别统计即可   每个字符出现的频次
    统计 第一个字符 每次加一
    统计 第二字符串  每次减一

    最后 hash_map 中的value 全为0 ，则为 异位词

    """

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_map = defaultdict(int)

        for char in s:
            hash_map[char] += 1

        for char in t:
            hash_map[char] -= 1

        return not any(hash_map.values())


class Solution2:
    """
    统计每个字符出现的频次
    这里直接使用 collections 下面的 Counter 来统计
    """

    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = Counter(s)
        counter_t = Counter(t)
        return counter_s == counter_t

    def isAnagram_2(self, s: str, t: str) -> bool:
        """
        定义两个字典 进行统计 每个字符出现的频次，然后比较。
        这个 其实 和 上面的解法一样
        """

        c1 = defaultdict(int)
        c2 = defaultdict(int)

        for char in s:
            c1[char] += 1
        for char in t:
            c2[char] += 1

        return c1 == c2


class Solution3:
    """
    排序 就行
    """

    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        return s == t


class Solution4:
    """
    定义两个字典 进行统计 每个字符出现的频次，然后比较。

    这个 其实 和 solution2 的解法一样
    """

    def isAnagram(self, s: str, t: str) -> bool:

        c1 = defaultdict(int)
        c2 = defaultdict(int)

        for char in s:
            c1[char] += 1
        for char in t:
            c2[char] += 1

        return c1 == c2


class Solution5:
    """

    这个 也是排序的思想

    这里  一个字符一个字符比较，而不是 直接比较 排序过后的字符串。相对会好一些吧，如果有不相等的字符，可以直接返回了。

    """

    def isAnagram(self, s: str, t: str) -> bool:
        # check parameter
        if len(s) != len(t):
            return False
        if len(s) == 0:
            return s == t
        s = sorted(s)
        t = sorted(t)

        #
        for i, j in zip(s, t):
            if i != j:
                return False
        return True


class Solution:
    """
    思路：手动模拟hashtable，将字符串”a-z“的ASCII码作key，计数求差异

    这里注意 所有的字符都是小写 字母，所以 可以使用 长度为26 的数组 进行模拟 hash table 
    """

    def isAnagram(self, s: str, t: str) -> bool:
        arr1, arr2 = [0] * 26, [0] * 26
        for i in s:
            arr1[ord(i) - ord('a')] += 1
        for i in t:
            arr2[ord(i) - ord('a')] += 1
        return arr1 == arr2
```









## leetcode 49. 字母异位词分组
 

```python


# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。 
# 
#  示例: 
# 
#  输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ] 
#   
#  说明： 
# 
#  
#  所有输入均为小写字母。 
#  不考虑答案输出的顺序。 
#  
#  Related Topics 哈希表 字符串 



from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for str in strs:
            hash_map[tuple(sorted(str))].append(str)

        return list(hash_map.values())

```







## leetcode 438. 找到字符串中所有字母异位词

https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/

给定一个字符串 **s** 和一个非空字符串 **p**，找到 **s** 中所有是 **p** 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 **s** 和 **p** 的长度都不超过 20100。

**说明：**

- 字母异位词指字母相同，但排列不同的字符串。
- 不考虑答案输出的顺序。

**示例 1:**

```
输入:
s: "cbaebabacd" p: "abc"

输出:
[0, 6]

解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
```

 **示例 2:**

```
输入:
s: "abab" p: "ab"

输出:
[0, 1, 2]

解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
```



解题思路：  滑动窗口解法 

```python
from typing import List

from collections import defaultdict
"""


滑动窗口技巧

https://www.bookstack.cn/read/fucking-algorithm/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97-%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E6%8A%80%E5%B7%A7.md

"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        needs = defaultdict(int)
        window = defaultdict(int)

        size = len(s)
        p_size = len(p)

        left, right = 0, 0

        result = []
        match = 0
        for c in p:
            needs[c] += 1

        while right < size:
            c1 = s[right]
            if c1 in needs:
                window[c1] += 1
                if window[c1] == needs[c1]:
                    match += 1

            right += 1
            # 开始移动 左边的窗口
            while match == len(needs):
                # 在可能结果中寻找一个最优解，即是 异位词
                # 注意这里不要在加1 ，因为right上面已经加过一了，否则会多加一次
                if right - left == p_size:
                    result.append(left)
                c2 = s[left]
                if c2 in needs:
                    window[c2] -= 1
                    if window[c2] < needs[c2]:
                        match -= 1

                left += 1
        return result


if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"

    r = Solution().findAnagrams(s=s, p=p)

    print(r)

```







## leetcode 14. 最长公共前缀


https://leetcode-cn.com/problems/longest-common-prefix/

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 `""`。

**示例 1:**

```
输入: ["flower","flow","flight"]
输出: "fl"
```

**示例 2:**

```
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
```

**说明:**

所有输入只包含小写字母 `a-z` 。



```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
          
        length,count = len(strs[0]),len(strs)

        for i in range(length):
            c = strs[0][i]
            for j in range(1,count):
                if i ==len(strs[j]) or strs[j][i] !=c:
                    return strs[0][0:i]
        
        return strs[0]

```











## end tag 

