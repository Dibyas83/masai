data = input("enter , separated: ")
num = data.split(",")
print(num)
tot = 0
for no in num:
    tot += int(no)
print(tot)

def_value = input("enter def value: ")


def display(values = def_value):
    print("value",values)

def_value = "changed default"

display()
display("new input")

display(def_value)
print("-----------------------------------------------")











