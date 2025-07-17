#string formating
l="hey my name is {1} and i am from {0}"
country="india"
name="ashish"
print(l.format(country,name))

#f-string
print(f"hey my name is {name} and i am from {country}")#populating value of string

txt="for only {price:.2f} dollars!"
print(txt.format(price=49.354))

price=49.354
txt=f"for only {price:.2f} dollars!"
print(txt)

print(type(f"{2*30}"))

print(f"hey my name is {{name}} and i am from {{country}}")

#docstring
def square(n):
  #print(n)
  '''takes in anumber n,returns the square of n''''''docssring of function square (if we change docsstring programm may be changed )'''
  print(n**2)
square(5)
print(square.__doc__)#doc attribute #python totally ignores docstring
#docstring must declared just after the function name

'''pep8 is a document that provides guidelines and best practices on how to write python code.it was written in 2001 by guido van rossum,Barry warsaw,and nick coghlan.the primary focus of pep8 is to improve the readability and consistency of python code
'''
#python enhancement proposal
#zen of python
import this

