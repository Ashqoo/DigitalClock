class employee:
  def __init__(self,name):
    self.name= name

  def __len__(self):
    i=0
    for item in self.name:#dunder method 
      i=i+1
    return i
  def __str__(self):
     return f"The name of the employee is {self.name}"
  def __repr__(self):
     return f"employee {self.name}"
  def __call__(self):
    print("hye i am good ")
  
e = employee("ashqoo")
print(e)
print(str(e))
print(repr(e))
e()