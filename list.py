trainee=["john",[2, ["james", "mary"]]]
#display 2 from the list 
print(trainee[1][0])
#out put james from list 
print( trainee[1][1][0])
#using method add 56 to the end of the list
trainee.append(56)
print(trainee)
#using the method add mike beteen john and mary
trainee[1][1].insert(1,"mike")
print(trainee)
#change 2 to 8
trainee[1][0]=8
print(trainee)