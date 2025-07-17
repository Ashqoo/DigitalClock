#class method as alternative constructor

class employee:
  def __init__(self, name, salary):#this is a normal constructor
    self.name=name
    self.salary=salary

  @classmethod
  def fromstr(cls, string):#this is a class method as alternative constructor
    return cls(string.split('-')[0], int(string.split('-')[1]))


e1 = employee('ashish', "12000")
print(e1.name)
print(e1.salary)

string='ashish-12000'
e2=employee.fromstr(string)
#e2=employee(string.split('-')[0], string.split('-')[1])
print(e2.name)
print(e2.salary)

class person:
  def __init__(self, name, age):
    self.name=name
    self.age=age

  @classmethod
  def from_string(cls, string):
    name, age=string.split(',')
    return cls(name, int(age))

person = person.from_string("John Doe,30")
print(person.name, person.age)