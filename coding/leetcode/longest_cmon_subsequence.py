
# abcde - random char's ace is subsequence aec is not
# and ace should be common bet two string
# by finding common chars subsequently bet two strings

#  using two dimentional dp                    a   c   e   if matched goes to next(remaining) to match
#                                          a   1           diagonally if not matched checks right or down
#1 abcde  bcde   2 bbcde  bcde             b       0        default is 0 outside matrix
# a matched         b didnt match          c       1
# ace     ce       ace    ace              d           0
#                                          e           1

class Solut:
    def longest_comon_subseq(self,text1: str,text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        dp = [[0 for j in range(n2+1)] for i in range(n1+1)]  # dp constructed with 0 as default outside matrix

        for i in range(n1-1,-1,-1):
            for j in range(n2-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j]) # search sol in down or right

            return dp[0][0]   # result ends at top left






