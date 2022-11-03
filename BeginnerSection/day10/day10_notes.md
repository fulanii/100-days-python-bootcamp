```python
###################################### 100 days of code day 10
###################################### 100 days of code day 10

#** Function with outputs

def format_name(f_name, l_name):
    f_f_name = f_name.title()
    f_l_name = l_name.title()
    return f"{f_f_name} {f_l_name}" ) # this get printed
    # return ends a fuction meaning any code 
		# after the return function wont get executed 

format_name("yassine", "issoufou")

# new notes on fuction w outputs 
# new notes on fuction w outputs 
 

def my_fuction():
    name = "Yassine"
    return name 
# here the return keyword will return the value of name which is "Yassine"

my_fuction() # will return/print  "Yassine"

f_name = my_fuction() 
		# since now my_fuction() = "Yassine" so is f_name
print(f_name) # Yassine will get printed

# when u return something in a fuction what's being return replaces where the fuction is call EX:

def my_fuction():
    name = "Yassine"
    return name

# Ex of return fuction 
# Ex of return fuction 

def my_fuction():
    name = "Yassine"
    return name # the fumction will end here anything bellow will not run
    print("Izzoufxu") # this will not run

print(my_fuction()) 

#TIPS

# the return function should be the last to run in a fuction 
# coz in python the return fuction tell it its the end of the code 

def my_fuction():
    return "any code bellow will not run" 
# you can add msg like this to be return 
    print("Izzoufxu") # will not get printed

print(my_fuction()) 

#** Docstring
		# docstring are written using the triple quotes """  """
		# anything in the quotes will serve as explanation to the code 
    # EX: bellow
def format_name(f_name, l_name):
 """ Take a first and last name and format it 
to return the title case version of the name."""

# print vs return 
"""
the return keyword help  us reuse code if we want too, but its not posible with the print keyword

EX: the calculation bellow can not be done with print
"""
def my_fuction(a, b):
    return a + b 

print(my_fuction(1, 2))

awnser_2 = my_fuction(1,) + 10 
	# by using return we can re-use the first awnser to a + b 
print(awnser_2)

```