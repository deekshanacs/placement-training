num = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    ele = int(input("Enter element {}: ".format(i + 1)))
    num.append(ele)
print("Entered elements:", num)
max_number = max(num)
print("Maximum number:", max_number)
