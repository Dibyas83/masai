
# graph prob
# if 5 courses[0,1,2,3,4] and two have prerequisites [1,0] 0 should havebeen finished [4, 3] 3 should havebeen finished

# ex  5 courses[0,1,2,3,4]   prerequisites [ [0,1], [0,2], [1,3], [1,4],[3,4]]
#  prerequisites map or hashmap or adjacancy list will be used

#           map
#      crs      prereq
#       0       1,2
#       1       3,4
#       2       -
#       3       4
#       4       -
# 4 can be done so 3 so 2 so 1 and 0

# if prerequisite [[1,0],[0,1]] this is a cycle and not possible
# how to detect this cycle by using visit set,and add as we visit and check if prereq is already in set

class Sole:
    def canfinish(self,numCourses: int, prereq: list[list[int]]) -> bool:
        premap = {i:[] for i in range(numCourses)} # blank dict maping courses to prereq
        for crs,pre in prereq:
            premap[crs].append(pre)
            print(premap)
            visitset = set()
            def dfs(crs):
                if crs in visitset:
                    return False
                if premap[crs] == []:
                    return True

                visitset.add(crs)
                for pre in premap[crs]:
                    if dfs(pre): return False
                visitset.remove(crs)
                premap[crs] = []
                return True
            for crs in range(numCourses):  # for unlinked crs to preq
                if not dfs(crs): return  False
            return True




