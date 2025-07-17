#dictionary
dic={'harry': 'human being',
     'spoon':'object'}
print(dic['harry'])
print(dic.get('spoon'))
print(dic.keys())
print(dic)
for key in dic.keys():
  print(dic[key])

for value in dic.values():
  print(value)

for key in dic.keys():
  print(f"the value corresponding to the key {key} is {dic[key]}")

print(dic.items())
for key,value in dic.items():
  print(f"the value corresponding to the key {key} is {value}")
#dictionary are used to create a mapping of some datas like employees performance,grossary ka price,item code,item names,item quantity

dic={
  344:'harry',#keys:value
  56:'ashish',
  634:'zakir',
  567:'neha'

}
print(dic[567])
#dictionary is ordered collection of data items.they store multiple items in a single variable.
#dictionary items are key value pairs that are separated by commas and enclosed within curly brackets.

#methods of dictionary
ep1={122:45,123:89,567:69,670:69}#employee id:performance#ep1 is a senior manager
ep2={222:67,566:90}#junior manager
#ep2.update(ep1)#update method
#ep1.update(ep2)
#ep1.clear()
#print(ep2)
#print(ep1)
#print(ep1)
empt={}
print(empt)
print(type(empt))
ep1.pop(123)
ep1.popitem()
print(ep1)
#del ep1
#print(ep1)
del ep1[122]
print(ep1)

