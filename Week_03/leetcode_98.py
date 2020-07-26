# -*- coding: utf-8 -*- 

"""
@Time   : 2020/7/20 22:17
@File   : leetcode_98.py
@Author : 15769162764@163.com


98. 验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。



https://leetcode-cn.com/problems/validate-binary-search-tree/


解法1 : 递归

解法2 中序遍历

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        return self.recurse(root, float('-inf'), float('inf'))

    def recurse(self, node: TreeNode, lower, upper):

        if node is None:
            return True

        # process level
        cur_val = node.val

        if cur_val >= upper or cur_val <= lower:
            return False

        if not self.recurse(node.right, cur_val, upper):
            return False

        if not self.recurse(node.left, lower, cur_val):
            return False

        return True


class Solution02:
    def isValidBST(self, root: TreeNode) -> bool:

        stack = []

        # 用来存储上一个 中序遍历的树结点的值
        inorder = None

        while stack or root is not None:
            while root is not None:
                stack.append(root)
                root = root.left

            root = stack.pop()
            #  如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if inorder is not None and root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True


if __name__ == '__main__':
    pass
