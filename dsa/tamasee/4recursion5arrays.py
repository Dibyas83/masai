
"""
* The factorial function (commonly denoted as n!) is a classic mathematical
function that has a natural recursive definition.
• An English ruler has a recursive pattern that is a simple example of a fractal
structure.
• Binary search is among the most important computer algorithms. It allows
us to efficiently locate a desired value in a data set with upwards of billions
of entries.
• The file system for a computer has a recursive structure in which directories
can be nested arbitrarily deeply within other directories. Recursive algo￾rithms are widely used to
explore and manage these file systems

The factorial function is important because
it is known to equal the number of ways in which n distinct items can be arranged
into a sequence, that is, the number of permutations of n items. For example, the
three characters a, b, and c can be arranged in 3! = 3 · 2 · 1 = 6 ways: abc, acb,
bac, bca, cab, and cba.

More generally, for a positive integer n, we can define n! to be n ·(n−1)!
it contains one or more base cases, which are defined nonrecursively in terms of fixed quantities.
In this case, n = 0 is the base case. It also contains one or more recursive cases,
which are defined by appealing to the definition of the function being defined

There is no circularity in this defini￾tion, because each time the function is invoked, its argument is smaller by one, and
when a base case is reached, no further recursive calls are made.

We illustrate the execution of a recursive function using a recursion trace. Each
entry of the trace corresponds to a recursive call. Each new recursive function
call is indicated by a downward arrow to a new invocation.In Python, each time a function (recursive or otherwise) is called, a struc￾ture known as an activation record or frame is created to store information about
the progress of that invocation of the function. This activation record includes a
namespace for storing the function call’s parameters and local variables (see Sec￾tion 1.10 for a discussion of namespaces), and information about which command
in the body of the function is currently executing
When the execution of a function leads to a nested function call, the execu￾tion of the former call is suspended and its activation record stores the place in the
source code at which the flow of control should continue upon return of the nested
call. This process is used both in the standard case of one function calling a dif￾ferent function, or in the recursive case in which a function invokes itself. The key
point is that there is a different activation record for each active call


"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

"""
0    ---- major length = 4(dashes)
.125 -
.25  --                   1 -drawint(2)
     - major length = 1
0.5  ---major length = 3  2- drawline(3)
     -
     --major length = 2   3- drawint(2)
     -
1    ---- num inches = 1
.125 -
.25  --  2nd iter DRAW INTERVAL BETWEEN lines UNTIL (CENTER LENGTH-1) IS 0 
     - 
0.5  ---   1ST iteration DRAW INTERVAL BETWEEN 0 & 1 UNTIL (CENTER LENGTH-1) IS 0
     -
     --
     -
2    ---- 

"""
class Englishruler:
    def __init__(self,num_inches,major_length): #local variables that are given to instance variables
        self.__num_inches = num_inches # inches to be printed
        self.__major_length = major_length # __num_inches,__major_length(no of dashes) are instance variable

    def draw_line(self,tick_length,tick_label=''): # tick label='' is string of length 0
        line = '-' * tick_length
        if tick_label:
            line += '-' + tick_label # this is adding label to the scale like 0,1,2,3 inches or leftover space of line string of len 4
        print(line) # this is not recursive method but a helper method

    def draw_interval(self,center_length):  # will draw only the intervals or dashes not 0,1,2 inches only in between
        if center_length > 0: # center length less by one of major len
            self.draw_interval(center_length-1) # len =1 in between start and center
            self.draw_line(center_length) # drawing in the middle is what draw interval will do len = 3
            self.draw_interval(center_length-1) # len =1



    def draw_ruler(self): # will draw the whole
        self.draw_line(self.__major_length,'0')  # 1 calling draw line - 1st time
        for j in range(1,1+self.__num_inches): # 0 already done
            self.draw_interval(self.__major_length-1) #  2 in between after 4 daashes on 0 ,3 dashes will be dran in middle then 2 dashes on middle then 1 dash on middle
            self.draw_line(self.__major_length,str(j)) # 3 no of recursions to call draw_line - 2nd,3rd,4th to draw inches all with n dashes
            """
                       -----0    1

                       ----      2

                       ------1   3

                       ----
                       """

if __name__ == '__main__':
    ruler = Englishruler(5,5)
    ruler.draw_ruler()


"""
A Recursive Approach to Ruler Drawing
The English ruler pattern is a simple example of a fractal, that is, a shape that has
a self-recursive structure at various levels of magnification
Observe that the two patterns of ticks above
and below this central tick are identical, and each has a central tick of length 3.

In general, an interval with a central tick length L ≥ 1 is composed of:
• An interval with a central tick length L−1
• A single tick of length L
• An interval with a central tick length L−1
The
main function, draw ruler, manages the construction of the entire ruler. Its argu￾ments specify the total number of inches in the ruler and the major tick length. The
utility function, draw line, draws a single tick with a specified number of dashes
(and an optional string label, that is printed after the tick).
The interesting work is done by the recursive draw interval function. This
function draws the sequence of minor ticks within some interval, based upon the
length of the interval’s central tick

