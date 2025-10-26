

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
            self.draw_interval(center_length-1) # cent_len - 1 in between start and center
            self.draw_line(center_length) # drawing in the middle is what draw interval will do len = 3
            self.draw_interval(center_length-1) # cent_len - 1



    def draw_ruler(self): # will draw the whole
        self.draw_line(self.__major_length,'0')  # 1 calling draw line - 1st time
        for j in range(1,1+self.__num_inches): # 0 already done
            self.draw_interval(self.__major_length-1) #  4 daashes on 0 ,3 dashes will be dran in middle then 2 dashes on middle then 1 dash on middle
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

"""









