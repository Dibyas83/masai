# using trie or prefix trie having root node

"""
                          a
                a      m  --         z  or .(any)
               b       a
            (c)  (g)   (d)


"""
class Trienode:
    def __init__(self):
        self.children = {}  # hash map can have upto 26 chars, when a is added children["a"] = Trienode like hashing
        self.endofword = False


class wordDict:
    def __init__(self):
        self.root = Trienode() # initial empty trienode

    def insert(self,word: str) -> None:
        cur = self.root # starting from  root

        for c in word:
            if c not in cur.children:
                cur.children[c] = Trienode()  # c is add as a new trienode
            cur = cur.children[c] # moving to child node
        cur.endofword = True


    def search(self,word: str) -> bool:
        def dfs(j,root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".": # recursive part
                    for child in cur.children.values():
                        if dfs(i+1,child):
                            return True
                        return False
                else: # iterative part
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        return dfs(0,self.root)









