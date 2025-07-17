#file iO


#READING A FILE
# f=open('myfile.txt', 'r')#r-for ride,w-for write,a-for append
#print(f)
# text=f.read()# r mode is always default
# print(text)
# f.close
# if rb mode is given then it will open binary files like image,pdfs,jpg etc

#WEITING A FILE
# f=open('myfile.txt','a')
# f.write('hello world!')
# f.close()

# with open('myfile.txt','a')as f:
#   f.write("hey i am ashish")


#FILE HANDLING METHODS :-

#f= open('myfile.txt',"r")
# while True:
#   line=f.readline()
#   print(line)
#   if not line:
#     print(line,type(line))
#     break

#   #print(line)
# i=0
# while True:
#   i=i+1
#   line=f.readline()
#   if not line:
#     break
#   m1= int(line.split(",")[0])  
#   m2= int(line.split(",")[1])  
#   m3= int(line.split(",")[2])  
#   print(f"marks of students {i} in maths is: {m1*2}")
#   print(f"marks of students {i} in maths is: {m2*2}")
#   print(f"marks of students {i} in maths is: {m3*2}")


#   print(line)

# f=open('myfile.txt','w')
# lines=['line1\n','line2\n','line3\n']
# f.writelines(lines)
# f.close()





with open('myfile2.txt','r') as f:
  print(type(f))
  #move to the 1oth byte in the file
  f.seek(10)
  #read the next 5 bytes
  print(f.tell())
  data=f.read(5)
  print(data)
  # f.seek(f.file())

with open('sample.txt','w')as f:
  f.write('hello world')
  f.truncate(5)
#print only 5 bytes from the file
with open('sample.txt','r')as f:
  print(f.read())
  