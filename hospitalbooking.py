doctor_in = input("Enter and sit down: thank ")
doctornot_in = int(input("Enter booking date: "))

available_dates = (26042026, 23052026, 24062026)

if doctor_in == "enter and sit down":
    print("enter and sit down")

elif doctornot_in in available_dates:
    print("book date")
else:
    print("hospital closed")