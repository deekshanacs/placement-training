def max_value(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max

num = []
n=int(input("Enter the number of elements : "))
for i in range (n,0):
  ele=input("ente rth elements : ")
  num.append(ele)

print(max_value(num))
