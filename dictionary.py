#data structure that store keyword with values 
#keys are always strings and unique 
my_dictionary= {
    "name": "richard muthii",
    "gender": "male",
 "age": 40,
 "town": "kagumo",

}
print(my_dictionary)
print( type(my_dictionary))


#accessing values in dictionaries
print( my_dictionary["age"])

#updating a dictionary 

my_dictionary["age"] =41
print(my_dictionary["age"])
my_dictionary["town"]= "mombasa"

#adding a new property
my_dictionary["occupation"]= "software dev"
print(my_dictionary)

#dictionary method 
my_dictionary.pop("age")
#my_dictionary.popitem=remove last updated item
