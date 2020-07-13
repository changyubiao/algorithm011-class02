# -*- coding: utf-8 -*- 

"""
@Time   : 2020/7/13 21:53
@File   : leetcode_429.py
@Author : 15769162764@163.com


429. N叉树的层序遍历
https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/solution/ncha-shu-de-ceng-xu-bian-li-by-leetcode/

"""


# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution111:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        pass


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            res.append(node.val for node in queue)
            queue = [child for node in queue for child in node.children]

        return res



if __name__ == '__main__':
    pass