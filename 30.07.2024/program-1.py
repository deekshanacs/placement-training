res = []
numbers_str = input("Enter numbers separated by spaces: ")
numbers = list(map(int, numbers_str.split()))
for i in numbers:
    res.append(i * i)
print(res)
