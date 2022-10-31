```python
#*** comparison operator
"""
> greater than, 
< less than, 
>= greater or equal to, 
<= less than orequal to, 
== equal to, 
!= not equal to

diff between = and == : 
= is assigning a value to a varible 
== is checking if a varible is equal to a value 
"""

# odd or even 
"""
% is called modulo it divides a num by another num and give you the remainder of that division
EX: 7 % 2 is 1 coz 2 + 2 + 2 + 1 = 7
even number are always div by 2 and any even num that is % 2 is always 0
when an odd num is % 2 its always 1  
"""


#******* 💪This is a Difficult Challenge 💪

# **every** year that is evenly divisible by 4 
# **except** every year that is evenly divisible by 100 
# **unless** the year is also evenly divisible by 400

leap_1 = year % 4 == 0 #if result is equal 0 then leap year
non_leap_1 = year % 100 != 0 #if result is equal 0 then not leap
# leap_2 = year % 400 == 0 #if result is equal 0 then leap

if leap_1 and non_leap_1 == True:
		 print("Leap year. ")
elif leap_2 == True:
     print("Leap year")
else:
     print("Non leap year") 
  

# # ***** Angela's SOLUTION ***** 
# year = int(input("Which year do you want to check? "))


if year % 4 == 0:
   if year % 100 == 0:
     if year % 400 == 0:
       print("Leap year.")
     else:
       print("Not leap year.")
   else:
     print("Leap year.")
 else:
   print("Not leap year.")
```