```python
#** fuction with inputs
def greet_with_name(name): 
	# created a variable here but dont got to define it 
	# till the function is called
    print(f"Hello {name}")
    print(f"How are you {name}")
greet_with_name(input("What is your name? ")) 
	## here the fuction gets call and need the previous variable to be defined 

#** IMPORTANT WHEN TALKING ABOUT FUNCTION WITH INPUT **#
def my_function(something): # here something will be equals to 5
    print(something + 3)
    # here do this with something 
my_function(5)
#* in programming something is know as a Parameter and 5 as Argument


##** Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"So you're from {location}")

greet_with(name = "Mike", location = "USA")
		 # this is an example of keyword argument



```