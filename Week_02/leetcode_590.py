# -*- coding: utf-8 -*- 

"""
@Time   : 2020/7/13 21:48
@File   : leetcode_590.py
@Author : 15769162764@163.com

"""
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        res = []

        def my_post(root):
            if root:
                for node in root.children:
                    my_post(node)

                res.append(root.val)

        my_post(root)
        return res


if __name__ == '__main__':
    pass
