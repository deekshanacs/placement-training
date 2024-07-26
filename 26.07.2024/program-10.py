
amnt=0
n=int(input("Enter number of units consumed :")
if n<=100:
      amnt=0
elif n>100 and n<=200:
      amnt=(nu-100)*5
elif n>200:
     amnt=500+(nu-200)*10
print("Amount to be paid :",amnt)
