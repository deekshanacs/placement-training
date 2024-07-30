input_str = input("Enter a string: ")
total = 0
cnt = 0
for char in input_str:
    if char.isdigit():
        total += int(char)
        cnt += 1
if cnt > 0:
    avg = total / cnt
    print("Sum is:", total, "Average is:", avg)
else:
    print("No digits found in the input.")
