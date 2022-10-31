```python

print("Yassine"[6]) # prints "s" coz it start from index 0


# Bellow code will print yo coz y is at index 4 and o at index 7
street_name = "Abbey Road"
print(street_name[4] + street_name[7])


len() # returns lenght of an object 
type() # returns object type of an object Ex: str(), int() or float() etc..


# you can covert some object to any fuction like int() str() float() etcc.
a = str(1234) # will convert 1234 to str()
print(type(a)) # the type will be str()


# **  TO REMEMBER: 
# spaces in python matter and count as character Example 'kk k' len will be 4 instead of 3 python count from 0 not 1


# ** calculation in python
3 + 5 # add
9 - 5 # sub
7 * 8 # mul
6 / 3 # div in python div always print float Example 6/3 = 2.0 
2**2 # means to the power Ex: 2**2 = 4 


""" 
the order of operations in math "PEMDAS-LR” 
basically what come first or priotize in math 
usable  to know if u have a multiple calculation in a line of code


Parentheses ()  # comes first then exponents etc..
Exponents **
Multiplication *
Division /
Addition +
Subtraction - 
L R for left to right

Division / and  Multiplicayion * are equaly important
so wtv sign come first get executed first

"""
# * this is how to round
print(round(8/3))  
# the round() func is used Ex: 8 / 3 is 2.6666666666666665 after rounded its 3

print(round(8/3, 2))  
# comma , 2 is used to say round up to 2 number after the decimal


# ** Floor Div 
print(8//3) # will return 2
# In py div always returns decimal answer 
# so (floor div) // is used to just get int/whole num not decimal

**** += , -= , *= , /=
# The Python operators lets you (add, sub, mult, div) two values together




#**** f-string: makes it easy to print str and data types Ex: bellow

""" 
score = 0 # str
height = 1.8 # float
is_winning = True # boolean
""" 
print(f"ur score is {score} ur height is {height} r you winning? {is_winning} ") 

```