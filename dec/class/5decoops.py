[1,2].append([1,2])
print([1,2])
# contructor is instance method
s = {4,5,6,7}
s.add((1,2))
print(s)

tup =(1,2,[4,5])
#tup[1].append(4)
tup[2].append(4)

# inheritence allows a new class(child) to receive attributes and method from an existing parent

# class(parent) = blueprint of house
# object(child) = actual house built
"""
def solve(N):
  #  N= int(input())
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]
    for i, symbol in enumerate(symbols):
        print(f"{symbol} -{N +i*2}")
        
Description
You are given a number stored in a variable with the name N
You have to map the following symbols starting from the value N
The mapping is such that the difference between the values of two characters, is 2
'!', '@','#','$', '%', '^', '&'
For example, consider the value stored in N = 10, then the required output will be
1-10
@-12
#-14
$-16
%-18
A-20
&-22
*-24
assign the starting position of 'i' in your code 
#  for i, symbol in enumerate(symbols, 0):
remove the space after {symbol}
do like this
#print(f"{symbol}-{N +i*2}")


"""

class animal:
    def eat(self):
        print("eating")

class pet:
    def faith(self):
        print("guard")

class dog(animal,pet):
    def bark(self):
        print("barking")

class guarddog(dog):
    def powerfull(self):
        print("attack")

    def bark(self): # overiding
        print("bhhou")


print("--------------------------------")
german = dog()
kan_gal = guarddog()
print(german.eat())
print(german.bark())

print(kan_gal.faith())
print(kan_gal.powerfull())
print(kan_gal.bark())


# method overiding


