# -*- coding: utf-8 -*- 

"""
@Time   : 2020/7/13 21:24
@File   : leetcode_145.py
@Author : 15769162764@163.com

"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def postorder(root):
            if root:
                postorder(root.left)
                postorder(root.right)
                res.append(root.val)

        postorder(root)

        return res


if __name__ == '__main__':
    pass
