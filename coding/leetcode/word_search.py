from typing import List


# search  a word formed from ele in matrix being neighbor of each other(search in neighbor)

# brute force backtracking or dfs
#insert,search, startswith functions will be written
class Trienode:
    def __init__(self):
        self.children = {}  # 26 chars, when a is added children["a"] = Trienode like hashing
        self.isfword = False

    def addword(self,word: str) -> None:
        cur = self.root # starting from  root

        for c in word:
            if c not in cur.children:
                cur.children[c] = Trienode()
            cur = cur.children[c] # moving to child node
        cur.isword = True

class Solution:
    def findword(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trienode()
        for w in words:
            root.addword(w)

        row, col = len(board), len(board[0])
        res, visit = set(),set()  # cant visit same char twice
        def dfs(ro,co,node, word):  # i is the curr char in target word
             if (ro < 0 or co < 0 or
                     ro == row or co == col or
                     board[ro][co] not in node.children or
                     (ro, co) in visit):
                        return
             visit.add((ro, co))
             node = node.children[board[ro][co]]
             word += board[ro][co]
             if node.isword:
                 res.add(word)
             dfs(ro-1,co,node,word)
             dfs(ro+1,co,node,word)
             dfs(ro,co-1,node,word)
             dfs(ro,co+1,node,word)
             visit.remove((ro,co))

        for ro in range(row):
            for co in range(col):
                dfs(ro,co,root,"")

        return list(res)







