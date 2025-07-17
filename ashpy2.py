def average(a=9, b=10):  #indentation
  print("the average is ", (a + b) / 2)  #floating point division
average(1, 5)
average(4, 9)
def calculateGmean(a, b):
  mean = (a * b) / (a + b)
  print(mean)
calculateGmean(5,6)
def isgreater(a=5,b=6):
  if(a>b):
    print('a is greater')
  else:
    print('b is greater')
isgreater(9)#here a=9 & b=default b=6
def islesser(a,b):
  pass


a=9
b=10
isgreater(a,b)
calculateGmean(a,b)

def average1(a,b,c=0):
  print('the average number is ',(a+b+c)/3)

average1(5,6)
average1(0,0)

def average2(*number):
  print(type(number))
  sum=0
  for i in number:
    sum=sum+i
  print('average is ',sum/len(number))
  #return sum/len(number)
  

average2(5,6.4,7,8.1)#list#=c
#print(c)

def average3(**name):
  print(type(name))
  print('hello',name['fname'],name['mname'],name['lname'])
  #name(mname="ashish",lname='ashqoo',fname='ranjan')

average3(mname='ashish',lname='ashqoo',fname='ranjan')



