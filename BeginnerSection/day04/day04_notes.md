```python
### Ramdom Module

import random # ramdon is a py module u can use to generate random values

import fun_2 
		# u can create as many module in ur code EX: for a discord bot u can have 
		# commands, main, owner, roles  etc 

print(fun_2.name) 
# to use anything from a diff module u use module name then dot (.) wtv u need 
# EX: here i did (fun_2.name) i used this to print the value of name that i stored in fun_2.py which was "Yassine"


#** To print a whole number (int) # can inclue 1 or 100
random_number = random.randint(1, 100)
print(random_number)

#** To print a random decimal number (float) between 0 and 1
ramdom_float = random.random() 
print(ramdom_float)

#** To print a random number between 0 and wtv
ramdom_num = random.randint(0, 5)
print(ramdom_num)



#### **** Lists in python 
# More info here: https://docs.python.org/3/tutorial/datastructures.html

"""
list are created using [] , EX: us_states = ["Michigan", "Alaska", "Kansas"] 

to get anything from a list i can use [] and the number 
	EX: print(us_states[0]) Michigan will be printed

python count from 0 and up EX: Michigan is 0 Alaska is 1 Kansas is 2 etcc 

u can use negative (-) numbers to print from end of list 
	EX: print(us_states[-1]) Kansas will be printed etcc

"""
 
# ******** To remember 
"""
.split(",") is used to change strings divied by a comma (,) into a list 
	EX: string = "Hello, python, is, great, for, real" then string.split(",") 
	will returm ["hello", "python", "is", "great", "for", "real"]

******** 
VERY IMPORTANT ALWAYS READ DOCUMANTATIONS AND INSTRUCTION VERY CAREFULLY 
********

Idex Errors  
	When working with list the index out of range is the most common error
"""



# ********* Nested Lists *********

dirty_dozen_1 = ['apple', 'banana', 'avocado' 'cherries', 'lemon', 'beans', 
'broccoli', 'carrot', 'celery', 'corn' ]

"""
nested list are list within a list Ex: above we have a list of fruits and vegies 
	how can we seperated then into fruits and vegie lists 
	while keeping then in the dirty dozen list

** Demostration bellow
fruits = ['apple', 'banana', 'avocado' 'cherries', 'lemon']
vegetables = ['beans', 'broccoli', 'carrot', 'celery', 'corn' ]

dirty_dozen = [fruits, vegetables] 
		now here ive seperated and combimed 2 lists vegies and fruits 
		that bellong in dirty dozen

print(dirty_dozen) 
	when i print dirty dozen i get 3 list 
	[[fruits], [vegies]] 
	and the new list there both in aka dirty_dozen
"""
```