num = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    ele = int(input("Enter element {}: ".format(i + 1)))
    num.append(ele)
print("Entered elements:", num)
min_number = min(num)
print("Minimum number:", min_number)
