# ex1
thisset = {"apple", "banana", "cherry"}
print(thisset)  

# ex2
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

# ex3
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

# ex4
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# ex5
set1 = {"abc", 34, True, 40, "male"}

# ex6
myset = {"apple", "banana", "cherry"}
print(type(myset))

# ex7
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# ex8
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# ex9
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

# ex10
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# ex11
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# ex12
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

# ex13
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

# ex14
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

# ex15
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

# ex16
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

# ex17
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

# ex18
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# ex19
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# ex20
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# ex21
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

# ex22
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

# ex23
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

# ex24
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

# ex25
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

# ex26
fruits = {"apple", "banana", "cherry"}
fruits.add('orange')

# ex27
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#ex28
fruits = {"apple", "banana", "cherry"}
fruits.remove('banana')

#ex29
fruits = {"apple", "banana", "cherry"}
fruits.discard('banana')
