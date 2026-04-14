#manipulating strings into capital. upper or lower cases 
# capitilize make the first character uper case 

text="software developer"
text1=text.capitalize()
print(text1)

#upper - convert string to uppercase
text2=text.upper
print(text2)

#casefold return lowecase 

text3= "SOFTWARE DEVELOPMENT"
text3=text.casefold
print(text3)

# .strip() used to clean up data by removing trailing space




#find character in srting use index to pin point 
text="software developer"
print(text.index("d"))


#replacing a string
text=text.replace("software", "python")
print(text)

#spilt used to split string using specific characters 
email= "rmuriuki27@yahoo.com"
email= email.split("@")
print(email)