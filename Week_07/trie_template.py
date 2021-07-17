# -*- coding: utf-8 -*-
"""
@Time    : 2021/7/17 16:45
@Author  : Frank
@File    : trie_template.py
"""


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 存放单词的每个字母的信息
        self.root = {}
        # 单词结束的标志位
        self.end_of_word = '#'

    def insert(self, word) -> None:
        """
        Inserts a word into the trie.
        :param word:
        :return:
        """
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        # 单词结束的标志位
        node[self.end_of_word] = self.end_of_word

    def search(self, word) -> bool:
        """
        Returns if the word is in the trie.
        :param word:
        :return:
        """

        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        # 这里要判断 最后的单词是否 结束位
        return self.end_of_word in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")

    print(trie.search("apple"))

    print(trie.search("app"))
    print(trie.startsWith("app"))
    print(trie.insert("app"))
    print(trie.search("app"))

    ...
