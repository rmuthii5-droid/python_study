doctor_in = input("Enter and sit down: thank ")
doctornot_in = int(input("Enter booking date: "))

if doctor_in == "enter and sit down":
    print("enter and sit down")

elif doctornot_in in available_dates:
    print("book date")
else:
    print("hospital closed")


    grade = 'B'

match grade:
    case 'A':
        print("Excellent!")
    case 'B':
        print("Good!")
    case _:
        print("Not specified.")