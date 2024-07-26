d = {}
n = int(input("Enter the number of elements: "))

for i in range(n):
    key = input("Enter key: ")
    val = input("Enter value: ")
    d.update({key: val})

def is_key_present(x):
    if x in d:
        print('Key is present in the dictionary')
    else:
        print('Key is not present in the dictionary')

keych = input("Enter key to check: ")
is_key_present(keych)
