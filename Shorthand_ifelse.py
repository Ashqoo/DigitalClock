#short hand if-else
a=330
b=3303
print("A") if a>b else print("=") if a==b else print("B")
c=9 if a>b else 0
print(c)

#enumerate function
marks=[12,56,32,98,12,45,1,4]
index=0
for mark in marks:
  print(mark)
  if(index == 3):#pylinter
    print("ashish , awesome!")
  index+=1  

#by using enumerate function
for index,mark in enumerate(marks):
  print(mark)
  if(index==3):
    print("ashish ,awesome!")



