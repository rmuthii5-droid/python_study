#Create a new file extra_if_task.py

# 1 Write a program that checks login credentials:
#"Access granted" if email = "admin@gmail.com" and password = "Admin@123"
#"Wrong password" if email is correct but password is wrong
#"Email not found" otherwise

email=input("enter email: ")
email="admin@gmail.com"
password=input("enter password: ")
password="Admin@123"
if email=="admin@gmail.com" and password=="Admin@123":
    print("access granted")
else: 
    print("email not found")


#Create a program that validates an email:
#Invalid email" if it does not contain "@" or "."
#"Gmail account" if it ends with "@gmail.com"
#"Other email provider" otherwise

valid_email=input("@")
Gmail_account=input("@gmail.com")

if valid_email=="@":
    print("valid email")
else:
    print("not valid")
    
elif: Gmail_account="@gmail.com"
print("gmail account")
else 
print("other email account")



Write a program that checks password strength:
"Weak" if length < 6
"Moderate" if length 6–10 and contains at least one digit
"Strong" if length > 10 and contains both digits and uppercase letters
4.
Write a program that checks a password:
"Invalid" if it does not start with a capital letter
"Invalid" if it does not end with a number
"Valid password" otherwise
5.
Write a program that takes a number and checks:

"Fizz" if divisible by 3
"Buzz" if divisible by 5
"FizzBuzz" if divisible by both
Otherwise print the number

6.
Create a program that takes a score and prints a grade:
A (≥ 80)
B (70–79)
C (60–69)
D (50–59)
F (< 50)

7.
Create a program that takes two numbers and prints:
"Equal" if same
"First is greater"
"Second is greater"

8.
Write a program that takes a day number (1–7) and prints:
Weekday (1–5)
Weekend (6–7)
Invalid input otherwise

9.
Create a program that takes a temperature and prints:
"Freezing" if ≤ 0
"Cold" if 1–15
"Warm" if 16–30
"Hot" if > 30

10.
Create a program that takes a year and prints:
"Leap year" if divisible by 4
"Century year" if divisible by 100
"Common year" otherwise