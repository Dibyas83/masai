
# search  a word formed from ele in matrix being neighbor of each other(search in neighbor)

# brute force backtracking or dfs

class Solut:
    def exist(self, board: list[list[str]], word: str) -> bool:
         r,c = len(board), len(board[0])
         path = set() # cant visit same char twice

         def dfs(ro,co,i):  # i is the curr char in target word
             if i == len(word):  # means found
                 return  True
             if (ro < 0 or co < 0 or
                     ro >= r or co >= c or 
                     word[i] != board[ro][co] or
                     (ro, co) in path):
                 return False
             path.add((ro, co))
             res = (dfs(ro+1,co, i+1) or
                    dfs(ro-1,co, i+1) or
                    dfs(ro,co+1, i+1) or
                    dfs(ro,co-1, i+1)) # in 4 pos
             path.remove((ro,co))
             return  res

         for i in range(r):
              for j in range(c):
                  if dfs(i,j,0):
                      return True

         return False







