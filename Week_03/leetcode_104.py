# -*- coding: utf-8 -*- 

"""
@Time   : 2020/7/22 13:30
@File   : leetcode_104.py
@Author : 15769162764@163.com



104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution01:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.current = 0
        self.max_depth = 0

        self.find_max_depth(root)
        return self.max_depth

    def find_max_depth(self, root: TreeNode):

        #  terminal 边界
        if root is None:
            return self.max_depth

        self.current += 1

        if root.left is not None or root.right is not None:
            if root.left is not None:
                self.find_max_depth(root.left)
                self.current -= 1

            if root.right is not None:
                self.find_max_depth(root.right)
                self.current -= 1
        else:
            # 是根节点,更新 最大值
            self.max_depth = max(self.current, self.max_depth)


if __name__ == '__main__':
    root = TreeNode(1)

    root.left = TreeNode(2)

    r = Solution().maxDepth(root)
    print(f"r={r}")

    pass
