
"""
In Python, variables are categorized based on their scope, which determines where they can be accessed and modified. This categorization includes global, local, and nonlocal variables.
1. Global Variables:
Definition: Variables declared outside of any function or class, at the top level of a script or module.
Scope: Accessible from anywhere in the program, both inside and outside functions.
Modification: To modify a global variable inside a function, the global keyword must be used to explicitly declare the intent to modify the global variable, otherwise, a new local variable with the same name will be created within that function's scope.
"""

global_var = 10  # Global variable

def my_function():
    print(f"Inside function: {global_var}") # Accessing global_var
    global global_var # Declaring intent to modify global_var
    global_var = 20 # Modifying global_var

my_function()
print(f"Outside function: {global_var}")
"""
2. Local Variables:
Definition: Variables declared inside a function or a block of code.
Scope: Accessible only within the function or block where they are defined. They cease to exist once the function or block finishes execution. 
Modification: Automatically created and modified within their local scope.
"""

def another_function():
    local_var = 5 # Local variable
    print(f"Inside function: {local_var}")

another_function()
# print(local_var) # This would raise a NameError as local_var is not defined in this scope
"""
3. Nonlocal Variables:
Definition: Variables used in nested functions, where they are neither local to the inner function nor global to the entire module. They refer to variables in an enclosing (but not global) scope.
Scope: Accessible within the nested function and refer to variables in the immediate outer function's scope.
Modification: To modify a nonlocal variable inside a nested function, the nonlocal keyword must be used to explicitly declare the intent to modify the variable in the enclosing scope.
"""

def outer_function():
    nonlocal_var = "Hello" # Variable in the enclosing scope

    def inner_function():
        nonlocal nonlocal_var # Declaring intent to modify nonlocal_var
        nonlocal_var = "World" # Modifying nonlocal_var
        print(f"Inside inner function: {nonlocal_var}")

    inner_function()
    print(f"Inside outer function: {nonlocal_var}")

outer_function()









