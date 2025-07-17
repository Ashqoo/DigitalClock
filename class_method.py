class employee:
  company='apple'
  def show(self):
    print(f"The name is {self.name} and company is {self.company}")

  @classmethod#class method decoration
  def changecompany(cls, newcompany):#here cls is class variable and it is used to change the class variable by default 
    cls.company = newcompany


e1 = employee()
e1.name ='ashish'
e1.show()
e1.changecompany('tesla')
e1.show()
print(employee.company)
