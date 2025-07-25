
def memo(m,dict):
    if m in dict:
        return dict[m]
    else: # calculate
        dict[m] = memo(m-1,dict) + memo(m-2,dict) # store the new value in dict.as we know of 0 and 1 already rest will be fond and stored in dict
        return dict[m]

dict = {0:1,1:1}  # result after each month is stored in the dictionary from which values will be fetched
print(memo(12,dict))


# getting powerset  - {1,2,3}= {},{1},{2},{3},{1,2},{2,3},{1,3},{1,2,3}
"""

[1,2] = take ist element put it in one and other blank or dont put.take 2 we can put it in blank or not
        [1,2]
      []    [1]
    []  [2] [1]   [1,2]
"""


