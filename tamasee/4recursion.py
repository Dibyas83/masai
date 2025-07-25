
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
0    ---- major length = 4
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
    def __init__(self,num_inches,major_length):
        self.__num_inches = num_inches # inches to be printed
        self.__major_length = major_length # __num_inches,__major_length(no of dashes) are instance variable

    def draw_line(self,tick_length,tick_label=''): # tick label='' is string of length 0
        line = '-' * tick_length
        if tick_label:
            line += '-' + tick_label # this is adding label to the scale like 0,1,2,3 inches or leftover space of line string of len 4
        print(line) # this is not recursive method but a helper method

    def draw_interval(self,center_length):  # will draw only the intervals or dashes
        if center_length > 0:
            self.draw_interval(center_length-1) # len =1
            self.draw_line(center_length) # drawing in the middle is what draw interval willdo len = 3
            self.draw_interval(center_length-1) # len =2

    def draw_ruler(self): # will draw the whole
        self.draw_line(self.__major_length,'0')
        for j in range(1,1+self.__num_inches): # 0 already done
            self.draw_interval(self.__major_length-1) # after 4 daashes on 0 ,3 dashes will be dran in middle then 2 dashes on middle then 1 dash on middle
            self.draw_line(self.__major_length,str(j))


if __name__ == '__main__':
    ruler = Englishruler(5,5)
    ruler.draw_ruler()










