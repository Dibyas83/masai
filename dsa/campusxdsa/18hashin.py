
# hashing gives fast searching

"""
linear search - o(n)
binary search(sorted) - logn
hashing - constant

in array = l[150](target)  -> head address + mem size * 150 -> so constant time using index search,if we store data in theie index
but there will be wastage of mem [1,3,1000] for 3 items an array size of 1000 will be used

by using hashing function -> item %10 = index
11,22,33,44,55,66,77,88,99,100 - on index 1,2,3,4,5,6,7,8,9,0
if somebody asked for 101 - 101%10=1 , 11 != 101 so return not there


if data is [cat dog rat] size 3 of all int = [asci(c) + asci(a) + asci(t)] % size
"""
import select

cat = ord("c") + ord("a") + ord("t")
print(cat)
print(cat%10//2)
dog = ord("d") + ord("o") + ord("g")
print(dog)
print(dog%10//2)
rat = ord("r") + ord("a") + ord("t")
print(rat)
print(rat%10//2)

"""collison - two item with same index.solved by 
1-closed addressing technique -or chaining-duplicate will stay in the same address
by using node which has all items of same index is chained to same adress by creating nodes with
item in it and next pointed to other item address 

31,47,16,21,36 
l[1] = 31%5 = 1,l[2] = 47%5 = 2, 16%2 = 1,21%5 = 1,36%5= 1
this is not a int array but a node array(data,next)
if asked for 36 index 1  - we go to 1 compare if not there we traverse next by next    
When linked list created becomes bigger than array, there is no benifit
a - rehashing technique -if load factor crossed array size is increased,and hashing size inc and 
rehashing happens and items are placed in new places
b - chaining is long , we create balanced tree(logn)
                                       
2-open addressing technique-or linear probing,quadratic probing-send to a different mem address .
if same index we check the next address is blank or not
a-linear
(36,41,22,37,51)%5 = (1,1,2,2,1)- (0-51   1-36   2-41   3-22   4-37)
g(i) = [h(i) + k(i')] % size
h(i) = i
k(i') = i' for ist time i'=0
items = 36  -> 36%size=1,i'=0 ->[1+0]%5=1 index
item=41 -> [1+0]%5=1 index,but full ,make i' =2,[1+1]%5 = 2 index
item = 22 -> [2+0]%5=2 but full-[2+1]%5=3 index
item = 37 -> [2 +0]%5 = 2,but full-[2+1]%5=3 index,but full-[2+2]%5=4 index
item = 51 similarly goes to 0

it does clustering 1,2,3,-,-,-,-,-,5,6,7,-,-,-,-,-,8,9,11,12
these blank spaces are used to store items in future and also leads to mem wastage
so quadratic used
search 51 - search in 1 not there ,search next and traverse

b- quadratic probing(next) - g[i] = [h(i) +k(i')]%size      i= i*i
(36,43,22,52,51,63,21,33,44,99,11)%10 = (1,1,2,2,1)- (0-51   1-36   2-41   3-22   4-37)
g(i) = [h(i) + k(i')] % size
h(i) = i*i
k(i') = i' for ist time i'=0
items = 36  -> 36%size=6,i'=0 ->[6+0]%10=6 index
item=41 -> [1+0]%10=1 index,but full-[1+1]%10=2 index
item = 22 -> [2+0]%10 =2 but full-[2+1]%10=3 index
item = 52 -> [2 +0]%10 = 2,but full-[2+1]%10=3 index,but full-[2+4]%10=6 index,but full-[2+9]%10=1 index
idex 10 is 0


"""
class Dict: # using hash ,using two array one for keys one for values

    def __init__(self,size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,value):  # for placing key:value pair into dict,so we need a hash function and give it key
        hash_value = self.hash_functions(key)

        if self.slots[hash_value] == None:
            self.slots[hash_value] = key  # python ,hash value being 2
            self.data[hash_value] = value  # 45 ,hash value being 2
        else:
            if self.slots[hash_value] == key: # if the key was inserted beforehand or anyother key because of same hash
                self.data[hash_value] = value # nothing changes
            else: # not same key but different key,ist we use linear probing and do rehashing
                new_hashval = self.rehash(hash_value)  # this maybe empty or filled
                while self.slots[new_hashval] != None and self.slots[new_hashval] != key:  # untill we get none or the key already nserted
                    new_hashval = self.rehash(new_hashval)

                if self.slots[new_hashval] == None:
                    self.slots[new_hashval] = key
                    self.data[new_hashval] = value
                else: # found the key already their
                    self.data[new_hashval] = value

    def get(self,key):
        start_pos = self.hash_functions(key) # need to get the index from where to start,if we reach the
        # same position after traversing ,it is not there and if we get none(python is bet start and none linear probe)
        cur_pos = start_pos
        while self.slots[cur_pos] != None:

            if self.slots[cur_pos] == key:
                return self.data[cur_pos]
            cur_pos = self.rehash(cur_pos)  # if key not found in cur pos,cur pos is changed

            if cur_pos == start_pos:
                return "not found"
        return "not found"  # if none found


    def __str__(self):
        for i in range(len(self.slots)):
            if self.slots[i] != None:
                print(self.slots[i],":",self.data[i],end=' ') # i is the index or hash value
        return ""


    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value): # it will call put and pass key,value to it,so can make dict like input
        self.put(key,value)

    def rehash(self,old_hashval):
        return (old_hashval + 1) % self.size


    def hash_functions(self,key): # gives index
        #return key %self.size  # but will not working on string
        return abs(hash(key)) % self.size  # will work on string ,int,unmutable objects like tuple not list,
        # sometimes they are negetive so use abs

d1 = Dict(3)

print(d1.slots)
print(d1.data)

d1.put("python",45)
d1.put("java",45)
d1.put("php",100)
print(d1.slots)
print(d1.data)
d1["python"] = 50
print(d1.slots)
print(d1.data)
print(d1["java"])
print(d1["python"])

print(d1)






