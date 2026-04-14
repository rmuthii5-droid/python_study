#datacleaning capital letter to lower case inthe folowng name 
name= " JOHn "

name=name.lower
print(name)


sentence_one ="The Dog Breed is German Shepherd"
print(sentence_one[16:36])
print(len(sentence_one))

sentence_two ="Defeats for the Clinton forces, this was her moment of triumph"
print(sentence_two[16:31])
print(sentence_two) 

sentence_three="The lazy dog; ran so fast it hit; the wall"
sentence_three= sentence_three.split(";")
print(sentence_three)

first_name=" Joh.n" 
first_name=first_name.replace(".", "")
last_name= " Do,e"
last_name=last_name.replace("Do,e", "Doe")
print(first_name+last_name)


