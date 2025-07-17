 #oops
def hello():
  print('hello')
hello()

class person:
  def __init__(self,name,o):#constructor#always invoke when object is created
    print('hay i am a person')
    self.name=name
    self.occ=o
    
    
  
  def info(self):#self parameter
    print(f"{self.name} is a {self.occ}")

a=person('ashish','developer')
b=person('harry','HR')

#a.name='harry'
#a.occupation='accountant

#print(a.name ,a.occupation)
a.info()
b.info()


#CONSTRUCTOR

