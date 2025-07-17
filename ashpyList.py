#lists are mutable means we can update by our choice
marks=[3,6,4,'ashish',True]#list character/items always in square bracket
print(marks)
print(type(marks))
print(marks[0],marks[1],marks[2])
print(marks[-3])#negative index
print(marks[len(marks)-3])#positive index

if 7 in marks:
  print('yes')
else:
  print('no')
if "6" in marks:
  print('yes')
else:
  print('no')
if 'as' in 'ashish':
  print('yes')
#same things applies for strings as well

print(marks)
print(marks[:])
print(marks[:7])
print(marks[1:-1])#string slicing
print(marks[1:4])
print(marks[1:4:2])#jump index

#list comprehension
list=[i*i for i in range(10)]
print(list)
list=[i*i for i in range(10) if i%2==0]
print(list)

#list manipulation
l=[11,45,1,2,1,4,6]
print(l)
l.append(7)#add at the end
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)
print(l.index(11))
print(l.count(1))
m=l
m[0]=0
print(l)
m=l.copy()
print(m)
l.insert(1,899)
print(l)
m=[900,1000,1100]
l.extend(m)
print(l)
k=l+m
print(k)

thislist = list(("apple", "banana", "cherry"))
print(thislist)
