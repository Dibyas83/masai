
# m/n start from top left, move right or down, go to bottom right
# how many paths

# dfs with cache ,as there are many possible ways to get to a point in the path
# out of bound = 0,possible points 1
# start from end fill posible points as 1
# 
class Solut:
    def uniqpath(self, m: int, n: int) -> int:
        row = [1]* n # bottom row

        for i in range(m-1): # 1 row less
            newRow= [1]*n
            for j in range(n-2,-1,-1):
                newRow[j] = newRow[j+1] + row[j]
            row=newRow
        return row[0]









