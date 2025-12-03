
# lexicographically sorted -all uppercase letters come before all lowercase letters in the standard
# ASCII character set (e.g., "Apple" comes before "apple", and "Zebra" comes before "apple"). [1]

#  Lexicographically increasing order - "apple" comes before "banana," and "to" comes before "top" . ape then apple
# input is already sorted -if we see apes then ape, it has no solution as this is wrong

# [wrt,wrf,er,ett,rftt] these are sorted means using bfs we see w<e<r  t<f  r<t = w<e<r<t<f

# dfs is used

class Solut:
    def findmin(self, words: list[str]) -> str:
        adj = {c:set() for w in words for c in w} # adjacency list on basis of ordering of chars.every single char
        # is mapped to a set
        print(adj)

        for i in range(len(words) -1):
            w1,w2= words[i], words[i+1]
            minlen = min(len(w1), len(w2)) # length upto which both can be same
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""
            for j in range(minlen): # to find first diff chaar
                if w1[j] != w2[j]: # means char in w2 will come after w1
                    adj[w1[j]].add(w2[j])  # added to adj list, char in word 1 is key
                    break

        # to keep track of visited nodes use hash map or dict
        visit = {} # false- visited , True - visited and in current path may be in visit
        res = []
        def dfs(c):   # return T & F
            if c in visit:
                return visit[c] # we find c twice means a loop

            visit[c] = True # its been visited and also in the curr path
            for nei in adj[c]: # going through every char ie nei or adj of c
                if dfs(nei):
                    return True # means there is a loop
            visit[c] = False # no longer in the curr path
            res.append(c)

        for c in adj:
            if dfs(c):
                return "" # detected loop

        res.reverse()
        return "".join(res)









