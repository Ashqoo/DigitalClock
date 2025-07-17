#SINGLE INHERITANCE
class animal:
  def __init__(self, name, species):
    self.name= name
    self.species= species

  def make_sound(self):
    print('sound made by the animal')

class dog(animal):
  def __init__(self, name, breed):
    animal.__init__(self, name,species='dog')
    self.breed=breed

  def make_sound(self):
    print('bark')#overriden method


d= dog('dog','doggerman')
d.make_sound()

a=animal('dog','dog')
a.make_sound()

#MULTIPLE INHERITANCE
class employee:
  def __init__(self, name):
   self.name= name

  def show(self):
    print(f"the name is {self.name}")

class dancer:
    def __init__(self, dance):
     self.dance= dance
    def show(self):
        print(f"the dance is {self.dance}")


class danceremployee(employee, dancer):#here first employee lass will inherited then dancer class
  def __init__(self, dance, name):
    self.dance= dance
    self.name= name

o= danceremployee('kathak', 'satya')
print(o.name,o.dance)
o.show()
print(danceremployee.mro())#it will show the order of inheritance


#MULTILEVEL INHERITANCE
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")
        
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color
        
    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")

o= GoldenRetriever('tommy', 'black')
o.show_details()
print(GoldenRetriever.mro())

#HYBRID INHERITANCE
class baseclass:
  pass

class derived1(baseclass):
  pass

class derived2(baseclass):
  pass

class derived3(derived1, derived2):
  pass


#HIERARCHICAL INHERITANCE

class baseclasss:
   pass

class derived_class1(baseclasss):
   pass

class derived_class2(baseclasss):
   pass

class derived_class3(derived_class1):
   pass

class derived_class4(derived_class2):
   pass