# -*- coding: utf-8 -*- 

"""
@Time   : 2020/7/20 21:58
@File   : leetcode_226.py
@Author : 15769162764@163.com



226. 翻转二叉树
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
备注:


https://leetcode-cn.com/problems/invert-binary-tree/description/

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def invertTree(self, root)-> TreeNode:
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 递归函数的终止条件，节点为空时返回
        if not root:
            return None

        # 将当前节点的左右子树交换
        root.left, root.right = root.right, root.left

        # 递归交换当前节点的 左子树和右子树
        self.invertTree(root.left)
        self.invertTree(root.right)
        # 函数返回时就表示当前这个节点，以及它的左右子树
        # 都已经交换完了
        return root


if __name__ == '__main__':
    pass
