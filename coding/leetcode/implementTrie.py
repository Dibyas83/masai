# a tree daa structure used to efficiently store and retrieve keys in a dataset of strings
# or prefix tree - used to store strings that allows to filter and search based on prefix, used for
# auto complete and spell checker
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
   _e(end)   e and p as children of p gives ape
"""
#insert,search, startswith functions will be written
class Trienode:
    def __init__(self):
        self.children = {}  # 26 chars, when a is added children["a"] = Trienode like hashing
        self.endofword = False


class Trie:
    def __init__(self):
        self.root = Trienode()

    def insert(self,word: str) -> None:
        cur = self.root # starting from  root

        for c in word:
            if c not in cur.children:
                cur.children[c] = Trienode()
            cur = cur.children[c] # moving to child node
        cur.endofword = True

    def search(self,word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endofword # if last word is found cur.endofword is set to true which is returned

    def startswith(self,prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return  True


