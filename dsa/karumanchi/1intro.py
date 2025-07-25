

"""
Data types that are defined by system are called primitive  ݁data types

“݅݊int  may take 2 bytes or 4 bytes. If it takes 2 bytes (16 bits), then the total possible values are minus 32,768 to plus 32,767݊i“ (-
If it takes 4 bytes (32 bits), then the possible values are between −2,147,483,648 and +2,147,483,647 (-2
 The same is the case with other data types.

If the system-defined data types are not enough, then most programming languages allow the users to define their own data types, called user defined datatype

combining many system-defined data types and calling the user defined data type by the name Newtype
"""
class NewType(object):
    def __init__(self, datainput1, datainput2, datainput3):
        self.data1 = datainput1
        self.data2 = datainput2
        self.data3 = datainput3

#The implementation for these operations can be done when we
#want to actually use them. That means, in general, user defined data types are defined along with their operations
"""
ds is a special format for organizing and storing data.

General data structure types include arrays, files, linked lists, stacks, queues, trees, graphs and 
so on. Depending on the organization of the elements, data structures are classified into two types:
linear ds
1) ܮܽ݁݊݅ݎܽ݀ ݐ ܽݑݎݐݏܿݎݑݐ݁ݏ :Elements are accessed in a sequential order but it is not compulsory to store all elements sequentially. 
ݔܧ݉ܽ݌݈݁ݏ :Linked Lists, Stacks and Queues.
nonlinear ds
2) ܰ݋݈ܽ݁݊݅ − ݊ݎܽ݀ ݐ ܽݑݎݐݏܿݎݑݐ݁ݏ :Elements of this data structure are stored/accessed in a non-linear order. ݔܧ݉ܽ݌݈݁ݏ :Trees and graphs

To simplify the process of solving problems, we combine the data structures with their operations and we call this ܣܾݎݐݏܿܽݐ ܦܽݐܶ ܽ݌ݕ݁ݏ
(ADTs). An ADT consists of ݋ݓݐ parts:
1. Declaration of data
2. Declaration of operations 
Commonly used ADTs ݈݅݊ܿݑ :݁݀Linked Lists, Stacks, Queues, Priority Queues, Binary Trees, Dictionaries, Disjoint Sets (Union and Find), 
Hash Tables, Graphs, and many others. For example, stack uses LIFO (Last-In-First-Out)operation mechanism while storing the data in data structures. 
The last element inserted into the stack is the first element that gets deleted

It is the process of determining how processing time increases as the size of the problem (input size) increases. Input size is the number of 
elements in the input, and depending on the problem type, the input may be of different types
- Size of an array
 Polynomial degree 
 Number of elements in a matrix
 Number of bits in the binary representation of the input
 Vertices and edges in a graph

What is Rate of Growth?
The rate at which the running time increases as a function of input is called rate of growth
If your friend sees you there and asks what you are buying, then in general you say ܾݕݑܽܿ ܽ ݃݊݅ݎ .This is because the cost 
of the car is high compared to the cost of the bicycle (approximating the cost of the bicycle to the cost of the car).

"""



















