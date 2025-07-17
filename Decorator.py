#DECORATORS

def greet(fx):
  def mfx():
   print('good morning')
   fx()
   print('this for using this functions')
  return mfx 

@greet#decorator name
def hello():
  print('hello world')

hello()

greet(hello)()#this is also a decorator

#decorators are used to change the behaviour of a function without modifying the function itself


def greet(fx):
  def mfx(*args,**kwargs):
   print('good morning')
   fx(*args,*kwargs)
   print('this for using this functions')
  return mfx 

#@greet#decorator name
def add(a,b):
  print(a+b)

greet(add)(1,2)
#add(1,2)

#LOG FUNCTION






  