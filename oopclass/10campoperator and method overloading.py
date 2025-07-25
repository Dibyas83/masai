from fractions import Fraction


#polymerphism - multiple faces  > method overriding and overloading,operator overloading

#method overloading - by giving different values or process to method we get different result
# area = triangle ,square,recta

class Geometry:
    def area(self,radius,side=0):# default is set
        if side == 0:
            return 3.14 * radius**2
        else:
            return radius*side
    #def area(self,a,b,c):
        #return a*b*c

obj =Geometry()
print(obj.area(4))
print(obj.area(4,5))

#operator overloading- (+,-,>,<)if operator behaves differently other than its natural use
print("ad" + "me")
x = Fraction(3,4)
y = Fraction(5,6)
print(x+y)



















