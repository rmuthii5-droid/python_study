doctor_in=input("enter and sit down ")
doctor_in="enter and sit down"
doctornot_in=input("book date ")
doctornot_in=int()
doctornot_in={26042026, 23052026, 24062026 }

if doctor_in=="enter and sit down" :
    print("enter and sit down")
elif doctornot_in=={26042026, 23052026, 24062026 }:
    print("book date")
else:
    print("hospital closed")

doctor_in = input("Enter instruction: ")
doctornot_in = int(input("Enter booking date (e.g. 26042026): "))

available_dates = {26042026, 23052026, 24062026}

if doctor_in == "enter and sit down":
    print("enter and sit down")

elif doctornot_in in available_dates:
    print("book date")

else:
    print("hospital closed")
    

