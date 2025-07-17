tup=(1,5,6,7,8,9,10,11,12,13)
print(type(tup))
print(type(tup),tup)#immutable
print(tup[0],tup[8])
print(tup[-4])
if 11 in tup:
  print('yes')
tup2=tup[1:5]#tupple slicing
print(tup2)
#same as list operations
#have to do
'''tuples are immutable if we want to change something in the tuple so we have to convert the tuple into list and then change the list and then convert the list into tuple'''

#tupple manipulation
contries=('india','itally','india','england','geramany')
temp=list(contries)
temp.append("russia")
temp.pop(3)
temp[2]='finland'
contries=tuple(temp)
print(contries)
contries2=('vietnam','china')
southeastasia=contries+contries2
print(southeastasia)
tuple1=(0,1,21,3,4,5,6,7,2,2)
print(tuple1.count(2))
print(tuple1.index(2))
print(tuple1.index(2,4,10))
print(len(tuple1))

