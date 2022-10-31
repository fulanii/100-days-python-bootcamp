```python
# for loop 
fruits = ['Apple', 'Peach', 'Mangoe']
for fruit in fruits:
    print(fruit + " pie")


############## Note 
# ** The len() Python method returns the length of a list, string, dictionary, or any other iterable data format in Python

# ** The Python sum() function calculates the total, works with both integers, floating-point numbers and list.

# ** max() function can be use to get the max value or highest from a list etcc 

# ** min() function can be use to get the min value or lowest from a list etcc




############# For loop with range
"""
for in range doesnt include the last number 
coz it's in range of the first and last number 

  #EX: for in range of 1, 10 will print 1 to 9 excluding 10 
  #if i want 10 printed i do for in range of 1 to 11 now 1 to 10 will be printed

    # if i want to print the number by counting by 2 or 3 or 4 etcc 
    # i just do range(1, 11, 2) the last number specify by how munch  it counts




############# FizzBuzz chalenge
  # Your program should print each number from 1 to 100 in turn.

  When the number is divisible by 3 
	then instead of printing the number it should print "Fizz".
"""
  
for numbers in range(1, 101):
  if numbers % 3 == 0 and numbers % 5 == 0:
    print("FizzBuzz")
  elif numbers % 5 == 0:
    print("Buzz")
  elif numbers % 3 ==0:
    print("Fizz")
  else:
    print(numbers)


```