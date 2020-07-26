# -*- coding: utf-8 -*- 

"""
@Time   : 2020/7/22 13:37
@File   : leetcode_111.py
@Author : 15769162764@163.com


111. 二叉树的最小深度
给定一个二叉树，找出其最小深度。

最小深度是从 根节点 到最近 叶子节点 的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.




https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/

解题 思路  : 直接递归解决

要找到 递归的结束的条件


基线条件 和 递归条件

结束递归的条件, 我们 称为  基线条件
递归条件




每个递归函数都有两部分：基线
条件（ base case）和递归条件（ recursive case） 。递归条件指的是函数调用自己，而基线条件则
指的是函数不再调用自己，从而避免形成无限循环







解法1 : 递归 + 深度优先遍历
https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/solution/er-cha-shu-de-zui-xiao-shen-du-by-leetcode/





"""

# Definition for a binary tree node.
import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution01:
    def minDepth(self, root: TreeNode) -> int:
        """
        最直接的思路就是递归。

        我们用深度优先搜索来解决这个问题。

        :param root:
        :return:
        """

        if root is None:
            return 0

        # 叶子节点 的定义 是左右孩子 都没有 的节点 , 所以 是and 的关系.
        if root.left is None and root.right is None:
            return 1

        min_depth = sys.maxsize
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)

        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)

        return min_depth + 1


class Solution02:
    def minDepth(self, root: TreeNode) -> int:
        """
        还是 递归来解决

        AC  通过

        :param root:
        :return:
        """
        if root is None:
            return 0

        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)

        # 处理只有左子树或者右子树的情况或者叶子节点
        if root.left is None or root.right is None:
            return left_depth + right_depth + 1

        #  同时存在左右子树
        return 1 + min(left_depth, right_depth)


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """

        reference :

        题目中说明:叶子节点是指没有子节点的节点，这句话的意思是 1 不是叶子节点

        题目问的是到叶子节点的最短距离，所以所有返回结果为 1 当然不是这个结果

        另外这道题的关键是搞清楚递归结束条件

        叶子节点的定义是左孩子和右孩子都为 null 时叫做叶子节点
        当 root 节点左右孩子都为空时，返回 1
        当 root 节点左右孩子有一个为空时，返回不为空的孩子节点的深度
        当 root 节点左右孩子都不为空时，返回左右孩子较小深度的节点值

        作者：reals
        链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/solution/li-jie-zhe-dao-ti-de-jie-shu-tiao-jian-by-user7208/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



        :param root:
        :return:
        """
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)

        # 里其中一个节点为空，说明 left_depth 和 right_depth 有一个必然为0，所以可以返回 left_depth + right_depth + 1
        if root.left is None or root.right is None:
            return left_depth + right_depth + 1


        # 最后一种情况，也就是左右孩子都不为空，返回最小深度+1即可
        return min(left_depth, right_depth) + 1


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)

    r = Solution().minDepth(root)

    print(f"r = {r}")

    pass
