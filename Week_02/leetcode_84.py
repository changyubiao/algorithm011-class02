# -*- coding: utf-8 -*- 

"""
@Time   : 2020/7/7 07:20
@File   : leetcode_84.py
@Author : 15769162764@163.com

"""
from typing import List


class Stack:
    """模拟栈
    Stack()    建立一个空的栈对象

    push()     把一个元素添加到栈的最顶层
    pop()      删除栈最顶层的元素，并返回这个元素
    peek()     返回最顶层的元素，并不删除它
    top()     返回最顶层的元素，并不删除它
    empty()    判断栈是否为空
    size()     返回栈中元素的个数

    print_stack()  打印 当前栈的元素

    -----
    对于 C++ STL  , 栈中的实现  接口名  获取栈顶元素 使用 top() 这个名字

    对于Java 来说 , 栈中的实现  接口名, 后去栈顶元素 使用 peek() 这个名字

    这里根据个人喜好,来使用 这个名字, 这里两个名字 都可以使用.  表达相同的含义. 都是 获取栈顶的元素, 不删除 栈顶元素.




    """

    def __init__(self):
        self.items = []
        self._size = len(self.items)

    def print_stack(self):

        for item in self.items:
            print(item, end=' ')

    def empty(self):
        return self.size() == 0

    def push(self, item):
        self.items.append(item)
        self._size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("stack is empty now.")

        self._size -= 1
        return self.items.pop()

    def peek(self):
        """
        查看 栈顶元素
        :return:
        """
        if not self.empty():
            return self.items[len(self.items) - 1]


    def top(self):
        """
        等同于 peek
        :return:
        """
        return self.peek()


    def size(self):
        return self._size


class Solution:
    """

    """

    def largestRectangleArea(self, heights: List[int]) -> int:
        """

        :param heights:
        :return:
        """
        stack = Stack()
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            while not stack.empty() and heights[stack.top()] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i - stack.top() - 1) * heights[tmp])
            stack.push(i)
        return res

if __name__ == '__main__':
    pass