#Exception handling
#a=input('enter the number: ')
#print(f"multiplication table of {a} is:")
#try:
 #for i in range(1,11):
#  print(f"{int(a)} X {i} = {int(a)*i}")
#except Exception as e:
  #print(e)
#except:
#  print("invalid input")
#print('end of program')

#try: 
#  num=int(input("enter an integer: "))
#  a=[6,7]
#  print(a[num])
#except ValueError:
#  print("number entered is not an integer")
#except IndexError:
#  print("index error")

#finally keyword
#it is always executed wheather there is an exception or not
#def fun1():
#  try:
#    l=[1,3,5,5]
#    i=int(input("enter the index: "))
#    print(l[i])
#    return 1
#  except:
#    print("some error occured")
#    return 0
#  finally:
#    print("i am always executed")# it used to close the file or database connection without any error

#  print("i am executed when there is no error")


# print('inside the function')
# x=fun1()
# print(x)

#raising custom errors
a=int(input("enter any value between 5 and 9:"))
if(a<5 or a>9):
  raise ValueError("value should be between 5 and 9")
  
