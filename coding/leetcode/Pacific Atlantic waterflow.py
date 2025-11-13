
# bigger can cross small,can move l,r,u,d.border ele can reach oceans
"""
           pacific
pacific  1 2 3 3 5   atlantic
         3 2 3 4 4
         2 4 5 3 1
         6 7 1 4 5
         5 1 1 2 4
         atlantic
"""
# filterout border elemnt to their respective ocean , check ele in the middle who can go in both direction
# use set and dfs cache

class Sole:
    def paat(self, heights: list[list[int]]) -> list[list[int]]:
        rows, cols = len(heights), len(heights[0]) #  [[1234], [5678]]
        pac, atl =set(), set()

        def dfs(r, c, visit, prevheight): # visited or add to pac or atl
            if ((r,c) in visit or
            r<0 or c<0 or r == rows or c == cols or heights[r][c] < prevheight): # out of bound and not  possible to cross cooming from ocean
                return
            visit.add((r,c))
            # up,down,right,left
            dfs(r+1, c,visit, heights[r][c])
            dfs(r-1, c,visit, heights[r][c])
            dfs(r, c+1,visit, heights[r][c])
            dfs(r, c-1,visit, heights[r][c])


        for c in range(cols): #  water from ocean can go to <= heights
            dfs(0, c, pac, heights[0][c]) # for cols in first row.
            dfs(rows-1, c,atl, heights[rows-1][c]) # for cols in last row

        for r in range(rows):  # in ist and last col
            dfs(r, 0,pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r,c) in atl:
                    res.append((r,c))
        return  res







