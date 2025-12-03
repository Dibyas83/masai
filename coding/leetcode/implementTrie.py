# a tree daa structure used to efficiently store and retrieve keys in a dataset of strings
# or prefix tree - used to tore strings that allows to filter and search based on prefix, used for auto complete and spell checker
"""
inp = ["Trie","insert", "search", "search", "startswith", "insert", "search"]
      [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]

Trie trie = new Trial();  instantiating trie
trie.insert("apple");  inserting apple
trie.search("apple");  true
trie.startswith("app");  true
trie.search("app");  false


inert(apple)  -  create a node for every char in word added as child of prev char and mark the end of word

a-p-p-l-e(marked as end) gives apple
  |_e(end)   gives ape
"""

class Trienode:
    def __init__(self):
        self.children = {}  # 26 chars, when a is added children["a"] = Trienode like hashing
        self.endofword = False


class Trie:
    def __init__(self):
        self.root = Trienode()

    def insert(self,word: str) -> None:
        cur = self.root

        for c in word:

