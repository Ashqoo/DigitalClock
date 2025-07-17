
#dir(),__dict__ attribute,help()
x=[1,2,3]
print(dir(x))
print(x.__add__)#method_wrapper
class person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
    self.version=1

p=person('john', 30)
print(p.__dict__)#creates dictionary of the object 
#print(help(str))
#print(help(person))

