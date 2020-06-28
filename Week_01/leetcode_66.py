# -*- coding: utf-8 -*- 

"""
@Time   : 2020/6/28 21:41
@File   : leetcode_66.py
@Author : 15769162764@163.com

"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pass

        num_str = self.convert_string(digits)

        plus_one = int(num_str) + 1

        return self.convert_digits(plus_one)

    def convert_string(self, digits) -> str:
        """
        转成 字符串
        :param digits:
        :return:
        """

        return "".join(map(str, digits))

    def convert_digits(self, plus_one: int) -> List:
        """
        int  转成 数字数组
        :param plus_one:
        :return:
        """

        string = str(plus_one)

        return list(map(int, string))
