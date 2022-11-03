```python
#** Dictionary in Python

#	In python dictionary are made with 2 things inside brakes {} 
#	a key and value... The value is basically the definition of the key 

# Key  | Value
# Bug  | An error in a program that stop it from running 
	here bug is the key 
	# and "An error in a program that stop it from running" is the value 


{"key": "value"} or {"bug": "An error in a program that stop it from running"}

# Bellow is what it looks like in real code
{
"key": "value" 
"key": "value"
"key": "value"
"key": "value"
}


programming_dictionary = {
    "Bug": "An error in a program that stop it from running", 
    "Function": "code that you can easily call over and over again.",
    "loop": "The action of doing something over and over again",
    "Age": 18,
    1: "One"
}
# Retriving items from dictionaries
print(programming_dictionary["Bug"])

# Adding new item to dictionaries
programming_dictionary["Name"] = "Huey"

# Creating an empty dictionary
new_dictionary = {}

# Wiping or deleting existing dictionary
programming_dictionary = {}

# Edit item in a dictionary 
# if item is not in the dictionary it will create a new item 
programming_dictionary["Bug"] = "An insect"

# Loop through a dictionary
for key in programming_dictionary:
    print(key) # this only prints the keys in the dictionary

# This print the key value 
for value in programming_dictionary:
    print(programming_dictionary[value])

#** Nesting
#** Nesting
#** Nesting

ex_nesting = {
    "key": ["list", "list2", "list3"],
    "key2": {"dict": "dict value"}    
}
    # Above is an example of nesting 
    # "key" value is a list
    # "key2" value is a dictionary 


# **Nesting a List in a Dictionary
# **Nesting a List in a Dictionary

travel_log1 = {
  "France": ["Paris", "Marseille", "Nice"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# To retrive data from the dictionary i use the key Ex:
print(travel_log1["France"]) 

# To retrive from the list value of "France" i use the number index Ex:
print(travel_log1["France"][0]) # which will print Paris




# **Nesting Dictionary in a Dictionary
# **Nesting Dictionary in a Dictionary

travel_log2 = {
  "France": {
    "cities_visited": ["Paris", "Marseille", "Nice"], 
    "total_visits": 3},
 
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 3},
}


# To retrive the data from the dictionary bellow i use the key EX: 
print(travel_log2["France"])

# To retrive data from the dictionary value of "France" i use the key value
# Bellow the key "France" has a value which is a dictionary with 2 values
# "cities_visited" and "total_visits"

# "cities_visited" have a list value which is ["Paris", "Marseille", "Nice"]
print(travel_log2["france"]["cities_visited"]) # Ex 

# Which will print the list value of "cities_visited" 
["Paris", "Marseille", "Nice"]



# **Nesting Dictionaries in Lists
# **Nesting Dictionaries in Lists

travel_log3 = [
{"country": "France", 
"cities_visited": ["Paris", "Marseille", "Nice"], 
"total_visits": 3,},

{"country": "Niger", 
"cities_visited": ["Niamey", "Agadez", "Zinder"], 
"total_visits": 3,},
]


# To retrive the data in the list i use the number index 
print(travel_log3[0]) # Ex
# that would print the first dictionary  which is index 0 etcc...

# To retrive data from the dictionary i use the key after the index
print(travel_log3[1]["cities_visited"]) # Ex
# Which will:
    print ['Niamey', 'Agadez', 'Zinder']


```