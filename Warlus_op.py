#WALRUS OPERATOR
# a=True
# #print(a=False)#it can be done by walrus operator
# print(a:=False)
# numbers =[1,2,3,4,5]

# while(n := len(numbers))>0:
#   print(numbers.pop())

#it is new to python 3.8
#assignment expression aka walrus operator
#assign value to variables as part of a large expression

happy=False
print(happy)

print(happy:=True)

# foods=list()
# while True:
#   food= input('what food do you like?: ')
#   if food=="quit":
#     break

#   foods.append(food)


foods=list()
while(food:=input('what food do you like?: ')) != "quit":
  foods.append(food)
