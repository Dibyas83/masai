
def find(cards,query):
    pass

cards= [13,11,10,7,4,3,2,0],
query = 7
output = 3

res = find(cards,query)
print(res)

if res == output:
    True

# test cases
test  = {
    'input':{
        'cards': [13,11,10,7,4,3,2,0],
        'query': 7
    },
    'output': 3

}

find(test['input']['cards'], test['input']['query']) == test['output']
find(**test['input']) == test['output'] # python takes key from the dict and then the values are then used as arguments for parameters with names in cards















