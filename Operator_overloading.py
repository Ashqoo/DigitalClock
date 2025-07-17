#pypdf
#OPERATOR OVERLOADING
class vector:
  def __init__(self, i, j,k):
    self.i=i
    self.j=j
    self.k=k

  def __str__(self):
    return f"{self.i}i + {self.j}j + {self.k}k"#3i+5j+6k
  def __add__(self,x):
#    return f"{self.i + x.i}i + {self.j +x.j}j+ {self.k+ x.k}k"#3i5j6k
     return vector(self.i + x.i,self.j +x.j,self.k+ x.k)#3i5j6k #vector constructor for vector

v1=vector(3, 5, 6)
print(v1)
v2=vector(1, 2,3)
print(v2)

print(v1+v2)
print(type(v1+v2))