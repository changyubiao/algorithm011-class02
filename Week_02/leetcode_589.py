# -*- coding: utf-8 -*- 

"""
@Time   : 2020/7/13 21:45
@File   : leetcode_589.py
@Author : 15769162764@163.com

"""
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        if not root:
            return []
        res = [root.val]

        for node in root.children:
            res.extend(self.preorder(node))

        return res


class Solution02:
    """
    # N叉树通用递归模板
    """
    def preorder(self, root: 'Node') -> List[int]:
        res = []

        def helper(root):
            if not root:
                return

            res.append(root.val)
            for child in root.children:
                helper(child)

        helper(root)
        return res


if __name__ == '__main__':
    pass
