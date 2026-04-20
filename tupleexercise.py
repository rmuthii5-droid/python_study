# attempt all the questions

#1. numbers = (10, 20, 30, 40, 50)Add 60 to the end,Replace 30 with 35.
#2. values = (15, 5, 30, 25, 10) arrange the elements in ascending order.
#3. fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
#Count occurrences of "banana",Remove all occurrences of "banana".
#4. names = ("Alice", "Bob", "Charlie", "David") Reverse the order of elements using 
#sort method.
#5. colors = ("red", "blue", "green")add "yellow" at index 1,Extend with ["purple", 
#"orange"]

numbers = (10, 20, 30, 40, 50)
my_number=list(numbers)
print(my_number)
my_number.append(50)
print(my_number)
my_number.remove(30)
print(my_number)
my_number=tuple(numbers)

#2. values = (15, 5, 30, 25, 10) arrange the elements in ascending order.

values = (15, 5, 30, 25, 10)
my_values=list(values)
my_values.sort()
print(my_values)
my_values=tuple(values)

#3. fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
#Count occurrences of "banana",Remove all occurrences of "banana".

fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
len(fruits)
fruits.count("banana")

#4. names = ("Alice", "Bob", "Charlie", "David") Reverse the order of elements using 
#sort method.

names = ("Alice", "Bob", "Charlie", "David")
my_name=list(names)

my_name.reverse()