We rely on the intuition shown at the top of this
page, and with a base case when L = 0 that draws nothing. For L ≥ 1, the first and
last steps are performed by recursively calling draw interval(L − 1). The middle
step is performed by calling the function draw line(L).

draw interval(3)
    draw interval(2)
      draw interval(1)
            draw interval(0)
            draw line(1)        -
            draw interval(0)
            
    draw line(2)                --
    draw interval(1)
    
            draw interval(0)
            draw line(1)        -
            draw interval(0)
draw line(3)                    ---
draw interval(2)
    repeats
    
-----------------------------------------------------------------
 
    Binary Search
The algorithm
maintains two parameters, low and high, such that all the candidate entries have
index at least low and at most high. Initially, low = 0 and high = n− 1. We then
compare the target value to the median candidate, that is, the item data[mid] with
index
mid =(low +high)/2






"""

def binary_search(data, target,low,high):


    if low > high:
        return False # interval is empty; no match
    else:
        mid = (low + high) // 2
        if target == data[mid]:  # found a match
            return True
        elif target < data[mid]:
            # recur on the portion left of the middle
            return binary_search(data, target, low, mid -1)
        else:
            # recur on the portion right of the middle
            return binary_search(data, target, mid + 1, high)
data = [1,3,5,6,7,8,9,11,23,43,45,67,88,89]
print(binary_search(data,43,0,len(data)))
"""
File Systems 

The operating system allows directories to be nested arbitrarily deep (as long as there is enough
space in memory), although there must necessarily be some base directories that contain only files,
 not further subdirectories

Python’s os Module
To provide a Python implementation of a recursive algorithm for computing disk
usage, we rely on Python’s os module, which provides robust tools for interacting
with the operating system during the execution of a program. This is an extensive
library, but we will only need the following four functions:

• os.path.getsize(path)
Return the immediate disk usage (measured in bytes) for the file or directory
that is identified by the string path (e.g., /user/rt/courses).

• os.path.isdir(path)
Return True if entry designated by string path is a directory; False otherwise.

• os.listdir(path)
Return a list of strings that are the names of all entries within a directory
designated by string path. In our sample file system, if the parameter is
/user/rt/courses, this returns the list [ cs016 , cs252 ].

• os.path.join(path, filename)
Compose the path string and filename string using an appropriate operating
system separator between the two (e.g., the / character for a Unix/Linux
system, and the \ character for Windows). Return the string that represents
the full path to the file.

"""

import os
def disk_usage(path):  #Return the number of bytes used by a file/folder and any descendents"""

    total = os.path.getsize(path) # account for direct usage
    if os.path.isdir(path): # if this is a directory,
        for filename in os.listdir(path): # then for each child:
            childpath = os.path.join(path, filename) # compose full path to child
            total += disk_usage(childpath) # add child’s usage to total
    print ('{0:<7}' .format(total), path) # descriptive output (optional)
    return total # return the grand total
