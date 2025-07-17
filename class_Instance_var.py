#INSTANCE VARIABLE
#we use class variable to store data
#oops gives us a logical grouping of data and functions
class employee:
  companyname='apple'#class variable is same for all objects
  noOfemployee=0
  def __init__(self,name):
    self.name=name
    self.raise_amount=0.02#instance variable can be accessed only by the instance of the class
    employee.noOfemployee +=1

  def showdetails(self):
    print(f"the name of the employee is {self.name} and the raise amount in {self.noofemployee} sized {self.companyname} is {self.raise_amount}")

emp1=employee("ashish")
emp1.raise_amount=0.3
emp1.companyname='apple india'# here for emp1 companyname is changed
#here class variable acts like instance variable
employee.companyname='google'
emp1.showdetails()
emp2=employee("harry")
emp2.showdetails()
print(employee.companyname)
#if class variable found a local variable then it will take the local variable value
