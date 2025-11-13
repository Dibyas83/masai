# [1,2,3,4] targ = 7  ans = 1 1 1 4 , 2221 (not 1411 or 2122anymore)
# co

class Solut:
    def combinationSum(self, l: list[int], target: int) -> list[list[int]]:
        res = []
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >=len(l) or total>target:
                return # couldnt find combination

            cur.append(l[i])
            dfs(i, cur, total+l[i]) # ist option
            cur.pop()
            dfs(i+1,cur, total) # the 2nd option

        dfs(0, [], 0)
        return res





















