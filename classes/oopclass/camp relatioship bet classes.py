
"""
there are 3 types of relationships bet classes in a application or programme
1- aggregation(has-a) ex customer class has many classes one is a address class
2 - inheritance(is -a)
3-
"""
# aggregate class

class Customer:

    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address

    def edit_profile(self,n_name, n_city, n_pincode, n_state):
        self.name = n_name
        self.address.change_address(n_city,n_pincode,n_state)

class Address:

    def __init__(self,city,pincode,state):
        self.city = city
        self.pincode = pincode
        self.state =state

    def change_address(self,n_city,n_pincode,n_state):
        self.city = n_city
        self.pincode = n_pincode
        self.state = n_state
add = Address("kolkata",700156,"bengal")
cust = Customer("niti","m",add) # add = address takes the format of Address or is the object of class Address

print(cust.edit_profile("Ak","gur",7897,"har"))
print(cust.address.pincode)









