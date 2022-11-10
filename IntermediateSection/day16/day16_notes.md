```python
Procedural Programing: is a style of programing, where we set up procedures or functions that do particular things. And then one procedures lead to another, 
the computer works from top to bottom line by line and jump into funtions as 
needed


Object-Orriented Programing: 
"""
Object-orriented Programing or (OOP) is a programing paradigm based on the 
concepts of 
	Objects: which contain data (known as attributes or properties) and
	Code: in the form of procedures (known as methods) 

(Note: its call oop because it's trying to model real world objects)

Ex modeling a real world object a waiter:
	has: is_holing_plate = True
			 tables_responsible = [4, 5, 6]

	does: def take_order(table, order):
						# takes order to chef
				def take_payment(amont):
						# add money to cash register

So the has and does are the most important things that makes up an object so
there call attributes and methods

attributes: is basically like a variable  thats associated with a 
						model object like our waiter above.

methods: (r just functions) but its call methods coz it's a function, a 
				 particular model object can do (in this case our waiter)

summary: in oop we're trying to model real world object and those objects have 
				 things & can do things. The things that they have are their attributes
				 those are usally modeled with variables, and the things that they can 
				 do are called methods and those are model by functions

(so oop is just combining piece of data and functionality altogether) 


"""
```

<hr>

```python
-- writting oop code 

-- Constructor:(initializing) specify what happens when object is being 
							 cosntructed/initialize and to give it a starting values etc

# The special function bellow is used to initialize and create a constructor
def __init__(): 
	 pass
# NOTE: The __init__ function will always be call when u wanna creat a new 
#				object in a class

Ex:
class User:

    def __init__(self,):
        print("User created")

user_1 = User()
user_2 = User()
user_3 = User()

"""
So above i created 3 objects from the class User()
everytime i create one the __init__ function gets call and run or (initialize)
when  i run the file i'll get 'User created' printed 3 times
"""
#-- Initializing an object

class User:

    def __init__(self, user_id, first_name):
        self.user_id = user_id
        self.name = first_name
        self.followers = 0



user_1 = User('2', 'Jane')

print(user_1.user_id)

"""
self: is the actual object being initialized/created its required when 
			initializing and creating an object

paramaters: is after self, u can have as many of them as you want above we got 2, user_id and first_name
	NOTE: When creating an object you have yo pass in the parameters as arguments
				the can't be empty unless u set a default value

				EX: user_1 = User('2', 'Jane') here im passing the 2 parameter 
						user_id and first_name

				Ex: default value, so above for self.followers im not requiring it as a 
						parameter and i alredy gave it default value 0, but i can still 
						access it when i do print(user_1.followers) will return 0

Setting Object Atributes: So once you reiceve the data from the parameter that 
get passed when the object is being contructed u can set the object attributes

EX: since ik ill get user_id and first_name i can set the object attributes 
		by doing (self.attribute_name) Ex: self.name, self.id

Self: keyword its very important when working with classes and objects 
			it's a way to refer to the object being created within the class. 
			You will never see self when using object(outside the class) 
			but you'll see it alot when writing code(inside your class).
"""

-- Methods 
class User:

    def __init__(self, user_id, first_name):
        self.user_id = user_id
        self.name = first_name
        self.followers = 0

    def follow(self):
        self.followers += 1 # will add 1 to self.followers attribute
        print("You got 1 followers now") # then this will be printed

user_1 = User('1', 'jane')

print(user_1.followers) # will print 0 coz the function wasnt call yet
print(user_1.follow()) # now the follow() method will run
print(user_1.followers) # now followers will change and be 1

"""
so above i got a simple method that add change an attribute value fro 0 to 1
and print something (that's basically how methods work it does things)
"""
```