# Code Fragment 4.5: A recursive function for reporting disk usage of a file system.
"""
 It reports the amount of
disk space used by a directory and all contents nested within, and can produce a
verbose report, as given in Figure 4.8
55    /user/rt/courses/cs252/projects/papers/sellhigh
82    /user/rt/courses/cs252/projects/papers
4786  /user/rt/courses/cs252/projects/demos/market
4787  /user/rt/courses/cs252/projects/demos
4870  /user/rt/courses/cs252/projects
3     /user/rt/courses/cs252/grades
4874  /user/rt/courses/cs252
5124  /user/rt/courses/
Figure 4.8: A report of the disk usage for the file system shown in Figure 4.7,
as generated by the Unix/Linux utility du (with command-line options -ak), or
equivalently by our disk usage function from Code Fragment 4.5

Proposition 4.1: For c ≥ 0, a call to draw interval(c) results in precisely 2c − 1
lines of output.
Justification: We provide a formal proof of this claim by induction (see Sec￾tion 3.4.3). In fact, induction is 
a natural mathematical technique for proving the
correctness and efficiency of a recursive process. In the case of the ruler, we
note that an application of draw interval(0) generates no output, and that 20 −1 =
1−1 = 0. This serves as a base case for our claim.
More generally, the number of lines printed b

induction

In the theory of computation, the induction method, specifically mathematical induction, is a powerful proof 
technique used to demonstrate the truth of statements that involve natural numbers. It's a way to prove properties 
of recursively defined structures or algorithms. The method relies on proving a base case and an inductive step to 
establish the truth for all natural numbers greater than or equal to a starting value. 
Principle of Mathematical Induction - GeeksforGeeks
Here's a breakdown of the process:
1. Base Case:
Establish that the statement holds true for the smallest value (or values) in the set you're considering. This is 
often n=0 or n=1. 
2. Inductive Hypothesis:
Assume the statement is true for some arbitrary value k, where k is a natural number greater than or equal to the 
base case. 
3. Inductive Step:
Prove that if the statement is true for k, it must also be true for k+1. This is the crucial step that links the 
truth of the statement for one value to the next. 
By proving the base case and the inductive step, you establish a "domino effect" where the truth of the statement 
for one value implies its truth for the next, and so on, thus proving the statement for all natural numbers within 
the scope of the proof. 
Example in Theory of Computation:
Consider proving a property of a recursively defined language. You might use induction to show that for any string 
generated by the language's grammar, the string will always have a certain property. 
Base Case:
Show the property holds for the simplest string(s) generated by the grammar (e.g., the empty string).
Inductive Hypothesis:
Assume the property holds for all strings of length k generated by the grammar.
Inductive Step:
Show that if you apply a grammar rule to a string of length k (which, by the inductive hypothesis, has the 
property), the resulting string of length k+1 will also have the property.
In essence, induction allows you to prove properties of complex structures by breaking them down into smaller, 
manageable steps and showing how these steps preserve the desired property

induction method in theory of computation
Induction in the theory of computation
Induction, particularly mathematical induction, is a fundamental proof technique in the Theory of Computation 
(ToC) used to establish statements about properties that hold for all natural numbers or other recursively 
defined structures. 
Here's how it generally works and why it's important in ToC:
1. The principle of mathematical induction
Mathematical induction is used to prove statements of the form "P(n) is true for all natural numbers n".
It operates based on two main steps:
Base Case: Prove that the statement P(n) holds for the smallest possible value of n (usually 0 or 1, depending 
on the definition of natural numbers being used).
Inductive Step: Prove that if the statement holds for an arbitrary natural number k (the Induction Hypothesis), 
then it must also hold for the next natural number, k+1. 
2. Why is induction important in ToC?
Verifying Algorithm Correctness: Induction is a crucial tool for proving that algorithms work as intended for 
all possible inputs. For example, you can use induction to prove the correctness of sorting algorithms like 
Merge Sort, showing that after each step, the algorithm maintains a certain property that ultimately leads to 
a sorted output.
Analyzing Algorithm Complexity: Induction is also used to analyze the time and space complexity of algorithms, 
especially recursive ones. It helps prove that a recursive algorithm, like the Fibonacci sequence calculation, 
has a particular time complexity (e.g., exponential in that case).
Proving Properties of Data Structures: Induction can be applied to prove properties of data structures like trees, 
graphs, and lists. For example, you could prove using induction that the height of a balanced binary search tree 
with 'n' nodes is O(log n).
Formal Verification: In formal verification, induction provides a robust framework to mathematically prove the 
correctness of programs and formal systems, such as compilers or theorem provers.
Relationship to Recursion: Induction and recursion are fundamentally linked concepts. Recursion defines a function 
or structure in terms of itself, and induction provides the method for proving properties about those recursively 
defined objects. 
3. Structural induction
Structural induction is a powerful generalization of mathematical induction, used to prove statements about 
recursively defined structures like lists, trees, or propositional formulas.
It extends the concept of induction to these structures by defining a well-founded partial order on them 
(e.g., a "subformula" relation for formulas or a "sublist" relation for lists).
A structural induction proof involves proving a proposition for all minimal structures and showing that if 
the proposition holds for the immediate sub-structures of a given structure, it must also hold for the structure itself. 
In essence, induction is a cornerstone of proving properties and theorems within the realm of Theory of 
Computation, enabling rigorous analysis and verification of algorithms, data structures, and various 
computational concepts.

Principle of Mathematical Induction
Last Updated : 23 Jul, 2025
Mathematical induction is a concept in mathematics that is used to prove various mathematical statements and 
theorems. The principle of mathematical induction is sometimes referred to as PMI. It is a technique that is 
used to prove the basic theorems in mathematics which involve the solution up to n finite natural terms. 

Principle of Mathematical Induction is widely used in proving various statements such as a sum of first n natural 
numbers is given by the formula n(n + 1)/2. This can be easily proved using the Principle of Mathematical Induction.

Principle-of-Mathematical-Induction
Table of Content

What is Mathematical Induction?
Principle of Mathematical Induction Statement
Mathematical Induction Steps
Mathematical Induction Example
What is Mathematical Induction?
Mathematical Induction is one of the fundamental methods of writing proofs and it is used to prove a given statement 
about any well-organized set. Generally, it is used for proving results or establishing statements that are 
formulated in terms of n, where n is a natural number.

Suppose P(n) is a statement for n natural number then it can be proved using the Principle of Mathematical 
Induction, Firstly we will prove for P(1) then let P(k) be true then prove for P(k+1). If P(k+1) holds then we
 say that P(n) is true by the principle of mathematical induction.

We can compare mathematical induction to falling dominoes. When a domino falls, it knocks down the next domino 
in succession. The first domino knocks down the second one, the second one knocks down the third, and so on. In 
the end, all of the dominoes will be bowled over. But there are some conditions to be fulfilled:

The base step is that the starting domino must fall to set the knocking process in action.
The distance between dominoes must be equal for any two adjacent dominoes. Otherwise, a certain domino may fall 
down without bowling over the next. Then the sequence of reactions will stop. Maintaining the equal inter-domino 
distance ensures that P(k) ⇒ P(k + 1) for each integer k ≥ a. This is the inductive step.
Principle of Mathematical Induction Statement
Any statement P(n) which is for "n" natural number can be proved using the Principle of Mathematical Induction 
by following the below steps,

Step 1: Verify if the statement is true for trivial cases (n = 1) i.e. check if P(1) is true.

Step 2: Assume that the statement is true for n = k for some k ≥ 1 i.e. P(k) is true.

Step 3: If the truth of P(k) implies the truth of P(k + 1), then the statement P(n) is true for all n ≥ 1.

The image added below contains all the steps of Mathematical Induction

Principle of Mathematical Induction 
Steps for Mathematical Induction
The first statement is the fact and if it is not possible for all P(n) to hold true at n = 1 then these statements are 
true for some other values of n say n = 2, n = 3, and others.

If the statement is true for P(k) then if P(k+1) is proven to be true then we say that P(n) is true for all n
 belonging to Natural Numbers (N)

Mathematical Induction Steps
Various steps used in Mathematical Induction are named accordingly. The names of the various steps used in the 
principle of mathematical induction are,

Base Step: Prove P(k) is true for k =1
Assumption Step: Let P(k) is true for all k in N and k > 1
Induction Step: Prove P(k+1) is true using basic mathematical properties.
If the above three steps are proved then we can say that "By the principle of mathematical induction, P(n) is 
true for all n belonging to N".

Mathematical Induction Example
Mathematical induction is used to prove various statements we can learn this with the help of the following example.

Example: For any positive integer number n, prove that n3 + 2n is always divisible by 3

Solution:

Let P(n): n3 + 2n is divisible by 3 be the given statement.

Step 1: Basic Step

Firstly we prove that P(1) is true. Let n = 1 in n3 + 2n
= 13 + 2(1) 
= 3
As 3 is divisible by 3. Hence, P(1) is true.

Step 2: Assumption Step

Let us assume that P(k) is true
Then, k3 + 2k is divisible by 3
Thus, we can assume k3 + 2k = 3n,             (where n is any positive integer)....(i)

Step 3: Induction Steps

Now we have to prove that algebraic expression (k + 1)3 + 2(k + 1) is divisible by 3

= (k + 1)3 + 2(k + 1) 
= k3 + 3k2 + 3k + 2k + 3
= (k3 + 2 k) + (3k2 + 3k + 3)

from eq(i)

= 3n + 3(k2 + k + 1)
= 3(n + k2 + k + 1)

As it is a multiple of 3 we can say that it is divisible by 3.

Thus, P(k+1) is true i.e. (k + 1)3 + 2(k + 1) is be divisible by 3. Now by the Principle of Mathematical Induction, 
we can say that, P(n): n3 + 2n is divisible by 3 is true.

Read More,Arithmetic Progression Geometric Progression
Solved Examples of Mathematical Induction
Example 1: For all n ≥ 1, prove that, 12 + 22 + 32+....+n2 = {n(n + 1) (2n + 1)} / 6

Solution:
Let the given statement be P(n),
For n = 1, the left side :
1 2  = 1

The right-hand side:
P(n):12+22+32+…+n2=n(n+1)(2n+1)6
 
For n=1
P(1):1(1+1)(2×1+1)6=1
        
P(n):1  +2  +3 +…+n = n(n+1)(2n+1) 
For n=1
P(1): 61(1+1)(2×1+1) =1        

Now, let's take a positive integer, k, and assume P(k) to be true i.e.,

12+22+32+....+k2=k(k+1)(2k+1)6
        
1 +2 +3  +....+k = 6k(k+1)(2k+1)
We shall now prove that P(k + 1) is also true, so now we have,

P(k + 1) = P(k) + (k + 1)2  
=k(k+1)(2k+1)6+(k+1)2 =k(k+1)(2k+1)+6(k+1)26 =(k+1)(2k2+k)+6(k+1)6 =(k+1)(2k2+7k+6)6
=(k+1)(k+2)(2k+3)6 =(k+1)((k+1)+1)(2(+1)+1)6= 6k(k+1)(2k+1) +(k+1) 
= 6k(k+1)(2k+1)+6(k+1) = (k+1) (2k  +k)+6(k+1)= (k+1)(2k  +7k+6)= 6(k+1)(k+2)(2k+3)= 6(k+1)((k+1)+1)(2(k+1)+1)
 
Thus P(k + 1) is true, whenever P(k) is true for all natural numbers. Hence, by the process of mathematical 
induction, the given result is true for all natural numbers.

Example 2: For all n ≥ 1, prove that, 1.2.3 + 2.3.4 + 3.4.5+...+n(n + 1) (n + 2) = {n (n + 1) (n + 2) ( n + 3)} / 4

Solution: 
Let the given statement be S(n),
S(n):1.2.3+2.3.4+3.4.5+…+n.(n+1)(n+2)=n(n+1)(n+2)(n+3)4
 
For n=1,
S(1):1(1+1)(1+2)(1+3)4=6
which is true.
S(n):1.2.3+2.3.4+3.4.5+…+n.(n+1)(n+2)= 4n(n+1)(n+2)(n+3)
For n=1,
S(1): 41(1+1)(1+2)(1+3) =6
which is true.

Now, let's take a positive integer, k, and assume S(k) to be true i.e.
S(k):1.2.3+2.3.4+3.4.5+…+k.(k+1)(k+2)=k(k+1)(k+2)(k+3)4
S(k):1.2.3+2.3.4+3.4.5+…+k.(k+1)(k+2)= 4k(k+1)(k+2)(k+3)
We shall now prove that  S(k + 1) is also true, so now we have,
S(k+1):S(k)+(k+1)(k+2)(k+3)
 ⇒S(k+1):k(k+1)(k+2)(k+3)4+(k+1)(k+2)(k+3)
 
⇒S(k+1):k(k+1)(k+2)(k+3)+ 4(k+1)(k+2)(k+3)4 
⇒S(k+1): (k+1)(k+2)(k+3)(k+4)4
 
⇒S(k+1):(k+1){(k+1)+1}{(k+1)+2}{(k+1)+3}4
 
S(k+1):S(k)+(k+1)(k+2)(k+3)
 
⇒S(k+1): 4k(k+1)(k+2)(k+3)+(k+1)(k+2)(k+3)
 
⇒S(k+1): 4k(k+1)(k+2)(k+3)+ 4(k+1)(k+2)(k+3)

⇒S(k+1):  4(k+1)(k+2)(k+3)(k+4)
⇒S(k+1): 4(k+1){(k+1)+1}{(k+1)+2}{(k+1)+3}

Thus S(k + 1) is true, whenever S(k) is true for all natural numbers. And we initially showed that S(1) is true 
thus S(n) is true for all natural numbers.

Example 3: For all n ≥ 1, prove that, 1 + 3 + 5 +... + 2n - 1 = n2

Solution: 
Let the given statement be S(n), 
and S(n) = 1 + 3 + 5 +... + 2n - 1 = n2
For n = 1, 
L.H.S = 2 (1) × 1 - 1 = 1
R.H.S = 12 = 1 

Thus S(1) is true .

Now, let's take a positive integer, k, and assume S(k) to be true i.e.,
S(k) = 1+ 3 + 5+...+(2k - 1) = k2 

We shall now prove that  S(k + 1) is also true, so now we have,
1 + 3 + 5+...+ (2(k + 1) - 1) = (k + 1)2 

L.H.S = 1 + 3 + 5 + .... (2k - 1 ) + 2k + 2 - 1

⇒ L.H.S = S(k) + 2k + 1
⇒ L.H.S = k2 + 2k + 1
⇒ L.H.S = (k + 1)2 
⇒ L.H.S = R.H.S

Thus S(k + 1) is true, whenever S(k) is true for all natural numbers. And we initially showed that S(1) is true 
thus S(n) is true for all natural numbers.

Example 4: For all n ≥ 1, prove that, 1.2 + 2.3 + 3.4 +...+ n(n + 1) = {n(n + 1)(n + 2)} / 3

Solution: 
Let the given statement be S(n),
 S(n):1.2+2.3+3.4+……+n.(n+1)=n(n+1)(n+2)3
 
for n=1,
 S(1):1(1+1)(1+2)3=2
which is true. S(n):1.2+2.3+3.4+……+n.(n+1)= 3n(n+1)(n+2)
 
for n=1,
S(1): 31(1+1)(1+2)=2
which is true.
Now, let's take a positive integer, k, and assume S(k) to be true i.e.,
S(k):1.2+2.3+3.4+……+k.(k+1)=k(k+1)(k+2)3    
S(k):1.2+2.3+3.4+……+k.(k+1)= 3k(k+1)(k+2) 
       

We shall now prove that S(k + 1) is also true, so now we have,
S(k+1):S(k)+(k+1)(k+2) 
⇒S(k+1):k(k+1)(k+2)3+(k+1)(k+2)
 
⇒S(k+1):k(k+1)(k+2)+3(k+1)(k+2)3
 
⇒S(k+1):(k+1)(k+2)(k+3)3
 
⇒S(k+1):(k+1){(k+1)+1}{(k+1)+2}3
        
S(k+1):S(k)+(k+1)(k+2)
 
⇒S(k+1): 3k(k+1)(k+2) +(k+1)(k+2)
 
⇒S(k+1): 3k(k+1)(k+2)+3(k+1)(k+2) 
⇒S(k+1): 3(k+1)(k+2)(k+3)
⇒S(k+1): 3(k+1){(k+1)+1}{(k+1)+2}

Thus S(k + 1) is true, whenever S(k) is true for all natural numbers. And we initially showed that S(1) is true 
thus S(n) is true for all natural numbers.

Example 5: Prove an = a1 + (n - 1) d, is the general term of any arithmetic sequence.

Solution: 
For n = 1, 
an = a1 + (1 - 1) d = a1 
so the formula holds true for n = 1

Let us assume that the formula ak = a1 + (k - 1) is true for all natural numbers. 

We shall now prove that the formula is also true for k+1, so now we have,
ak + 1 = a1 + [(k + 1) - 1] d = a1 + k · d.

We assumed that ak = a1 + (k - 1) d, and by the definition of an arithmetic sequence ak+ 1 - ak = d,

Then, ak + 1 - ak 
= (a1 + k · d) - (a1 + (k - 1)d)
= a1 - a1 + kd - kd + d
= d
Thus the formula is true for k + 1, whenever it is true for k. And we initially showed that the formula is true 
for n = 1. Thus the formula is true for all natural numbers.
Practice Problems on the Principle of Mathematical Induction
Problem 1: Prove that for all natural numbers n, the following holds: 1 + 2 + 3 + . . . + n = [n(n + 1)]/2.
Problem 2: Show that for all integers n ≥ 1 : 13 + 23 + 33 + . . . + n3 = [{n(n + 1)}/2]2.
Problem 3: Verify that for all natural numbers n: 2n > n2.
Problem 4: Prove that for all integers n ≥ 1: 1×2 + 2×3 + 3×4 + ⋯ + n(n+1) = [n(n+1)(n+2)]/3.
Problem 5: Show that for all integers n ≥ 1: 7n − 4n is divisible by 3

Computing Factorials
 To compute factorial(n), we see that there are a
total of n+1 activations, as the parameter decreases from n in the first call, to n−1
in the second call, and so on, until reaching the base case with parameter 0.
 Therefore, we conclude that the overall number of operations for computing
factorial(n) is O(n), as there are n+1 activations, each of which accounts for O(1)
operations

Drawing an English Ruler
In analyzing the English ruler application from Section 4.1.2, we consider the fun￾damental question of how many 
total lines of output are generated by an initial call
to draw interval(c), where c denotes the center length
 We know that a call to draw interval(c) for c > 0 spawns two calls to
draw interval(c−1) and a single call to draw line. We will rely on this intuition to
prove the following claim
 In the case of the ruler, we
note that an application of draw interval(0) generates no output, and that 20 −1 =
1−1 = 0. This serves as a base case for our claim

the number of lines printed by draw interval(c) is one more
than twice the number generated by a call to draw interval(c−1), as one center
line is printed between two such recursive calls. By induction, we have that the
number of lines is thus 1+2 ·(2^(c−1) −1) = 1+2^c −2 = 2^c −1 

Performing a Binary Search
: The binary search algorithm runs in O(logn) time for a sorted
sequence with n element
the number of candidate entries still to be searched is given by the value
high−low+1.
Moreover, the number of remaining candidates is reduced by at least one half with
each recursive call. Specifically, from the definition of mid, the number of remain￾ing candidates is either
(mid−1)−low+1 
or
high−(mid+1) +1
Initially, the number of candidates is n; after the first call in a binary search, it is at
most n/2; after the second call, it is at most n/4; and so on.
Hence, the maximum number of recursive calls performed,
is the smallest integer r such that
n/2^r < 1.
In other words (recalling that we omit a logarithm’s base when it is 2), r > logn.
Thus, we have r = [logn]+1
which implies that binary search runs in O(logn) time

-------------
The argument we have made is more advanced than with the earlier examples
of recursion. The idea that we can sometimes get a tighter bound on a series of
operations by considering the cumulative effect, rather than assuming that each
achieves a worst case is a technique called amortization;
our disk usage algorithm is really
a manifestation of a more general algorithm known as a tree traversal.
-------
Recursion Run Amok
Although recursion is a very powerful tool, it can easily be misused in various ways.

We begin by revisiting the element uniqueness problem, defined on page 135
of Section 3.3.3. We can use the following recursive formulation to determine if
all n elements of a sequence are unique. As a base case, when n = 1, the elements
are trivially unique. For n ≥ 2, the elements are unique if and only if the first n−1
elements are unique, the last n−1 items are unique, and the first and last elements
are different (as that is the only pair that was not already checked as a subcase). A
recursive implementation based on this idea is given in Code Fragment 4.6, named
unique3 (to differentiate it from unique1 and unique2 from Chapter 3).


h Fibonacci number, Fn, depends on the two previous values, Fn−2 and Fn−1. But
notice that after computing Fn−2, the call to compute Fn−1 requires its own recursive
call to compute Fn−2, as it does not have knowledge of the value of Fn−2 that was
computed at the earlier level of recursion. That is duplicative work. Worse yet, both
of those calls will need to (re)compute the value of Fn−3, as will the computation
of Fn−1. This snowballing effect is what leads to the exponential running time of
bad recursion.

We can compute Fn much more efficiently using a recursion in which each invo￾cation makes only one recursive call. 
To do so, we need to redefine the expectations of the function. Rather than having the function return a single 
value, which is the nth Fibonacci number, we define a recursive function that returns a pair of con￾secutive 
Fibonacci numbers (Fn,Fn−1), using the convention F−1 = 0. Although it seems to be a greater burden to report 
two consecutive Fibonacci numbers in￾stead of one, passing this extra information from one level of the recursion 
to the next makes it much easier to continue the process. (It allows us to avoid having to recompute the second 
value that was already known within the recursion.) An implementation based on this strategy is given in Code 
Fragment 4.8

"""

