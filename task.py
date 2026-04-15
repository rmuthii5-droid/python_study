#convert to round
temp=55.5464 
temp=round(55.5464)
print(temp)

#convert to float55.8926 to 55.893
temp=55.8926
temp=round(temp,3)
print(temp)

#convert to temp 55.8926 to string for easy slicing to 8.926
temp=55.8926
temp=str(temp)
#slice
temp=temp[3:] #8926
#8 +"."+926

temp=temp[0]+"."+temp[1:]
temp=float(temp)
print(temp)