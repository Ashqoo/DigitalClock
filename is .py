#is vs ==
#is compare exact location of object in memory(identity)
#== compare value

a=4
b='4'

print(a is b) #exact location of object in memory or leveraging to one emmory location or pointing to same address
# all immutable value will return True in case of "is" comparision operator
print(a == b) #value

a=[1,2,43]
b=[1,2,43]

# a=(1,2)
# b=(1,2)

# a=None
# b=None

print(a is b)
print(a is None)
print(a == b)
#here python create only one list constamt in memory and both list are same so it return true
#both list pointing same memory located object value

