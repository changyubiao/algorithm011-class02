# -*- coding: utf-8 -*- 

"""
@Time   : 2020/7/22 15:35
@File   : leetcode_297.py
@Author : 15769162764@163.com


297. 二叉树的序列化与反序列化
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

示例:

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"






https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/




解法1 : 先序遍历 序列化二叉树

用 ! 表示这个节点结束的标志位

用 # 代表 空节点

res = '1!2!4!#!#!#!3!#!#!'
res.split('!')[0:-2]
['1', '2', '4', '#', '#', '#', '3', '#', '#']

"""
from queue import Queue, Empty


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str


        类似于先序遍历
        """

        if root is None:
            return "#!"
        res = str(root.val) + "!"

        res += self.serialize(root.left)
        res += self.serialize(root.right)

        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        nodes = data.split('!')[0:-2]

        q = Queue()

        for node in nodes:
            q.put(node)

        return self.recon_preorder(q)

    def recon_preorder(self, queue: Queue):

        try:
            value = queue.get_nowait()
        except Empty:
            print("queue is Empty")
            value = None
        if value == '#' or not value:
            return None

        head = TreeNode(int(value))

        head.left = self.recon_preorder(queue)
        head.right = self.recon_preorder(queue)
        return head


if __name__ == '__main__':
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)

    codec = Codec()

    r = codec.serialize(root)

    print(r)

    r2 = codec.deserialize(data=r)
    print(r2)

    # Your Codec object will be instantiated and called as such:
    # codec = Codec()
    # codec.deserialize(codec.serialize(root))
