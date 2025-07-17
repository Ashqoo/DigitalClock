class math:
  def __init__(self,num):
    self.num=num

  def addtonum(self,n):#by using self we can access the object of that method
     self.num=self.num+n

  @staticmethod#it can call without creating object
  def add(a,b):#here we can't use self because it is static method ,there is no object in static method(not need to pass self argument)
    return a+b
result=math.add(1,2)
# result=math
print(result)
a=math(5)
print(a.num)
a.addtonum(result)
print(a.num)