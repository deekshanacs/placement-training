def remove_(sample_list, val):
    return [i for i in sample_list if i != val]
user_input = input("Enter numbers separated by commas: ")
value_to_remove = int(input("Enter the value to remove: "))
list1 = [int(num.strip()) for num in user_input.split(",")]
res = remove_(list1, value_to_remove)
print(res)
