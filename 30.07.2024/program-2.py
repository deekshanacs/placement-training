user_input = input("Enter names separated by commas: ")
list1 = [name.strip() for name in user_input.split(",")]
res = list(filter(None, list1))
print(res)
