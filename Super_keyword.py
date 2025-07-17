#SUPER KEYWORD
#used to reffer the parent class
class parentclass:
  def permanent_method(self):
    print('this is  the parent method')

class childclass(parentclass):
  def parent_method(self):
    print('ashish')
  def child_method(self):
    print('this is the child method')
    super().permanent_method()

child_object = childclass()
child_object.child_method()
child_object.parent_method()

####
class employee:
  def __init__(self, name, id):
    self.name=name
    self.id=id

class programmer(employee):
  def __init__(self, name, id ,lang):
    super().__init__(name, id)
    self.lang=lang

rohan=employee('rohan','420')
harry=programmer('harry','2332','python')
print(harry.name)
print(harry.id)
print(harry.lang)