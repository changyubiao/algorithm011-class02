# -*- coding: utf-8 -*- 

"""
@Time   : 2020/7/25 16:33
@File   : leetcode_17.py
@Author : 15769162764@163.com



17. 电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。




示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。





"""
from typing import List, Dict


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        hash_map = {

            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        self.result = []

        if not digits:
            return self.result

        current_result = ""
        self._generate_combination(digits=digits, hash_map=hash_map, current_result=current_result, level=0)

        return self.result

    def _generate_combination(self, digits: str, hash_map: Dict, current_result: str, level: int):
        if level == len(digits):
            self.result.append(current_result)
            return

        # process current  level
        letters = hash_map[digits[level]]

        for j in range(0, len(letters)):
            # drill down
            self._generate_combination(digits, hash_map, current_result + letters[j], level + 1)

        # reverse states


if __name__ == '__main__':
    digits = "23"
    r = Solution().letterCombinations(digits=digits)

    print(r)
    pass
