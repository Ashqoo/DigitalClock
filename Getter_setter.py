#GETTERS & SETTERS
class MyClass:
  def __init__(self,value):
    self._value=value
  def show(self):
    print(f"value is {self._value}")
#here MyClass class has a single property _value.
#getter is used to get the value of _value.
#setter is used to set the value of _value.
#getters do not take any parameters and setter take a parameter
#we cann't set the value through getter

  @property#property decorator#getter
  def ten_value(self):#arguments 0,1,2,3,continue
    return 10*self._value
#setter method is defined using @property_name.setter decorator
  @ten_value.setter#setter
  def ten_value(self,new_value):
    self._value=new_value/10

obj=MyClass(10)
obj.ten_value=67
print(obj._value)
print(obj.ten_value)
obj.show()
'''getters in python are methods that are used to access the values of an object's properties.they are used to return the value of a specific property,and are typically defined using the @property decorator.the getter method is called whenever you access the value of an object's property and it should return the value of that property'''
