## append is use for add single element in list
"""
mylist = [10,20,30,40]
print("Original list",mylist)
print(type(mylist))
mylist.append(50)
mylist.append(60)
mylist.append(70)
print(f"New list : {mylist}")

"""
## insert method [0,1,2,3.....]
"""
mylist = [10,20,30,40]
print("Original list",mylist)

mylist.insert(1,50)
print(f"New list : {mylist}")
"""
## Extend method is use for add multiple element
"""
mylist = [10,20,30,40]
print("Original list",mylist)

mylist.extend([50,60,70])
print(f"New list : {mylist}")
"""

"""
list1 = [1,2,3,4]
list2 = [5,6,7,8]

new_list = list1 + list2
print(f"Original list is : {new_list}")
# pop is used for remove last element
new_list.pop() 
print(f"New list : {new_list}")
"""

## remove, delete, clear
"""
list1 = [1,2,3,4,5,6,7,8]
# list1.remove(2)
# del list1[2]
list1.clear()
print(list1)
"""

## Range
# range(start, end, step)
"""
for i in range(1,50,2):
    print(i)
"""

## Set

"""myset = set([10,20,30])
print(f"Original set : {myset}")
# myset.add(40)
# myset.add(200)
myset.update([50,60,70])
print(type(myset))
print(f"New set is :{myset}")
"""

## id
"""
name = 'Shubham'
print(id(name))

name = 'chouhan'
print(id(name))
"""

## Tuple
"""
mytuple = (1,2,3,4,5)

print(mytuple)
print(type(mytuple))
"""

## Dictonary 
"""
mydict = {1:"Shubham",2:"Chouhan",3:"Naina"}
print(mydict)
print(type(mydict))
# for key values
print(mydict.keys()) 
print(mydict[2])

# adding element in dictonary
mydict["Rahul"]=10
print(mydict)
"""

## If and else condition

"""
a = 1

if a > 0:
    print("A is a positive number")
else :
    print("A is a negative number")
"""

## loops -- for and while

# for 
sum = 0
for i in range(1,5):
    print(i)
    sum += i
    i += 1 
print("Sum of first 5 number is", sum)

# while 

i = 1
while 1:
    if i == 9:
        break
    print(i)
    i += 1