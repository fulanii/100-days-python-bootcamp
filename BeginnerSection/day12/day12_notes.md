```python

"""
Scope: 

Local Scope: is only valid where it's created ex: in the function

EX: local scope
def name(): 
    name = "yassine" 
		# this is a local scope coz i cant use it outside of the function
    print(name)

Global Scope: can be used anywhere in code as long as it's created outside any funtion and is in main code/file

EX: Global scope
name = 'yassine'  # this is a global scope i can use it anywhere
def name_print(): 
    print(name)

name_print() # will print name 'yassine'
"""
# Namespace: is anything you give a name too
# where you crerat a variable determine it's scope


# There is no block scope in python
    # if u creat a variable within an if block, while loop, 
		# for loop or anything with indentation and colant 
		# (:) that does not count as local

# Ex: Bellow 
age = 0
if age < 10:
    new_age = 11 # this variable is not a local scope
print(new_age) # so this will work just fine 

# global scope
enemies = 0

def increase_enemies():
# using global we tell the function there is a global variable 
# call eneimes you can use
    global enemies
		# without line above we get: UnboundLocalError: local variable 'enemies' 
    # referenced before assignment
    enemies += 1
    return enemies

print(enemies)
print(increase_enemies())





```