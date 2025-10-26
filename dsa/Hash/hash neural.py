
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity # capacity =  no of buckets
        self.size = 0  # no of ele in hash map list
        self.buckets = [[] for _ in range(capacity)]

    def __len__(self):
        return self.size

    def __contains__(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for k,v in bucket:
            if k == key:
                return True
        return False

    def __str__(self):
        elements = []
        for i in range(self.capacity):
            current = self.buckets[i]
            while current:
                elements.append((current.key, current.value))
                current = current.next
        return str(elements)

    def put(self,key, value):  #putting new key ,val pair
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket): # check if key in hash map ,if it is there update it
            if k == key:
                bucket[i] = (key, value)
                break
        else: # if  doesnt breaks or key not there in list
            bucket.append((key, value))
            self.size += 1

    def get(self,key): # and get val
        index = self._hash(key)
        bucket = self.buckets[index]

        for k,v in bucket:
            if k == key:
                return v
        raise KeyError('key not found')

    def key(self):
        return [k for bucket in self.buckets for k,_ in bucket] # for key in list in list

    def val(self):
        return [v for bucket in self.buckets for _, v in bucket]

    def items(self): # for pairs
        return [(k, v) for bucket in self.buckets for k, v in bucket]

    def _hash(self, key):
        key_str = str(key)
        hash_res = 0
        for char in key_str:
            hash_res = (hash_res * 31 + ord(char)) % self.capacity # so that index is not greater than capacity
        return hash_res

    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (key, val) in enumerate(bucket): # check if key in hash map
            if key == key:
                del bucket[i]
                self.size -= 1
                break
        else:
            raise KeyError('key')


# Driver code
if __name__ == '__main__':
    import uuid  # to create unique identifier string,for long string
    import matplotlib.pyplot as plt

    # Create a hash table with
    # a capacity of 5
    ht = HashTable(100)

    # Add some key-value pairs
    # to the hash table
    ht.put("apple", 3)
    ht.put("banana", 2)
    ht.put("cherry", 5)
    ht.put("name", "mike")
    ht.put("age", 25)

    # Check if the hash table
    # contains a key
    print("apple" in ht)  # True
    print("durian" in ht)  # False

    # Get the value for a key
    print(ht.__contains__("banana"))  # 2

    # Update the value for a key
    ht.put("banana", 4)
    print(ht.__contains__("banana"))  # 4

    ht.remove("apple")
    # Check the size of the hash table
    print(len(ht))  # 3
    print(ht.items())
    #print(ht.buckets)
    for _ in range(10000):
        ht.put(uuid.uuid4(), 'some_value') # adding identifiers into hashmap as key

    x = []
    y = []

    for i, bucket in enumerate(ht.buckets):
        x.append(i) # bucket nos
        y.append(len(bucket))

    plt.bar(x,y)
    plt.show() # how many identifiers in each bucket



"""   
collision handling

    #1 by going to next free space
    #2 using bucket -list of list,linked list
    f= [[],[],[],[]]
    # all land in one bucket or list if hash gives same index like 0 or 1 and then it has to move to the desired key




for i, (key, val) in enumerate(bucket): # check if key in hash map
                         ~~~~~~~~~^^^^^^^^
TypeError: 'Node' object is not iterable

hash_res * 31: The current hash result is multiplied by a prime number, 31. This step is crucial for 
distributing hash codes more uniformly and preventing simple patterns from causing collisions.


"""