def good_fibonacci(n): #Return pair of Fibonacci numbers, F(n) and F(n-1)"""
    if n <= 1:
        return (n,0)
    else:
        (a, b) = good_fibonacci(n-1)
        return(a+b, a)

print(good_fibonacci(7))

#The bad fibonacci function usesexponential time. We claim that the execution of function good fibonacci(n)
# takes O(n) time.

# Maximum Recursive Depth in Python
# Another danger in the misuse of recursion is known as infinite recursion. If each
# recursive call makes another recursive call, without ever reaching a base case, then
# we have an infinite series of such calls.
#def fib(n):
#  return fib(n)

"""
Revisiting our implementation of binary search in Code Fragment 4.3, in the final
case (line 17) we make a recursive call on the right portion of the sequence, in
particular going from index mid+1 to high. Had that line instead been written as
return binary_search(data, target, mid, high) # note the use of mid
this could result in an infinite recursion. In particular, when searching a range of
two elements, it becomes possible to make a recursive call on the identical range

The precise value of this limit depends
upon the Python distribution, but a typical default value is 1000. If this limit is
reached, the Python interpreter raises a RuntimeError with a message, maximum
recursion depth exceeded

 We organize our presentation by considering the maximum number of
recursive calls that may be started from within the body of a single activation.
1• If a recursive call starts at most one other, we call this a linear recursion.
--the implementation of the factorial function (Section 4.1.1) and
the good fibonacci function (Section 4.3) are clear examples of linear recursion.
More interestingly, the binary search algorithm (Section 4.1.3) is also an example
of linear recursion, despite the “binary” terminology in the name. The code for
binary search (Code Fragment 4.3) includes a case analysis with two branches that
lead to recursive calls, but only one of those calls can be reached during a particular
execution of the body.
We can solve this summation problem using linear recursion by
observing that the sum of all n integers in S is trivially 0, if n = 0, and otherwise
that it is the sum of the first n − 1 integers in S plus the last element in S

For an input of size n, the linear sum algorithm makes n+1 function
calls. Hence, it will take O(n) time, because it spends a constant amount of time
performing the nonrecursive part of each 
"""
def linear_sum(S, n): # Return the sum of the first n numbers of sequence S.”””
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]

