#? print Hello
print("hello")

#?comments in python
"""
This is comments in python
"""
print('comments are shown above')

#?assign value to single variable
a=12
print(a)

#?assign value to the multiple variables
x,y,z="Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#?different variables have same 
x=y=z="orange"
print(x)
print(y)
print(z)

#?unpack collection
fruits=["orange","apple","grapes"]
a=b=c=fruits
print(a)
print(b)
print(c)

x = "Python is awesome"
print(x)

#?know the type of variable
x = 5
print(type(x)) 

y=4.6
print(type(y))

z="name"
print(type(z))

p=2/3
print(type(p))

a=2
b=2
c=a is b
print(type(c))

#? slicing strings
b="hello world"
print(b[:5])
print(b[1:5])

#? modify string
#!uppercase
a="Hello world"
print(a.upper())

#!lowercase
b="hello world"
print(b.lower())

#!remove whitespace
c=" Hello , world "
print(c.strip())             #!removing the white space
print(c)

#!replace method
a="Hello,world"
print(a.split(","))

#?concatenate string
a="hello"
b="world"
c=a+" "+b
print(c)

#?format string
a=23
b="hello my name is abhinandan and i am {}"
print(b.format(a))

a="hello my name is {}{}{}{}"
b="abhinandan "
c="and i am "
d= 23
e=" years old"
print(a.format(b,c,d,e))

#?escape characters
text="hello my name is \"abhinandan\" and i am 23 years old"
print(text)

#************************ python operators********************
#!Airthmatic operators
a=2
b=4
print(a+b)  #?addition
print(b-a)  #?substraction
print(a*b)  #?multilication
print(b/a)  #?divide
print(b//a) #?floor division
print(a%b)  #?modulus
print(a**b)  #?exponantiation


#!Comparison operator
a=6
b=5
print(a==b)
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)
print()

#!Assignment operator
a=6
a +=3
b=4
b -=2
c=5
c *=2
d=10
d //=2
e=12
e >> 2
print(a)
print(b)
print(c)
print(d)
print(e)

#!Logical operator
x=5  
print(x>3 and x<7)
print(x>3 or x<7)

#! identity operator
a=6
b=7
print( a is b)
print( a is not b)

#! membership operator
a=[1,2,3,4,5]
b=4
print(b in a)
print(b not in a)

#! bitwise operator
a=5
b=7
print(a & b)
print(a | b)
print(~ a)
print( ~ b)


#!list
a=['abhi','nandan','khatri']
print(a)
print(len(a))

#!access items from the list
li=['abhi',1,'nandan',2]
print(li[1])

#!change the list items
thislist=["apple","mango","banana"]
# thislist[1]='orange'
thislist[:-1]='orange'
# print(thislist)
print(thislist)

#!append
values=['a','b','c','d']
values.append('e')
print(values)

#!remove
values=['a','b','c','d']
values.remove('d')
print(values)

#!pop in list
stack=[]
stack.append('a')
stack.append('b')
stack.append('c')
print(stack)

print(stack.pop(1))     #remove item using indexing
print(stack.pop())   #give the last item of the list


#!delete item
list1=['apple','mango','orange']
del list1[1]     #delete item from first number using list
print(list1)

#!insert method in list

a=['apple','mango','orange']
a.insert(1,'tomato')             #INSERT IS USED TO APPEND ITEM IN PARTIACULAR  POSITION USING NAME
print(a)


#!extend method in list
c=['apple','mango','grapes','tomato']
d=['potato','milk']              #is used to append list in list
c.extend(d)
print(c)

#!loop on the list
items=['i','will','perfect','today']
for i in items:
    print(i)

#!use range in list
for j in range (len(items)):
    print(j)

#!list comprenhension
comp_list=['apple','mango','bananan','orange']
blank_list=[]
for i in comp_list:
    print(i) 
    if 'n' in i:    # use condition to append items who has n in words
        blank_list.append(i)
print(blank_list)


#*comprehension in one list
fruits=['apple','grapes','mango','orange']
print(fruits)
new=[i for i in fruits if "a" in i]
print(new)

# !sort list
list1=['a','b','c','x','g','i']
list1.sort()
print(list1)

#! sort the list in reverse order
list_display=[1,9,4,2,3,8,6]
list_display.sort(reverse=True)
print(list_display)

# ! sort the list with words
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

#!copy list
thislist=['apple','mango','banana','peas']
elist=thislist.copy()
print(elist)

#!join list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
print(list1 + list2)

#***************** ____________   Python-Tuples  _______________ ***************************
thistuple=('apple','mango','banana')
print(thistuple)

 #!tuple duplicate
thistuple=('apple','mango','apple','apple','banana')
print(thistuple)

#!access tuple items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#! update in tuples
x=('apple','mango','banana')
y=list(x)   #converted tuple into list
y[1]='kiwi'
print(tuple(y))

#!add value in tupel
thistuple = ("apple", "banana", "cherry")
y=('orange',)
thistuple+=y
print(thistuple)

#!remove item from tuple
thistuple = ("apple", "banana", "cherry")
y=list(thistuple)
y.remove("apple")
print(tuple(y))

#!delete tuple
thistuple = ("apple", "banana", "cherry")
del thistuple


#!unpack tuples
thistuple = ("apple", "banana", "cherry")
(a,b,c)=thistuple
print(a)
print(b)
print(c)

#!loop in tuples
thistuple = ("apple", "banana", "cherry")
for i in thistuple:
    print(i)

#!loop in length of tuple
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(i)

#!join tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#!multiply tuples
tuple1 = ("a", "b" , "c")
tuple2=tuple1 * 2
print(tuple2)

#**********************     Python-sets   ***************
thisset = {"apple", "banana", "cherry"}
print(thisset)

#!loop the set
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#!add item to the set 
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#!@update complete list
thisset = {"apple", "banana", "cherry"}
thisset1 = {"mango", "tomato", "pear"}
thisset.update(thisset1)
print(thisset)

#! add element of the list to the set
thisset={"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)


#!remove item from the list
thisset = {"apple", "banana", "cherry"}
thisset.remove("apple")
print(thisset)

#!loop on the set
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#!join set
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3=set1.union(set2)
print(set3) 

#!update
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#!python dictoneries
#*print value of dict from key name
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
#*print length of dict
print(len(thisdict))

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict[ "colors"])

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

#!get all the keys of dict
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.keys())
print(thisdict.values())

#!add new item to the dict
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(car.keys())
#**add item
car["color"]="white"
print(car)

#!change items of dictonery
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
car["year"]=2022
print(car)

#!update dictonery
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"brand":"nano"})
print(thisdict)

# !remove items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#!popitem
#***popitem is used to removed the last inserted item from the list
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#!del
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#**delete complete dictonery
thisdict= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
# print(thisdict)

#!clear method for empty dictonery
thislist = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thislist.clear()
print(thislist)

#!loop on the dictonery
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for i in thisdict:
    print(thisdict)

#!get the values of dict using loop
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for i in thisdict.values(): #?get values
    print(i)
for j in thisdict.keys(): #?get keys
    print(j)
for x, y in thisdict.items(): #?get both
  print(x, y)    

#!copy dictonery
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
this=thisdict.copy()
print(this) 

#!nested dictonery
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child1"]["name"])
