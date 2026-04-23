  #Take three inputs from a user, separately. Print the largest of the numbers.
    #Hint: Determine what type of data is taken in as input.





#45
# 5if num1>num2 and num1>num3
    #print("num1")




balance= input(" balance")
balance= int( balance)

if balance<100:
    print("insuffiecient")
elif balance>=100 and balance <=1000:
    print("moderate balance")
else:
    print('high balance')





#run a program to check the following number if 10 small if above 10 but small than 50 medium and else large


numb= input("numb")
numb= int(numb)

if numb<100:
    print("small")
elif numb>=10 and numb <=50:
    print("medium")
else:
    print("large")

# Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   
#granted", otherwise print "Access denied"

password= input("")
correct_password="secret1234"
if password== correct_password:
    print("access granted")
else:
    print("acess denied")


# write an programe that ask user for email and 
# password check if eamil is is equal "admin@gmail.com"  and password "admin123" if it
#  is print access granted else access denied

email= input("enter email: ")
correct_email=="admin@gmail.com"
password= input("enter password: ")
correct_password=="admin123"
if email ==correct_email and password==correct_password:
    print("access granted")
else:
    print("access denied")