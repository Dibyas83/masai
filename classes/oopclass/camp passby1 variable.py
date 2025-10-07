


class Customer:
    def __init__(self,name,gender):
        #print("hello")
        self.name = name
        self.gender = gender


def greet(customer):  # a func is created outside class
    if customer.gender == "male":
        print("hello",customer.name,"sir")
    else:
        print("hello",customer.name,"maam")

    cust2 = Customer("arun","male")  # through this function a object is returned
    return cust2

cust = Customer("siksha","female")
#rint(cust.name)
#greet(cust)  # fuction is given  an object as argument or var as customer. so cust = customer,so cust.name can access class name
greet(cust) # now it is returning a object,cust2=customer
new_cust = greet(cust) # new_cust will behave as customer,as it stores the object cust2 which behaves as object of class Customer
print(new_cust.name) # this will return name of cust2
greet(new_cust)  # now its greeting its own created customer




































