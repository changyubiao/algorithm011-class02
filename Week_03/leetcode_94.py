# -*- coding: utf-8 -*- 

"""
@Time   : 2020/7/13 21:20
@File   : leetcode_94.py
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)

        inorder(root)
        return res


if __name__ == '__main__':
    pass
