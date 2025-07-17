#sets
#collection of well defined objects
#to unrepeadtly store a collection of data
#sets are unordered, unchangeable, and do not allow duplicate values
#sets are written with curly brackets
thisset={2,4,2,6}
print(thisset)
info={'ashqoo',19,False,5.9,19}
print(info)#doesn't maintain any order
#sets are unchangeable meaning we cannot change items of the set once created
print(type(info))
ashish={}
print(type(ashish))#this is a dictionary
ashish=set()
print(type(ashish))#this is a empty set
#accessing set items
for i in info:
  print(i)

#set methods
#union() and update()
s1={1,2,3,5,3}
s2={3,4,6,7}
print(s1.union(s2))
print(s1,s2)
print(s1.update(s2))
print(s1,s2)
#intersection() and intersection_update()
print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1)
#symmetric_difference() and symmetric_differnce_update()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.difference(cities2)
print(cities)
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = { "Seoul", "Kabul"}
print(cities.isdisjoint(cities2))
cities3 = { "Tokyo", "Delhi", "Madrid"}
print(cities.issuperset(cities3))
print(cities3.issubset(cities))

print(cities.add("england"))
cities.add('england')
print(cities)
cities.remove('england')
print(cities)
cities.discard('tokyo')#tokyo is not present in the set so it will not throw an error
print(cities)
item=cities.pop()#remove any random item
print(cities)
print(item)
del cities
#print(cities) deleted
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")

