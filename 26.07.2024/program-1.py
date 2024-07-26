lis=[]
n=int(input("Enter the no.of elements : "))
for i in range (0,n):
    ele=float(input("Enter the elements : "))
    lis.append(ele)
print(lis)
count=sum(lis)
avg = count/len(lis)
print("sum = ", count)
print("average = ", avg)