S = [2,3,4,5,6,7,8,9]
print("linear",linear_sum(S,7))
"""
Reversing a Sequence with Recursion
Next, let us consider the problem of reversing the n elements of a sequence, S, so
that the first element becomes the last, the second element becomes second to the
last, and so on. We can solve this problem using linear recursion, by observing that
the reversal of a sequence can be achieved by swapping the first and last elements
and then recursively reversing the remaining elements

there are two implicit base case scenarios: When start == stop, the
implicit range is empty, and when start == stop−1, the implicit range has only
one element. In either of these cases, there is no need for action, as a sequence
with zero elements or one element is trivially equal to its reversal. When otherwise
invoking recursion, we are guaranteed to make progress towards a base case, as
the difference, stop−start, decreases by two with each call (see Figure 4.11). If n
is even, we will eventually reach the start == stop case, and if n is odd, we will
eventually reach the start == stop − 1 case. terminate after a total of 1+  n/ 2
recursive calls. Since each call
involves a constant amount of work, the entire process runs in O(n) time
"""
def reverse(S13, start, stop):
    if start < stop -1: # if at least 2 elements:
        S13[start], S13[stop-1] = S13[stop-1], S13[start] # swap first and last
        return reverse(S13, start+1, stop-1) # recur on rest

S12 = [2,3,4,5,6,7,8,9]
reverse(S12,2,5)
print(reverse(S12,3,7))


