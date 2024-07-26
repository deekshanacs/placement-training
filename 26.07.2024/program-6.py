def find_sc(sample_str):
    char_count = 0
    digit_count = 0
    symbol_count = 0
    for char in sample_str:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            symbol_count += 1
    print("Chars =", char_count, "Digits =", digit_count, "Symbols =", symbol_count)
sample_str = input("Enter a string: ")
print("Total counts of chars, digits, and symbols:")
find_sc(sample_str)
