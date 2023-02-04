#ex1 
thislist = ["apple", "banana", "cherry"]
print(thislist)

#ex2
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#ex3
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#ex4
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#ex5
list1 = ["abc", 34, True, 40, "male"]

#ex6
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#ex7
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#ex8
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#ex9
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#ex10
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#ex11
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#ex12
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#ex13
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#ex14
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#ex15
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#ex16
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#ex17
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) 

#ex18
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#ex19
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#ex20
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#ex21
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#ex22
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#ex23
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#ex24
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#ex25
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#ex26
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#ex27
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#ex28
thislist = ["apple", "banana", "cherry"]
del thislist

#ex29
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#ex30
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#ex31
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#ex32
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#ex33
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#ex34
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#ex35
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#ex36
newlist = [x for x in fruits if x != "apple"]

#ex37
newlist = [x for x in fruits]

#ex38
newlist = [x for x in range(10)]

#ex39
newlist = [x for x in range(10) if x < 5]

#ex40
newlist = [x.upper() for x in fruits]

#ex41
newlist = ['hello' for x in fruits]

#ex42
newlist = [x if x != "banana" else "orange" for x in fruits]

#ex43
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#ex44
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#ex45
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#ex46
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#ex47
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#ex48
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#ex49
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#ex50
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#ex51
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#ex52
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#ex53
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#ex54
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#ex55
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#ex56
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#ex57
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

#ex58
fruits = ["apple", "banana", "cherry"]
fruits.append('orange')

#ex59
fruits = ["apple", "banana", "cherry"]

fruits.insert(1,"lemon")

#ex60
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#ex61
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#ex62
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#ex63
fruits = ["apple", "banana", "cherry"]
print(len(fruits))