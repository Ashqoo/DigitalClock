#HIGHER ORDER FUNCTIONS
#A function that accepts another function as an argument
#A function that returns another function
#MAP

def cube(x):
  return x*x*x

print(cube(2))

l=[1,2,3,4,5,6]
#newl=[]
#for item in l:
 # newl.append(cube(item))
#print(newl)

newl=map(cube,l)
print(newl)#returns ap object
newl=list(map(cube,l))
print(newl)

#FILTER
def filter_function(a):
  return a>=2

newnewl=list(filter(filter_function,l))
print(newnewl)
new2=list(filter(lambda x:x>2,l))
print(new2)
          

#REDUCE
from functools import reduce
num=[1,2,3,4,5]
#num=[3,3,4,5]
#num=[6,4,5]
#num=[10,5]
#num=[15]
sum=reduce(lambda x,y:x+y,num)
print(sum)
