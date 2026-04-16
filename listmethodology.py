#LISTMETHODOLOGY  is manipulating list with functions inside class list
#used to manipulate or modify a list of data
my_list= ["mary","john","mike", 100,200, True,False]


#REMOVE
#remove function. remove a specified item with specific value eg
my_list.remove(100)
print(my_list)


#POP
#pop remove the item with specified index if you fail to indetifies it remove the last item
my_list.pop(2)
print(my_list)

#APPEND add an an item at end of list 
my_list.append("mango")
print(my_list)

#INSERT
#add an item with specified index
my_list.insert(1,"richard")
my_list.insert(5,1000)
print(my_list)
#

lst=[10,20,30,["mary","john","mike", [1000,2000,3000]], 40,50]
#add 70 at end of list
#add jane between mary and john
#add 1500 between 1000 and 2000
lst.append(70)
print(lst)

#add jane btw mary and john

lst[3].insert(1,"jane")
print(lst)


#add 1500 btw 1000 and 2000

lst[3][4].insert(1, 1500)
print(lst)

#delete 2000
lst[3][4].pop(2)
print(lst)


#count
list2= ["mary","john","mike","john"]
list2.count("john")
print(list2)

#sorting 
list2.sort()
print(list2)


#extending
list2= ["mary","john","mike","john"]
list1=[20,40,50]
list2.extend(list1)
print(list2)
