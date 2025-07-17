#ACCESS MODIFIER/SPECIFIER
#there is not exact access modifier in python
#but there is a concept of access modifier
#Public
class Employee:
  def __init__(self):
    self.name="ashish"

a=Employee()
print(a.name)
#private
class Employee1:
  def __init__(self):
    self.__name="ashish"#__ indication

a=Employee1()
#print(a.__name)
print(a._Employee1__name)#can be accessed indirectly
#name mangling
print(a.__dir__())
# class Student: 
#     def __init__(self, age, name): 
#         self.__age = age      # An indication of private variable
        
#         def __funName(self):  # An indication of private function
#             self.y = 34
#             print(self.y)

# class Subject(Student):
#     pass

# obj = Student(21,"Harry")
# obj1 = Subject

# # calling by object of class Student
# print(obj.__age)
# print(obj.__funName())

# # calling by object  of class Subject
# print(obj1.__age)
# print(obj1.__funName())


# -------------------------
# class MyClass:
#    def __Init__(self):
#       self._private_attribute =" I am a Private Attribute"
#       self.__mangled_attribute="I am a mangled Attribuet"

# my_obj=MyClass()

# print(my_obj._private_attribute)
# print(my_obj.__mangled_attribute)
# print(my_obj._MyClass__mangled_attribute)









#protected
class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName()) 
