#kaun banega crorepati
Questions = [  #list of questions & options
    [
        "which language was used to create fb?", "python", "french",
        "javascript", "php", "None", 4
    ],
    [
        "which language was used to create fb?", "python", "french",
        "javascript", "php", "None", 4
    ],
    [
        "which language was used to create fb?", "python", "french",
        "javascript", "php", "None", 4
    ],
]
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money=0
for i in range(0, len(Questions)):
  Question = Questions[i]
  print(f"\n\nQuestion for Rs.{levels[i]}")
  print(f"a.{Question[1]}      b.{Question[2]}")
  print(f"c.{Question[3]}      d.{Question[4]}")
  reply=int(input("enter yor answer(1-4) or 0 to quit: "))
  if(reply==0):
    money=levels[i-1]
  if(reply==Question[-1]):
   print(f"correct answer,you have won Rs. {levels[i]}")
   if(i==4):
     money=10000
   elif(i==9):
     money=320000
   elif(i==14):
     money=10000000
    
  else:
    print("wrong answere")
    break

print(f"your take home money is {money}")