tuple1_input = input("Enter the first tuple : ")
tuple1 = tuple(map(int, tuple1_input.split(',')))
tuple2_input = input("Enter the second tuple: ")
tuple2 = tuple(map(int, tuple2_input.split(',')))
tuple1, tuple2 = tuple2, tuple1
print("Swapped tuples:")
print("tuple1:", tuple1)
print("tuple2:", tuple2)
