a = int(input("Enter side 1 of the triangle : "))
b = int(input("Enter side 2 of the triangle : "))
c = int(input("Enter side 3 of the triangle : "))
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)
