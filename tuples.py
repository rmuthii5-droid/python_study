#used to store multiple diffrent data
# immutable - tuples are stuborn [ t make tuple convertable turnit into list. we use list function]
# ordered
# enclosed in normal brackets( )
days_of_week=("sun","mon","tue","wed","thur","friday","saturday",)
print(type(days_of_week))
print(days_of_week [2:4])
print(days_of_week[1])
print(days_of_week[6])
print(days_of_week[4:7])
#changing tuple to list
days_of_week=list (days_of_week)
print(type(days_of_week))
days_of_week[2]="tuesday"
days_of_week[1]="sunday"
days_of_week.append("january")
print(days_of_week)
days_of_week=tuple(days_of_week)
print(type(days_of_week))