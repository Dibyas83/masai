
# given a string and a dict of strings ,if we break the string int two if either of words in dict
#using brute force check one by one char with dict, else check if every word(len) in dict in string that much length

# using dp                 dict={abc  def  ghi}       string = abcghi
#   check ist 3 char    abc  def  ghi
#               then   ghi
#  check no f words left in string

# bottom up - base case= dp[8]= True, (dp[7] ,dp[6],dp[5])=false as len is less in comparison to  strings in dict
# dp[4] = True,dp[3]=char 't' no word stating in t so false,same for dp2 , dp1
# dp[0] = True
# check if length of strings at dp0 and dp4 = len str  - dp[0] = dp[0+length of word at dp0] = dp4 = true


class Solut:
    def wordbreak(self, s: str, wordDict: list[str]) -> bool:
        n=len(s)
        dp = [False] * (n + 1)
        dp[n] = True # bae case

        for i in range(n -1, -1, -1):
            for w in wordDict:
                if (i+ len(w)) <= n and s[i: i+len(w)] == w: # enough char in string
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]



