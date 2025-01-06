button = True
if button:
    print("light")
else:
    print("dark")

corrct_passwoed = "123py"
password = ""
while password != corrct_passwoed:
    password = input("enter: ")
print("access granted")

new_useer = ["alice","bob"]
for user in new_useer:
    print(f"welcome, {user}!")

atempts_1 = 0
while atempts_1< 3:
    password1 = input("enter: ")
    if password1 == "123":
        print("acess")
        break
    atempts_1 += 1
