def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)
print(power(6,3))

def power(x, n):
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2) # rely on truncated division
        result = partial * partial
        if n % 2 == 1: # if n odd, include extra factor of x
            result = x
        return result
"""
The first version has a recursive depth of O(n), and therefore O(n) activation
records are simultaneous stored in memory
As we saw with the analysis of binary search, the number of times that
we can divide n in half before getting to one or less is O(logn). Therefore, our new
formulation of the power function results in O(logn) recursive ca
2• If a recursive call may start two others, we call this a binary recursion.

As another application of binary recursion, let us revisit the problem of summing the n 
elements of a sequence, S, of numbers. Computing the sum of one or zero elements is trivial. With
two or more elements, we can recursively com￾pute the sum of the first half, and the sum of the
second half, and add these sums together
"""
def binary_sum(S, start, stop):
    if start >= stop: # zero elements in slice
        return 0
    elif start == stop-1: # one element in slice
        return S[start]
    else: # two or more elements in slice
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)
s = [1,2,3,4,5,6,7,8,9,11,22]
print("bisum",binary_sum(s,0,len(s)))
"""
3• If a recursive call may start three or more others, this is multiple recursion.Another common
application of multiple recursion is when we want to enumer￾ate various configurations in order to solve
a combinatorial puzzle. For example,the following are all instances of what are known as summation puzzles:
pot + pan = bib
dog + cat = pig
boy+ girl = baby
"""
"""

Designing Recursive Algorithms
In general, an algorithm that uses recursion typically has the following form:
• Test for base cases. We begin by testing for a set of base cases (there should be at least one). These 
base cases should be defined so that every possible chain of recursive calls will eventually reach a base case, 
and the handling of each base case should not use recursion.
• Recur. If not a base case, we perform one or more recursive calls. This recur￾sive step may involve a test 
that decides which of several possible recursive calls to make. We should define each possible recursive 
call so that it makes progress towards a base case.

Parameterizing a Recursion
To design a recursive algorithm for a given problem, it is useful to think of the
different ways we might define subproblems that have the same general structure
as the original problem.  finding the repetitive structure

A successful recursive design sometimes requires that we redefine the original problem to facilitate 
similar-looking subproblems. Often, this involved reparam￾eterizing the signature of the function. For 
example, when performing a binary search in a sequence, a natural function signature for a caller would 
appear as binary search(data, target). However, in Section 4.1.3, we defined our function
with calling signature binary search(data, target, low, high), using the additional
parameters to demarcate sublists as the recursion proceed

    Eliminating Tail Recursion
the usefulness of recursion comes at a modest cost. In particular, the.Python interpreter must maintain 
activation records that keep track of the state of each nested call. When computer memory is at a premium, 
it is useful in some cases to be able to derive nonrecursive algorithms from recursive ones.

we can use the stack data structure, which we will introduce in Section 6.1, to convert a recursive
algorithm into a nonrecursive algorithm by man￾aging the nesting of the recursive structure ourselves, 
rather than relying on the interpreter to do so.Although this only shifts the memory usage from the 
inter￾preter to our stack, we may be able to reduce the memory usage by storing only the minimal information 
necess.Even better, some forms of recursion can be eliminated without any use of axillary memory. A notable 
such form is known as tail recursion. A recursion is a tail recursion if any recursive call that is made from 
one context is the very last operation in that context, with the return value of the recursive call (if any)
immediately returned by the enclosing recursion. By necessity, a tail recursion must be a linear recursion 
(since there is no way to make a second recursive call if you must immediately return the result of the first

Of the recursive functions demonstrated in this chapter, the binary search func￾tion of Code Fragment 4.3 and 
the reverse function of Code Fragment 4.10 are examples of tail recursion

Any tail recursion can be reimplemented nonrecursively by enclosing the body
in a loop for repetition, and replacing a recursive call with new parameters by a
reassignment of the existing parameters to those values.

Our original base case condition of low > high has
simply been replaced by the opposite loop condition while low <= high. In our
new implementation, we return False to designate a failed search if the while loop end

: A nonrecursive implementation of binary search
"""
def iterative(data, target):
    low = 0
    high = len(data)-1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:  # found a match
            return True
        elif target < data[mid]:
            high = mid - 1  # only consider values left of mid
        else:
            low = mid + 1  # only consider values right of mid
    return False

"""
We can similarly develop a nonrecursive implementation (Code Fragment 4.16)
of the original recursive reverse method of Code Fragment 4.10.
1 def reverse iterative(S):
2 ”””Reverse elements in sequence S.”””
3 start, stop = 0, len(S)
4 while start < stop − 1:
5 S[start], S[stop−1] = S[stop−1], S[start] # swap first and last
6 start, stop = start + 1, stop − 1 # narrow the range
"""


