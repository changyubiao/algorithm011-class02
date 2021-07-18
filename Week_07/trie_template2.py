# -*- coding: utf-8 -*-
"""
@Time    : 2021/7/18 10:55
@Author  : Frank
@File    : trie_template2.py
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isword = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """

        node = self.root

        for w in word:
            node = node.children.setdefault(w, TrieNode())
        node.isword = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]

        return node.isword

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

        node = self.root
        for p in prefix:
            if p not in node.children:
                return False
            node = node.children[p]
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
