
import random

x = random.randint(1,8)
y = random.randrange(1,8)
li =["h","u","d","o"]
z = random.choice(li)
random.seed(17)
"""
The seed() method is used to initialize the random number generator.

The random number generator needs a number to start with (a seed value), to be able to generate a random number.

By default the random number generator uses the current system time.

Use the seed() method to customize the start number of the random number generator.

Note: If you use the same seed value twice you will get the same random number twice. See example below
"""
print(random.random())
random.seed(19)
print(random.random())
print(x)
print(y)
print(z)
















