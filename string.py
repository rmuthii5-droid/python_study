#type function is used to check the type of valuables. this how it is used.

First_name="richard"
second_name="muthii"

print(type(First_name))

number=100
number1=199.5
value=True 

print(type(number))

print(type(number1))

print(type(value))

full_name=First_name+" "+second_name
print(full_name)

number=200
number2=300
total=number+number2
print(total)

#adding strings
number='200'
number2='300'
total=number+number2
print(total) #they concat in array form

#len function is used to know number of character in a string
text="my name is richard muthii"
print(len(text))

#indexing and  means every character has a numerical representations starting 0 from right or -1 from right
text="my name is richard muthii"
print( text[8])

print(text[-13])

#slicing is extracting part of string using index

text="i am software student and am learnig python programing"
#display python programing
#displayi am software student

print( text[29:54]) #or 
print(text[29:])

#method is a function inside a class eg string method are in (classs str)
#used to modify or manipulate string valuabe