#LAMBDA FUNCTION

#def double(x):
 # return x*2

def appl(fx,value):
  return 6+fx(value)
  
double =lambda x:x*2
print(double(5))
cube=lambda x:x*x*x
print(cube(5))
avg=lambda x,y,z:(x+y+z)/3
print(avg(5,3,5))
# if you want to pass more than one argument then you can use lambda function
#you can also pass function as an argument
#lambda function is an annonymous function
print(appl(cube,2))