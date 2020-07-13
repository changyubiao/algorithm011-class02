# -*- coding: utf-8 -*- 

"""
@Time   : 2020/7/13 21:18
@File   : leetcode_144-preorder.py
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
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def preorder(root):
            if root:
                res.append(root.val)
                preorder(root.left)
                preorder(root.right)

        preorder(root)

        return res

if __name__ == '__main__':
    pass