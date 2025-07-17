#print("hello world")#function print()
#print('i am a good boy\nand also good student')
#print("hello \"hello\"hello")#escape sequence character
#a=1010101
#a1=1010
#print(a)
#ashish='b'
#b='ashish'
#print(b)
#print(a + a1)
#print('the type of a is',type(a))
#print(type(b))
#c=complex(6,2)
#print(c)
#list=[8,2.3,[-4,5],['apple','banana']]
#a='a'
#b='b'
#print(a+b)
#a=input('enter a number ')#always a string
#print('my name is',a)
#x=input('enter first num  ')
#y=input('enter second num  ')
#print(x+y)
#print(int(x)+int(y))
#name='ashish'
#print('hello ',name)
#print(name)
#hello='hello ashqoo \n how are you '
#print(hello)
#print('hello,'+name)
#print(name[0],name[1])
#for character in hello:
#  print(character)
#strings are immutable
a='ashqoo!'
print(len(a))
print(a.upper())
print(a.rstrip("!"))
print(a.replace('ashqoo','ashish'))
#print(a.split(''))
blogashish='intro to python'
print(blogashish.capitalize())
str1='welcome to the console!!!'
print(str1.center(50))
print(a.count('s'))#at index 1
print(str1.endswith('!!!'))
print(str1.endswith("to",4,10))
print(str1.find('is'))#no - return -1
print(str1.find('to'))
str1='welcometoconsole'
print(str1.isalnum())#alphanumaeric
print(str1.isalpha())
str1='Welcome000'
print(str1.isalpha())
print(str1.islower())
print(str1.isupper())
print(str1.isprintable())#$ if any \n present then false
str1='    '
print(str1.isspace())
print(str1.istitle())#if first letter is capital then will return true
print(str1.startswith("python"))
str1='hello'
print(str1.swapcase())#if null returns false
name='ashish'
#print(name[0:5])#string slicing
len1=len(name)
#print(len1)
#print(name[:4])
#print(name[:])
#print(name[0:len(name)-3])
#print(name[:-1])#-3
print(name[-1:len(name)-1])
print(name[-1:-3])
print(name[-3:-1])#2:4 including 0 but not 4
nm='harry'
print(nm[-4:-2])
